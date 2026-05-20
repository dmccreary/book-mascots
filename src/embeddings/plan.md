# Plan: Mascot Visual Similarity Map

## Context

The book-mascots gallery now has 36 mascots and is growing every time a new sibling textbook is added. Browsing 36 cards alphabetically doesn't surface visual relationships — which mascots look alike (two bald eagles, two tree frogs, two octopuses), which form coherent stylistic families (all the flat-vector cartoon characters vs. the one 3D-rendered tugboat), and which sit alone visually (Tokie the abstract cube, Sparky the lightbulb). A 2D similarity map answers those questions at a glance and gives the user a "design coverage" view of the gallery — useful both for *picking a style* when starting a new mascot and for *spotting visual collisions* (a second squirrel that looks too much like the first).

The user has chosen **visual embeddings (CLIP on each `neutral.png`)** for the first iteration, with textual embeddings deferred as a follow-up. The visualization will be an **interactive Plotly.js scatter** that loads a JSON file and renders each mascot as a thumbnail at its 2D coordinates, with hover tooltips, click-through links, and pan/zoom for free.

## Approach

Three new artifacts, one nav change, zero edits to existing Python:

1. **`src/embeddings/compute_mascot_embeddings.py`** — one-time Python script under a new `src/embeddings/` source tree (the repo's first non-`docs/` source directory). Reads every `docs/mascots/<slug>/neutral.png`, embeds with CLIP (`sentence-transformers` + `clip-ViT-B-32`, runs on CPU in ~30s for 36 images), projects 512-dim → 2D via UMAP (PCA fallback), normalizes coordinates to a `[0, 1000]` SVG viewport, and writes `docs/data/mascot-embeddings.json`.

2. **`docs/mascot-similarity.md`** — markdown page with an inline `<script src="https://cdn.plot.ly/plotly-basic-2.35.2.min.js">` (Plotly's basic bundle — ~1 MB, scatter-only, far lighter than the full ~3 MB Plotly distribution). Fetches the JSON on load and calls `Plotly.newPlot()` with each mascot's `neutral.png` as a `layout.images` entry at its (x, y), plus a transparent scatter trace that supplies hover tooltips (name + textbook) and click events that navigate to the mascot page. Plotly handles pan/zoom/reset out of the box.

3. **`src/embeddings/requirements.txt`** — pins the four packages the embedding script needs, scoped to `src/embeddings/` so it doesn't leak into the main mkdocs build (which stays dep-free).

The script is **manually invoked**, not wired into `update_mascots.py`. Rationale: `update_mascots.py` is stdlib-only and runs in seconds; making it depend on torch would balloon both runtime and install footprint. The user runs `python src/embeddings/compute_mascot_embeddings.py` after importing new mascots, and the script prints a one-line reminder of this in `update_mascots.py`'s summary output so it's hard to forget.

## Files to create

### `src/embeddings/compute_mascot_embeddings.py` (new, ~120 lines)

Single-file script. Structure:

```
1. Constants: MASCOTS_DIR, OUTPUT_JSON, CLIP_MODEL = "clip-ViT-B-32"
2. discover_mascots() → list[(slug, neutral_path, char_name, book_title)]
   - Walks docs/mascots/<slug>/, finds neutral.png (case-insensitive
     pattern, matching update_mascots.py's find_neutral logic)
   - Reuses extract_character_name() and display_title() logic from
     skills/update-mascots/update_mascots.py — import them, do NOT
     duplicate
3. embed_images(records) → np.ndarray of shape (N, 512)
   - sentence-transformers SentenceTransformer(CLIP_MODEL).encode([PIL.Image])
4. project_2d(embeddings) → np.ndarray of shape (N, 2)
   - Try umap.UMAP(n_neighbors=8, min_dist=0.15, metric="cosine", random_state=42)
   - Fall back to sklearn.decomposition.PCA(n_components=2) if umap import fails
5. normalize_to_viewport(xy, padding=60) → xy in [60, 940] range
6. write_json(records, xy, projection_method)
   - Schema: {"model": "clip-ViT-B-32", "projection": "umap",
              "generated_at": "<ISO timestamp>", "viewport": [1000, 1000],
              "points": [{"slug": "...", "name": "Olli the Octopus",
                          "title": "Bioinformatics",
                          "neutral": "mascots/bioinformatics/neutral.png",
                          "x": 412.3, "y": 587.1}, ...]}
7. main() — prints "Embedded N mascots → docs/data/mascot-embeddings.json"
```

**Reuse**: import `extract_character_name`, `display_title`, `find_neutral`,
`name_for` from `skills/update-mascots/update_mascots.py`. The script
prepends `<repo-root>/skills/update-mascots` to `sys.path` at startup
(resolved relative to the script's own `__file__`, so it works regardless
of the current working directory). No code duplication.

### `src/embeddings/requirements.txt` (new, 4 lines)

```
pillow>=10.0
sentence-transformers>=2.7
umap-learn>=0.5
scikit-learn>=1.3
```

(`numpy` and `torch` come in transitively. `scikit-learn` is needed for the PCA fallback even if UMAP is the primary path.)

### `docs/mascot-similarity.md` (new, ~100 lines incl. inline JS)

Page structure:

```markdown
# Mascot Similarity Map

<intro paragraph: explains visual CLIP embedding + UMAP, says
similar-looking mascots cluster; mentions that a textual-similarity
view may come later>

<div id="map" style="width: 100%; height: 80vh;"></div>

<script src="https://cdn.plot.ly/plotly-basic-2.35.2.min.js"></script>
<script>
  fetch("data/mascot-embeddings.json")
    .then(r => r.json())
    .then(renderMap);

  function renderMap(data) {
    const pts = data.points;
    const trace = {
      x: pts.map(p => p.x),
      y: pts.map(p => p.y),
      mode: "markers",
      type: "scatter",
      marker: { size: 60, opacity: 0 },  // invisible hit-area
      customdata: pts.map(p => [p.slug, p.name, p.title]),
      hovertemplate:
        "<b>%{customdata[1]}</b><br>%{customdata[2]}<extra></extra>",
    };
    const layout = {
      images: pts.map(p => ({
        source: p.neutral, x: p.x, y: p.y,
        sizex: 50, sizey: 50,
        xanchor: "center", yanchor: "middle",
        xref: "x", yref: "y", layer: "below",
      })),
      xaxis: { visible: false, scaleanchor: "y" },
      yaxis: { visible: false },
      hovermode: "closest",
      margin: { l: 20, r: 20, t: 20, b: 20 },
      dragmode: "pan",
    };
    Plotly.newPlot("map", [trace], layout,
                   { responsive: true, displaylogo: false });
    document.getElementById("map").on("plotly_click", (e) => {
      const slug = e.points[0].customdata[0];
      window.location.href = `mascots/${slug}/`;
    });
  }
</script>
```

The `layout.images` array places each mascot's neutral.png at its (x, y) as a 50×50 image. The invisible scatter trace provides hover hit-targets (60px markers, opacity 0) and the click handler, since `layout.images` are not interactive on their own. `scaleanchor: "y"` on the x-axis keeps the aspect ratio square so the embedding's geometry isn't distorted by the container width. Plotly's modebar (pan, zoom, reset, snapshot) appears in the corner automatically and is responsive on resize.

**Why Plotly basic (not full)**: This page only needs `scatter` + `layout.images`, both in the `plotly-basic` bundle (~1 MB). The full Plotly distribution adds 3D, maps, finance traces, etc., none of which apply. Pinning to a specific version (`2.35.2`) instead of `plotly-latest.min.js` makes the page reproducible — a Plotly API change two years from now won't silently break the viz.

**Caveat — CDN dependency**: This page won't render in an offline mkdocs build. If offline rendering matters, the follow-up is to vendor `plotly-basic-2.35.2.min.js` into `docs/js/` and update the `<script src>`. Not done in this iteration to keep the change minimal.

### `docs/data/mascot-embeddings.json` (new, generated)

Output of the script. Committed to repo so the page works without re-running the script on every fresh clone.

## Files to modify

### `mkdocs.yml` (1 line added)

Add `- Mascot Similarity Map: mascot-similarity.md` to the top-level nav, immediately after `- Mascot Species Directory:`. Same indent.

### `skills/update-mascots/update_mascots.py` (~3 lines added)

At the end of `main()`'s summary print block, add:

```python
print()
print("To refresh the similarity map after adding mascots, run:")
print("  python src/embeddings/compute_mascot_embeddings.py")
```

Only prints when `new_imports` is non-empty (i.e. genuinely new mascots were added).

## Files NOT touched

- `docs/list-mascots.md` — separate concern (alphabetical gallery, marker-managed)
- `docs/mascot-species-directory.md` — separate concern (taxonomic directory)
- The 36 `docs/mascots/<slug>/index.md` pages — no per-page "similar mascots" section in this iteration (deferred)

## Dependencies introduced

Scoped to `src/embeddings/requirements.txt`. **The mkdocs build itself remains dep-free at the Python level** — no new theme, no new plugin, no new `extra_javascript` entry in `mkdocs.yml`. The similarity page loads Plotly via an inline `<script src="cdn.plot.ly/...">` so the dependency is scoped to that one page and never affects other pages.

Installation is a one-time `pip install -r src/embeddings/requirements.txt` for whoever runs the embedding script. Transitively pulls torch (~2 GB), which is the largest piece. Acceptable for a one-time setup on the author's machine; not required for site visitors or for building the docs.

This is the first directory under `src/` in the repo. If future ML/data-processing tools are added (e.g., a textual-embedding variant, a clustering report, an image deduplication scan), they live under `src/<topic>/` alongside their own `requirements.txt`, keeping each subtree's dependency cost contained.

## Verification

End-to-end test, from a clean checkout:

1. **Install deps** (from repo root): `pip install -r src/embeddings/requirements.txt` — confirm no errors. Torch will be the biggest download.
2. **Run script** (from repo root): `python src/embeddings/compute_mascot_embeddings.py` — confirm output `Embedded 36 mascots → docs/data/mascot-embeddings.json`. Time to first run: ~60s including model download.
3. **Inspect JSON**: `jq '.points | length' docs/data/mascot-embeddings.json` returns `36`. `jq '.points[0]' ...` shows `{slug, name, title, neutral, x, y}` shape.
4. **Build site**: `mkdocs serve` (user runs this themselves per CLAUDE.md). Visit `http://127.0.0.1:8000/book-mascots/mascot-similarity/`.
5. **Visual checks** — all 36 thumbnails render via Plotly's `layout.images`; the page does not show a broken-image grid or an empty Plotly canvas:
   - Hover any thumbnail: Plotly's tooltip appears with the mascot name + textbook title.
   - Click any thumbnail (or its invisible hit-marker): navigates to the corresponding `mascots/<slug>/index.md` page.
   - Plotly's modebar in the top-right works: pan, zoom-to-region, reset.
   - Browser console shows no 404 for the Plotly CDN script or the JSON file.
6. **Cluster sanity check** — eyeball the layout:
   - The two bald eagles (Lex, Liberty) should be near each other.
   - The two tree frogs (Gregor, Mossby) should be near each other.
   - The two octopuses (Olli, Xavi) should be near each other.
   - The two squirrels (Sylvia, Sylvia) should be near each other.
   - Tokie (abstract pink cube) and Sparky (lightbulb) should sit visibly outside the main animal cluster.
   - If any of these fail, switch projection to PCA via a `--projection pca` flag (already in script) and compare; this isolates whether the problem is the embedding (CLIP doing something odd) or the projection (UMAP being weird with N=36).
7. **Re-run resilience** — add a fake mascot dir, re-run `python skills/update-mascots/update_mascots.py`, observe the new reminder line. Re-run `python src/embeddings/compute_mascot_embeddings.py`, observe `Embedded 37 mascots`. Reload the page, see the new point appear. Delete the fake mascot, re-run both scripts, observe N drops back to 36.

## Open follow-ups (NOT in this plan)

- **Textual embeddings as a second view** — embed `image-prompts.md` content and render a sister page `mascot-similarity-by-description.md`. Different clustering axis (discipline, not appearance). User chose to defer this.
- **Per-mascot "Similar mascots" section** — add the 5 nearest neighbors as a card row in each `docs/mascots/<slug>/index.md`. Requires the script to also write a per-mascot neighbors list. Easy add once the embedding pipeline is live.
- **Color-coded categories** — overlay an animal/robot/object/mythical category as point border color. Requires a small category mapping (could live in the script or in a separate YAML).
- **Auto-rebuild trigger** — make `update_mascots.py` optionally invoke `compute_mascot_embeddings.py` when new mascots are imported. Skipped for now to keep `update_mascots.py` stdlib-only.
- **Vendor Plotly locally** — copy `plotly-basic-2.35.2.min.js` into `docs/js/` and change the `<script src>` to point at it. Makes the page work offline and removes the CDN as a point of failure. Worth doing if/when the gallery is mirrored to environments without CDN access.