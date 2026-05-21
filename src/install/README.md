# install-mascot

Standalone install scripts that copy a single mascot's seven pose
images (plus `image-prompts.md`) from the published
[book-mascots gallery](https://dmccreary.github.io/book-mascots/) into
the local mkdocs textbook project at `docs/img/mascot/`. No clone of
this repo required.

Two parallel implementations, same I/O contract:

| File | Shell | Platform |
|---|---|---|
| [install-mascot.sh](install-mascot.sh) | bash / zsh | macOS, Linux, WSL, Git Bash |
| [install-mascot.ps1](install-mascot.ps1) | PowerShell 5.1+ | Windows native, also cross-platform `pwsh` 7+ |

Both take one positional argument — the mascot **slug** (e.g.
`intelligent-textbooks`, `business`, `us-government`). The full
slug list is rendered live at
[https://dmccreary.github.io/book-mascots/install-mascot/](https://dmccreary.github.io/book-mascots/install-mascot/).

## What the scripts do

1. Create `docs/img/mascot/` in the current working directory
   (which should be the **root** of your mkdocs project — the
   directory that contains `mkdocs.yml`).
2. Download the 7 standard pose PNGs:
   `neutral`, `welcome`, `thinking`, `tip`, `encouraging`,
   `warning`, `celebration`.
3. Save each one with the bare pose name (e.g. `neutral.png`), even
   if the source uses a prefixed filename like `axiom-neutral.png`.
   Target filenames are uniform across mascots.
4. Best-effort copy of `image-prompts.md` (skipped silently if
   absent).
5. Print a one-line `ok`/`ERR` summary per pose and exit non-zero on
   partial failure.

No other changes — no Python deps, no `mkdocs.yml` edits, no extra
CSS.

## Bash usage

### With curl (default on macOS and most Linux)

```bash
# Inspect first, then run (recommended):
curl -O https://raw.githubusercontent.com/dmccreary/book-mascots/main/src/install/install-mascot.sh
chmod +x install-mascot.sh
./install-mascot.sh intelligent-textbooks

# Or one-liner (pipe straight into bash):
curl -sSfL https://raw.githubusercontent.com/dmccreary/book-mascots/main/src/install/install-mascot.sh \
  | bash -s intelligent-textbooks
```

### With wget (default on Debian/Ubuntu base images, Alpine, etc.)

Some minimal Linux environments don't ship `curl` but do include
`wget`. The fetch step has a direct equivalent:

```bash
# Inspect first, then run:
wget https://raw.githubusercontent.com/dmccreary/book-mascots/main/src/install/install-mascot.sh
chmod +x install-mascot.sh
./install-mascot.sh intelligent-textbooks

# Or one-liner:
wget -qO- https://raw.githubusercontent.com/dmccreary/book-mascots/main/src/install/install-mascot.sh \
  | bash -s intelligent-textbooks
```

Flag translation, in case you want to script around it:

| curl | wget | Meaning |
|---|---|---|
| `-O` | (default) | Save to local file using the URL's basename. |
| `-o <path>` | `-O <path>` | Save to a specific path. |
| `-sSfL` | `-q` (silent) | Quiet output and follow redirects on errors. |
| `\|` (pipe) | `-qO-` | Stream the response to stdout for piping. |

Note that **the script itself still uses curl internally** to fetch
the mascot PNGs. If your environment has only wget, you have two
options:

1. **Install curl** — usually `apt-get install -y curl` (Debian/Ubuntu)
   or `apk add curl` (Alpine). One-time, very small download.
2. **Rewrite the four `curl` lines inside the script** to use wget.
   Each `curl -sSfL "$url" -o "$out"` becomes
   `wget -q "$url" -O "$out"`. PRs welcome if you want this as a
   first-class option.

## PowerShell usage

PowerShell uses `Invoke-WebRequest` (alias `iwr`) for HTTP fetches —
the same idea as curl/wget, built in to every Windows install since
Windows 10:

```powershell
# Inspect first, then run (recommended):
Invoke-WebRequest `
  -Uri https://raw.githubusercontent.com/dmccreary/book-mascots/main/src/install/install-mascot.ps1 `
  -OutFile install-mascot.ps1
./install-mascot.ps1 intelligent-textbooks

# Or download to temp, run once, no local copy:
$tmp = Join-Path $env:TEMP 'install-mascot.ps1'
iwr https://raw.githubusercontent.com/dmccreary/book-mascots/main/src/install/install-mascot.ps1 -OutFile $tmp -UseBasicParsing
& $tmp intelligent-textbooks
```

If PowerShell refuses to run the script with an *execution policy*
error, allow signed-or-local scripts for the current user only:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

The `.ps1` script uses `Invoke-WebRequest` internally as well, so
there's no curl/wget question on the PowerShell side.

## Wiring the mascot into your textbook

After install, two common next steps:

1. **Site logo in `mkdocs.yml`**:

    ```yaml
    theme:
      name: material
      logo: img/mascot/neutral.png
      favicon: img/mascot/neutral.png
    ```

2. **Welcome pose at the top of a chapter**:

    ```markdown
    ![Mascot waving](../img/mascot/welcome.png){ width=120 align=right }
    Welcome to the chapter…
    ```

For richer pose-based admonitions, see
[docs/css/mascot.css](../../docs/css/mascot.css) in this repo.

## Troubleshooting

- **`ERR neutral.png (tried …)`** — the slug is misspelled, or the
  mascot uses non-standard pose filenames. Visit the mascot's gallery
  page (e.g. `https://dmccreary.github.io/book-mascots/mascots/<slug>/`)
  to see the actual filenames. If a mascot uses a name-prefix the
  script doesn't yet know about, add a case to the `prefix_for`
  function (bash) or `Get-PosePrefix` function (PowerShell).
- **`curl: command not found`** — see the wget section above, or
  install curl from your distribution's package manager.
- **`Permission denied: ./install-mascot.sh`** — run
  `chmod +x install-mascot.sh` first.
- **Wrong target directory** — run the script from the *root* of
  your mkdocs project (the directory that contains `mkdocs.yml`).
  Both scripts always write into `docs/img/mascot/` relative to the
  current working directory.

## See also

- The user-facing install guide on the published site:
  [Mascot Installation](https://dmccreary.github.io/book-mascots/install-mascot/) — same content as this README plus a live-rendered table of all available mascots.
- The full gallery:
  [Mascot Gallery](https://dmccreary.github.io/book-mascots/list-mascots/).
