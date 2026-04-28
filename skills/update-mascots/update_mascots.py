#!/usr/bin/env python3
"""Sync mascots from sibling book projects into book-mascots."""

from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path

REPO = (Path.home() / "Documents" / "ws" / "book-mascots").resolve()
SIBLINGS_ROOT = REPO.parent
MASCOTS_DIR = REPO / "docs" / "mascots"
LIST_PAGE = REPO / "docs" / "list-mascots.md"
MKDOCS_YML = REPO / "mkdocs.yml"

STANDARD_POSES = {
    "neutral", "welcome", "thinking", "tip",
    "encouraging", "encouragement", "warning", "celebration",
}

# Mascot-name display overrides for sources whose prompt files don't parse cleanly.
OVERRIDES: dict[str, str] = {
    "cybersecurity": "Sentinel the Fox",
    "intelligent-textbooks": "Axiom the Owl",
    "pre-calc": "Prema",
}

# Candidate locations (relative to a sibling project root) where the mascot PNGs live.
MASCOT_DIR_CANDIDATES = [
    "docs/img/mascot",
    "docs/img/mascots",
    "docs/mascots",
    "docs/img/mascot/img",
]

# Candidate prompt-file basenames within the mascot dir, in priority order.
PROMPT_FILE_CANDIDATES = [
    "image-prompts.md",
    "mascot-prompts.md",
    "mascot-descriptions.md",
    "README.md",
]

# Extra prompt-file paths relative to a sibling project root, used when none of the
# in-mascot-dir candidates above are present.
EXTRA_PROMPT_PATHS = [
    "docs/prompts/04-mascot.md",
    "docs/prompts/03-mascot.md",
    "docs/prompts/05-mascot.md",
    "docs/learning-graph/axiom-mascot-guide.md",
    "docs/learning-graph/mascot-guide.md",
]


def pose_name(filename: str) -> str:
    """Strip the optional mascot prefix and return the bare pose stem."""
    stem = Path(filename).stem.lower()
    # e.g. "axiom-neutral" -> "neutral"
    return stem.split("-")[-1]


def find_mascot_dir(project: Path) -> Path | None:
    """Return the first directory under project that holds enough standard pose PNGs."""
    for rel in MASCOT_DIR_CANDIDATES:
        cand = project / rel
        if not cand.is_dir():
            continue
        pngs = list(cand.glob("*.png"))
        poses = {pose_name(p.name) for p in pngs}
        has_neutral = any(p.name.lower().endswith("neutral.png") for p in pngs)
        if has_neutral and len(poses & STANDARD_POSES) >= 3:
            return cand
    return None


def find_prompt_file(project: Path, mascot_dir: Path) -> Path | None:
    for name in PROMPT_FILE_CANDIDATES:
        cand = mascot_dir / name
        if cand.is_file():
            return cand
    for rel in EXTRA_PROMPT_PATHS:
        cand = project / rel
        if cand.is_file():
            return cand
    return None


def title_case_slug(slug: str) -> str:
    return slug.replace("-", " ").replace("_", " ").title()


def extract_character_name(prompt_path: Path | None) -> str | None:
    if not prompt_path or not prompt_path.is_file():
        return None
    text = prompt_path.read_text(encoding="utf-8", errors="replace")

    # Try H1 first.
    m = re.search(r"^#\s+(.+)$", text, re.M)
    if m:
        title = m.group(1).strip()
        # Split on em-dash, en-dash, or " - "
        title = re.split(r"\s+[—–-]\s+", title, maxsplit=1)[0]
        title = re.sub(r"^Mascot:\s*", "", title, flags=re.I).strip(": ").strip()
        title = re.sub(
            r"^(AI\s+)?Image\s+(Generation\s+)?Prompts?\s+(?:for|of)\s+",
            "",
            title,
            flags=re.I,
        )
        title = re.sub(
            r"\s+(Mascot\s+Image\s+Prompts?|Mascot|Image\s+Prompts?|AI\s+Image.*)$",
            "",
            title,
            flags=re.I,
        ).strip()
        if title and not re.fullmatch(r"Mascot\s*Prompts?", title, re.I):
            return title

    # Fallback: **Name:** or **Name (Suggested):** value
    m = re.search(
        r"\*\*Name(?:\s*\(Suggested\))?:?\*\*\s*\*?\*?([^\n*]+)", text
    )
    if m:
        n = m.group(1).strip().strip("*").strip()
        if n:
            return n
    return None


def name_for(slug: str, dest_dir: Path) -> str:
    """Best-effort character name for a mascot already imported into the repo."""
    if slug in OVERRIDES:
        return OVERRIDES[slug]
    for name in PROMPT_FILE_CANDIDATES:
        p = dest_dir / name
        if p.is_file():
            n = extract_character_name(p)
            if n:
                return n
    return title_case_slug(slug)


def find_neutral(dest_dir: Path) -> str | None:
    pngs = sorted(p.name for p in dest_dir.glob("*.png"))
    for n in pngs:
        if re.fullmatch(r".*neutral\.png", n, re.I):
            return n
    return pngs[0] if pngs else None


def write_index_md(dest_dir: Path, slug: str) -> None:
    """Generate docs/mascots/<slug>/index.md showing every pose as a grid card."""
    files = sorted(p.name for p in dest_dir.glob("*.png"))
    skip = re.compile(
        r"^(favicon|android-chrome|apple-touch-icon|.*square|social-graph-preview)",
        re.I,
    )
    pose_files = [f for f in files if not skip.match(f)]
    title = title_case_slug(slug)

    lines = [
        f"# {title}",
        "",
        f"All poses for the **{title}** mascot.",
        "",
        '<div class="grid cards" markdown>',
        "",
    ]
    for pf in pose_files:
        label = Path(pf).stem
        label = re.sub(r"^[a-z]+-", "", label)  # drop "axiom-" style prefixes
        label_disp = label.replace("-", " ").replace("_", " ").title()
        lines += [
            f"-   ![{label_disp}]({pf}){{ width=300 }}",
            "",
            f"    **{label_disp}**",
            "",
        ]
    lines += ["</div>", "", "[← Back to gallery](../../list-mascots.md)", ""]
    (dest_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")


def import_mascot(project: Path, mascot_dir: Path, slug: str) -> None:
    dest = MASCOTS_DIR / slug
    dest.mkdir(parents=True, exist_ok=True)
    for png in mascot_dir.glob("*.png"):
        shutil.copy2(png, dest / png.name)
    prompt = find_prompt_file(project, mascot_dir)
    if prompt is not None:
        shutil.copy2(prompt, dest / "image-prompts.md")
    write_index_md(dest, slug)


def regenerate_list_page() -> list[str]:
    """Rewrite docs/list-mascots.md. Returns the slugs in the order they were emitted."""
    slugs = sorted(
        (d.name for d in MASCOTS_DIR.iterdir() if d.is_dir()), key=str.lower
    )
    out = [
        "# Mascot Gallery",
        "",
        "Click any mascot below to view all of its poses.",
        "",
        '<div class="grid cards" markdown>',
        "",
    ]
    for slug in slugs:
        dest = MASCOTS_DIR / slug
        neutral = find_neutral(dest)
        if not neutral:
            continue
        book_title = title_case_slug(slug)
        char = name_for(slug, dest)
        out += [
            f"-   **[{book_title}](mascots/{slug}/index.md)**",
            "",
            f"    ![{char}](mascots/{slug}/{neutral}){{ width=200 }}",
            "",
            f"    {char}",
            "",
        ]
    out += ["</div>", ""]
    LIST_PAGE.write_text("\n".join(out), encoding="utf-8")
    return slugs


def update_mkdocs_nav(slugs: list[str]) -> None:
    text = MKDOCS_YML.read_text(encoding="utf-8")
    nav_lines = ["  - Mascots:"]
    for slug in sorted(slugs, key=lambda s: title_case_slug(s).lower()):
        nav_lines.append(f"      - {title_case_slug(slug)}: mascots/{slug}/index.md")
    new_block = "\n".join(nav_lines)

    # Replace an existing "  - Mascots:" block, or append it under nav:.
    pattern = re.compile(
        r"^  - Mascots:\n(?:      - .+\n)*", re.M
    )
    if pattern.search(text):
        text = pattern.sub(new_block + "\n", text)
    else:
        # Append after the last existing top-level nav entry.
        text = text.rstrip() + "\n" + new_block + "\n"
    MKDOCS_YML.write_text(text, encoding="utf-8")


def main() -> int:
    if not MASCOTS_DIR.is_dir():
        print(f"ERROR: {MASCOTS_DIR} does not exist", file=sys.stderr)
        return 1

    existing = {d.name for d in MASCOTS_DIR.iterdir() if d.is_dir()}
    new_imports: list[str] = []
    skipped: list[tuple[str, str]] = []

    for project in sorted(SIBLINGS_ROOT.iterdir()):
        if not project.is_dir() or project.resolve() == REPO:
            continue
        slug = project.name
        if slug in existing:
            continue
        mascot_dir = find_mascot_dir(project)
        if mascot_dir is None:
            # Only mention it if there's a hint of a mascot dir we rejected.
            for rel in MASCOT_DIR_CANDIDATES:
                if (project / rel).is_dir():
                    skipped.append(
                        (slug, f"{rel} present but missing neutral.png or <3 poses")
                    )
                    break
            continue
        import_mascot(project, mascot_dir, slug)
        new_imports.append(slug)

    slugs = regenerate_list_page()
    update_mkdocs_nav(slugs)

    print()
    print("=" * 60)
    print("update-mascots summary")
    print("=" * 60)
    print(f"New mascots imported: {len(new_imports)}")
    for s in new_imports:
        print(f"  + {s}")
    print(f"Total mascots in repo: {len(slugs)}")
    if skipped:
        print(f"Skipped sibling projects: {len(skipped)}")
        for slug, reason in skipped:
            print(f"  - {slug}: {reason}")
    print("Updated: docs/list-mascots.md, mkdocs.yml")
    return 0


if __name__ == "__main__":
    sys.exit(main())
