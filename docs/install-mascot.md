# Mascot Installation

This page describes how to install **a single mascot's pose images**
into your own mkdocs textbook project, without cloning the entire
`book-mascots` repository. You give the install script a mascot slug
(e.g., `intelligent-textbooks`, `business`, `us-government`) and it
downloads the seven standard pose PNGs plus the `image-prompts.md`
reference into `docs/img/mascot/` of the current project.

## Quick install

From the root directory of your mkdocs project, run **one** of the
following:

### Option A — inspect first, then run (recommended)

```bash
curl -O https://raw.githubusercontent.com/dmccreary/book-mascots/main/src/install/install-mascot.sh
chmod +x install-mascot.sh
./install-mascot.sh <slug>
```

This downloads the script, lets you read it before executing, and
keeps a copy in your project for repeat runs.

### Option B — one-liner (no local copy of the script)

```bash
curl -sSfL https://raw.githubusercontent.com/dmccreary/book-mascots/main/src/install/install-mascot.sh \
  | bash -s <slug>
```

Faster, but you're piping a remote script straight into `bash`. Only
use this if you trust the source (and ideally only after running
Option A once to read the script).

## Example

Install Axiom the Owl, the mascot for the *Intelligent Textbooks*
guide:

```bash
./install-mascot.sh intelligent-textbooks
```

Output:

```
Installing mascot 'intelligent-textbooks' to docs/img/mascot/
  ok  neutral.png
  ok  welcome.png
  ok  thinking.png
  ok  tip.png
  ok  encouraging.png
  ok  warning.png
  ok  celebration.png
  ok  image-prompts.md

Installed 'intelligent-textbooks' to docs/img/mascot/
```

## What the script does

1. Validates that exactly one argument (the mascot slug) was given.
2. Creates `docs/img/mascot/` in the current working directory.
3. For each of the seven standard poses (`neutral`, `welcome`,
   `thinking`, `tip`, `encouraging`, `warning`, `celebration`),
   downloads the corresponding PNG from the published gallery at
   `https://dmccreary.github.io/book-mascots/mascots/<slug>/`.
4. Saves each file with the bare pose name (e.g., `neutral.png`),
   even if the source uses a name-prefix like `axiom-neutral.png`.
   This gives your project consistent filenames regardless of which
   mascot you install.
5. Tries to copy `image-prompts.md` (the source-of-truth prompts for
   regenerating the poses); absence is non-fatal.
6. Reports a summary and exits non-zero if any pose failed.

No other changes to your project — no Python deps, no mkdocs.yml
edits, no extra CSS.

## Available mascots

Copy a slug from the **Slug** column below, then run the install
script with it. The table renders live from the published embeddings
manifest, so it stays in sync with the gallery as mascots are added.

<div id="mascot-table">Loading…</div>

<script>
  // The page lives at /<base>/install-mascot/ (mkdocs default
  // use_directory_urls=true), so the data path needs a "../" prefix
  // to escape the page directory.
  fetch("../data/mascot-embeddings.json")
    .then(r => r.json())
    .then(d => {
      const rows = d.points
        .slice()
        .sort((a, b) => a.slug.localeCompare(b.slug))
        .map(p => `
          <tr>
            <td><code>${p.slug}</code></td>
            <td>${p.name}</td>
            <td>${p.title}</td>
            <td><a href="../mascots/${p.slug}/">view</a></td>
          </tr>`)
        .join("");
      document.getElementById("mascot-table").innerHTML = `
        <table>
          <thead>
            <tr>
              <th>Slug</th>
              <th>Character</th>
              <th>Textbook</th>
              <th>Gallery</th>
            </tr>
          </thead>
          <tbody>${rows}</tbody>
        </table>`;
    })
    .catch(e => {
      document.getElementById("mascot-table").textContent =
        "Could not load the mascot list. See the Mascot Gallery " +
        "for the full set of available mascots.";
      console.error(e);
    });
</script>

## Script source

The script is open source at
[src/install/install-mascot.sh](https://github.com/dmccreary/book-mascots/blob/main/src/install/install-mascot.sh).
For inspection, the full source is reproduced below — short enough
to read top to bottom:

```bash
#!/usr/bin/env bash
# Install a single mascot's pose images into the local mkdocs project.
#
# Usage:
#   ./install-mascot.sh <slug>
#
# Example:
#   ./install-mascot.sh intelligent-textbooks

set -euo pipefail

readonly BASE_URL="https://dmccreary.github.io/book-mascots/mascots"
readonly TARGET="docs/img/mascot"
readonly POSES=(neutral welcome thinking tip encouraging warning celebration)

# A handful of mascots use a name-prefix on each pose file (e.g.,
# axiom-neutral.png instead of neutral.png). Map those slugs to the
# prefix string used in their source filenames. Extend as needed.
prefix_for() {
  case "$1" in
    intelligent-textbooks) printf 'axiom-' ;;
    *) printf '' ;;
  esac
}

[ $# -eq 1 ] || { echo "Usage: $0 <slug>" >&2; exit 1; }
readonly SLUG="$1"
readonly PREFIX="$(prefix_for "$SLUG")"

mkdir -p "$TARGET"
echo "Installing mascot '${SLUG}' to ${TARGET}/"

errors=0
for pose in "${POSES[@]}"; do
  url="${BASE_URL}/${SLUG}/${PREFIX}${pose}.png"
  out="${TARGET}/${pose}.png"
  if curl -sSfL "$url" -o "$out"; then
    echo "  ok  ${pose}.png"
  else
    echo "  ERR ${pose}.png  (tried ${url})" >&2
    errors=$((errors + 1))
  fi
done

curl -sSfL "${BASE_URL}/${SLUG}/image-prompts.md" \
     -o "${TARGET}/image-prompts.md" \
  && echo "  ok  image-prompts.md" \
  || { echo "  --  image-prompts.md not available (non-fatal)"; \
       rm -f "${TARGET}/image-prompts.md"; }

[ "$errors" -eq 0 ] || { echo "${errors} pose(s) failed." >&2; exit 1; }
echo ""
echo "Installed '${SLUG}' to ${TARGET}/"
```

## Where the files land

```text
your-project/
└── docs/
    └── img/
        └── mascot/
            ├── neutral.png
            ├── welcome.png
            ├── thinking.png
            ├── tip.png
            ├── encouraging.png
            ├── warning.png
            ├── celebration.png
            └── image-prompts.md
```

## Wiring the mascot into your textbook

Once the files are installed, two common next steps:

1. **Reference the neutral pose in `mkdocs.yml`** as the site logo:

    ```yaml
    theme:
      name: material
      logo: img/mascot/neutral.png
      favicon: img/mascot/neutral.png
    ```

2. **Use the welcome pose at the top of a chapter**:

    ```markdown
    ![Mascot waving](../img/mascot/welcome.png){ width=120 align=right }
    Welcome to the chapter…
    ```

For richer pose-based admonitions (themed callouts that pair a mascot
image with a colored banner), see the styling in
[docs/css/mascot.css](https://github.com/dmccreary/book-mascots/blob/main/docs/css/mascot.css).

## Troubleshooting

- **`ERR neutral.png (tried …)`** — the slug is misspelled or the
  mascot uses non-standard pose filenames. Visit the per-mascot page
  in the gallery (e.g.,
  `https://dmccreary.github.io/book-mascots/mascots/<slug>/`) to see
  the actual filenames. If the mascot uses a prefix the script
  doesn't yet know about, add a case to the `prefix_for` function and
  re-run.
- **`curl: command not found`** — install curl, or use `wget` with
  the same URLs.
- **Permission denied on `./install-mascot.sh`** — run
  `chmod +x install-mascot.sh` first.
- **Wrong target directory** — run the script from the *root* of
  your mkdocs project (the directory that contains `mkdocs.yml`).
  The script always writes into `docs/img/mascot/` relative to the
  current working directory.

## License

Mascots are released under the same license as the book-mascots
repository. See
[the project license](https://github.com/dmccreary/book-mascots/blob/main/LICENSE)
for terms; attribution back to the source project is appreciated.
