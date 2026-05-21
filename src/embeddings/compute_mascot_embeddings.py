#!/usr/bin/env python3
"""Compute visual CLIP embeddings for every mascot and project to 2D.

Reads docs/mascots/<slug>/neutral.png for every slug, embeds with
sentence-transformers' clip-ViT-B-32, projects 512-dim -> 2D via UMAP
(falling back to PCA if UMAP import fails), and writes the result to
docs/data/mascot-embeddings.json for consumption by the mascot-similarity
page.

Setup (conda-first — see src/embeddings/README.md):
    conda env update -n mkdocs -f src/embeddings/environment.yml

Run from anywhere:
    python src/embeddings/compute_mascot_embeddings.py
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Reuse the mascot-discovery helpers from update_mascots.py instead of
# duplicating them. The update-mascots directory has a hyphen (fine for
# sys.path) but the module file uses an underscore.
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT / "skills" / "update-mascots"))
from update_mascots import (  # noqa: E402
    MASCOTS_DIR,
    display_title,
    find_neutral,
    name_for,
)

OUTPUT_JSON = REPO_ROOT / "docs" / "data" / "mascot-embeddings.json"
CLIP_MODEL = "clip-ViT-B-32"
VIEWPORT = (1000, 1000)
VIEWPORT_PADDING = 60


def discover_mascots() -> list[dict]:
    """One record per mascot dir that has a usable neutral pose."""
    records: list[dict] = []
    for d in sorted(MASCOTS_DIR.iterdir(), key=lambda p: p.name.lower()):
        if not d.is_dir():
            continue
        slug = d.name
        neutral = find_neutral(d)
        if not neutral:
            continue
        records.append(
            {
                "slug": slug,
                "name": name_for(slug, d),
                "title": display_title(slug),
                "neutral": f"mascots/{slug}/{neutral}",
                "neutral_path": d / neutral,
            }
        )
    return records


def embed_images(records: list[dict]):
    """Return an (N, 512) numpy array of CLIP image embeddings."""
    from PIL import Image
    from sentence_transformers import SentenceTransformer

    print(f"Loading CLIP model: {CLIP_MODEL} ...", flush=True)
    model = SentenceTransformer(CLIP_MODEL)
    images = [Image.open(r["neutral_path"]).convert("RGB") for r in records]
    print(f"Encoding {len(images)} images ...", flush=True)
    return model.encode(images, convert_to_numpy=True, show_progress_bar=True)


def project_2d(embeddings, method: str = "umap"):
    """Project (N, D) embeddings to (N, 2). Returns (xy, method_used)."""
    if method == "umap":
        try:
            from umap import UMAP

            print("Projecting with UMAP ...", flush=True)
            reducer = UMAP(
                n_neighbors=8,
                min_dist=0.15,
                metric="cosine",
                random_state=42,
            )
            return reducer.fit_transform(embeddings), "umap"
        except ImportError:
            print("UMAP not available, falling back to PCA", flush=True)
            method = "pca"
    from sklearn.decomposition import PCA

    print("Projecting with PCA ...", flush=True)
    return PCA(n_components=2, random_state=42).fit_transform(embeddings), "pca"


def normalize_to_viewport(xy, padding: int = VIEWPORT_PADDING):
    """Scale (N, 2) into the VIEWPORT box with padding on each side."""
    import numpy as np

    xy = np.asarray(xy, dtype=float)
    w, h = VIEWPORT
    out = np.empty_like(xy)
    for axis, span in enumerate((w, h)):
        col = xy[:, axis]
        lo, hi = col.min(), col.max()
        if hi - lo < 1e-9:
            out[:, axis] = span / 2.0
        else:
            out[:, axis] = padding + (col - lo) / (hi - lo) * (span - 2 * padding)
    return out


def write_json(records, xy, projection_method: str) -> None:
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    points = [
        {
            "slug": r["slug"],
            "name": r["name"],
            "title": r["title"],
            "neutral": r["neutral"],
            "x": round(float(xy[i, 0]), 2),
            "y": round(float(xy[i, 1]), 2),
        }
        for i, r in enumerate(records)
    ]
    payload = {
        "model": CLIP_MODEL,
        "projection": projection_method,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "viewport": list(VIEWPORT),
        "points": points,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--projection",
        choices=("umap", "pca"),
        default="umap",
        help="2D projection method (default: umap, falls back to pca)",
    )
    args = parser.parse_args()

    records = discover_mascots()
    if not records:
        print(
            f"ERROR: no mascots with neutral.png found in {MASCOTS_DIR}",
            file=sys.stderr,
        )
        return 1
    print(f"Found {len(records)} mascots with neutral.png")
    embeddings = embed_images(records)
    xy, method_used = project_2d(embeddings, method=args.projection)
    xy = normalize_to_viewport(xy)
    write_json(records, xy, method_used)
    rel = OUTPUT_JSON.relative_to(REPO_ROOT)
    print(f"Embedded {len(records)} mascots -> {rel}")
    print(f"  model: {CLIP_MODEL}")
    print(f"  projection: {method_used}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
