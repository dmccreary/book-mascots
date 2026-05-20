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

# Canonical display order for the pose grid in each per-mascot index.md.
# Poses not in this list (e.g. "caution", "explain", "beer") sort to the end
# in their original alphabetical order.
CANONICAL_POSE_ORDER = [
    "neutral",
    "welcome",
    "tip",
    "thinking",
    "encouraging",
    "warning",
    "celebration",
]

# Mascot-name display overrides for sources whose prompt files don't parse cleanly.
OVERRIDES: dict[str, str] = {
    "3d-printing-course": "Benchy the Tugboat",
    "cybersecurity": "Sentinel the Fox",
    "intelligent-textbooks": "Axiom the Owl",
    "pre-calc": "Prema",
}

# Display-title overrides for slugs whose naive title-case rendering looks wrong
# (initialisms, acronyms, possessives). Used for the per-mascot page H1, the
# gallery card label, and the mkdocs nav entry.
TITLE_OVERRIDES: dict[str, str] = {
    "right-database": "Selecting the Right Database",
    "us-government": "U.S. Government",
    "us-history": "U.S. History",
    "xapi-course": "xAPI Course",
}

# Files in a sibling mascot dir that are NOT mascot poses — favicons, Android
# Chrome app icons, Apple touch icons, social-graph previews, square logos.
# Filtered out at copy time and excluded from the per-mascot index.md gallery.
ICON_SKIP_RE = re.compile(
    r"^(favicon|android-chrome|apple-touch-icon|.*square|social-graph-preview)",
    re.I,
)

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


def display_title(slug: str) -> str:
    """Human-facing book title for a slug, honoring TITLE_OVERRIDES."""
    return TITLE_OVERRIDES.get(slug, title_case_slug(slug))


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
            r"^(?:Mascot\s+)?(?:AI\s+)?Image\s+(?:Generation\s+)?Prompts?\s*(?:for|of|[:—–-])\s+",
            "",
            title,
            flags=re.I,
        )
        title = re.sub(
            r"\s+((?:Pedagogical\s+)?Mascot\s+Pose\s+Guide|Mascot\s+Image\s+Prompts?|Mascot|Image\s+Prompts?|AI\s+Image.*)$",
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


def canonical_pose_key(filename: str) -> tuple[int, str]:
    """Sort key that orders pose PNGs by CANONICAL_POSE_ORDER.

    Files whose pose stem isn't in CANONICAL_POSE_ORDER sort to the end in
    alphabetical order. "encouragement" is treated as "encouraging".
    """
    pose = pose_name(filename)
    if pose == "encouragement":
        pose = "encouraging"
    if pose in CANONICAL_POSE_ORDER:
        return (CANONICAL_POSE_ORDER.index(pose), filename.lower())
    return (len(CANONICAL_POSE_ORDER), filename.lower())


def write_index_md(dest_dir: Path, slug: str) -> None:
    """Generate docs/mascots/<slug>/index.md showing every pose as a grid card.

    Poses are emitted in CANONICAL_POSE_ORDER (neutral, welcome, tip, thinking,
    encouraging, warning, celebration). Non-canonical poses go to the end.
    """
    files = sorted(
        (p.name for p in dest_dir.glob("*.png")),
        key=canonical_pose_key,
    )
    pose_files = [f for f in files if not ICON_SKIP_RE.match(f)]
    title = display_title(slug)

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
        if ICON_SKIP_RE.match(png.name):
            continue
        shutil.copy2(png, dest / png.name)
    prompt = find_prompt_file(project, mascot_dir)
    if prompt is not None:
        shutil.copy2(prompt, dest / "image-prompts.md")
    write_index_md(dest, slug)


# Markers that delimit the script-managed grid in docs/list-mascots.md.
# Only the content BETWEEN these markers is rewritten on each run; the H1,
# CSS, intro paragraph, and anything after the grid are preserved verbatim.
AUTO_BEGIN = "<!-- begin:auto -->"
AUTO_END = "<!-- end:auto -->"

# Bootstrap template used only when the file is missing entirely. Existing
# files (with or without markers) keep all their custom prose; the marker
# block is auto-migrated in on the first run after upgrade.
LIST_PAGE_DEFAULT_PREAMBLE = """\
# Mascot Gallery

<style>
@media screen and (min-width: 80em) {
  .md-typeset .grid.cards { grid-template-columns: repeat(5, 220px); }
}
</style>

The following list is sorted by the title of the intelligent textbook
that contains the mascot.  Click any mascot below to view all of its poses.

"""


def _build_grid_block(slugs: list[str]) -> str:
    """Return the markdown grid block (the content that goes between markers)."""
    out: list[str] = ['<div class="grid cards" markdown>', ""]
    for slug in slugs:
        dest = MASCOTS_DIR / slug
        neutral = find_neutral(dest)
        if not neutral:
            continue
        book_title = display_title(slug)
        char = name_for(slug, dest)
        out += [
            f"-   **[{book_title}](mascots/{slug}/index.md)**",
            "",
            f"    ![{char}](mascots/{slug}/{neutral}){{ width=220 }}",
            "",
            f"    {char}",
            "",
        ]
    out += ["</div>", ""]
    return "\n".join(out)


def regenerate_list_page() -> list[str]:
    """Rewrite ONLY the auto-managed grid in docs/list-mascots.md.

    Three cases, in order:
      1. File has both AUTO_BEGIN and AUTO_END markers → replace only the
         content between them. All other prose (H1, CSS, intro, footer) is
         preserved verbatim.
      2. File exists but has no markers, yet contains a `<div class="grid
         cards" markdown>` block → auto-migrate by wrapping the existing
         grid in markers, then replace the grid. One-time per file.
      3. File does not exist (or has neither markers nor a grid block) →
         bootstrap from LIST_PAGE_DEFAULT_PREAMBLE + grid + markers.
    """
    slugs = sorted(
        (d.name for d in MASCOTS_DIR.iterdir() if d.is_dir()), key=str.lower
    )
    grid_block = _build_grid_block(slugs)
    new_auto = f"{AUTO_BEGIN}\n{grid_block}{AUTO_END}\n"

    if LIST_PAGE.is_file():
        text = LIST_PAGE.read_text(encoding="utf-8")

        marker_re = re.compile(
            rf"{re.escape(AUTO_BEGIN)}.*?{re.escape(AUTO_END)}\n?",
            re.DOTALL,
        )
        if marker_re.search(text):
            new_text = marker_re.sub(lambda _m: new_auto, text, count=1)
            LIST_PAGE.write_text(new_text, encoding="utf-8")
            return slugs

        grid_re = re.compile(
            r'<div class="grid cards" markdown>.*?</div>\n?',
            re.DOTALL,
        )
        if grid_re.search(text):
            new_text = grid_re.sub(lambda _m: new_auto, text, count=1)
            LIST_PAGE.write_text(new_text, encoding="utf-8")
            return slugs

    LIST_PAGE.write_text(LIST_PAGE_DEFAULT_PREAMBLE + new_auto, encoding="utf-8")
    return slugs


def update_mkdocs_nav(slugs: list[str]) -> None:
    text = MKDOCS_YML.read_text(encoding="utf-8")
    nav_lines = ["  - Mascots:"]
    for slug in sorted(slugs, key=lambda s: display_title(s).lower()):
        nav_lines.append(f"      - {display_title(slug)}: mascots/{slug}/index.md")
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
