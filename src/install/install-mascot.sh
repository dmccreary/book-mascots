#!/usr/bin/env bash
# Install a single mascot's pose images into the local mkdocs project.
#
# Usage:
#   ./install-mascot.sh <slug>
#
# Example:
#   ./install-mascot.sh intelligent-textbooks
#
# What it does:
#   1. Creates docs/img/mascot/ in the current working directory
#      (which must be the root of your mkdocs project).
#   2. Downloads 7 standard pose PNGs from the published gallery at
#      https://dmccreary.github.io/book-mascots/
#   3. Copies image-prompts.md as a reference for regenerating poses.
#
# Source: https://github.com/dmccreary/book-mascots
# License: same as the book-mascots repository.

set -euo pipefail

readonly BASE_URL="https://dmccreary.github.io/book-mascots/mascots"
readonly TARGET="docs/img/mascot"
readonly POSES=(neutral welcome thinking tip encouraging warning celebration)

usage() {
  cat >&2 <<EOF
Usage: $(basename "$0") <slug>

Install a single mascot's pose images into the current mkdocs project.

Arguments:
  <slug>  The mascot slug, e.g. "intelligent-textbooks", "business",
          "us-government". The full list with slugs lives at:
          https://dmccreary.github.io/book-mascots/install-mascot/

Output (relative to current directory):
  ${TARGET}/{neutral,welcome,thinking,tip,encouraging,warning,celebration}.png
  ${TARGET}/image-prompts.md
EOF
  exit 1
}

# A handful of mascots use a name-prefix on each pose file (e.g.,
# axiom-neutral.png instead of neutral.png). Map those slugs to the
# prefix string used in their source filenames. Extend as needed.
prefix_for() {
  case "$1" in
    intelligent-textbooks) printf 'axiom-' ;;
    *) printf '' ;;
  esac
}

[ $# -eq 1 ] || usage
readonly SLUG="$1"
[ -n "$SLUG" ] || usage

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

# image-prompts.md is reference material; absence is non-fatal.
if curl -sSfL "${BASE_URL}/${SLUG}/image-prompts.md" \
        -o "${TARGET}/image-prompts.md"; then
  echo "  ok  image-prompts.md"
else
  echo "  --  image-prompts.md not available (non-fatal)"
  rm -f "${TARGET}/image-prompts.md"
fi

if [ "$errors" -gt 0 ]; then
  echo "" >&2
  echo "${errors} pose(s) failed to download." >&2
  echo "Check that '${SLUG}' is a real mascot slug at:" >&2
  echo "  https://dmccreary.github.io/book-mascots/install-mascot/" >&2
  echo "Or inspect the live gallery for this mascot at:" >&2
  echo "  ${BASE_URL}/${SLUG}/" >&2
  exit 1
fi

echo ""
echo "Installed '${SLUG}' to ${TARGET}/"
