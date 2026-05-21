# Mascot embeddings

Computes visual CLIP embeddings for every mascot's `neutral.png`,
projects them to 2D with UMAP, and writes
`docs/data/mascot-embeddings.json` for the
[Mascot Similarity Map](../../docs/mascot-similarity.md) page.

## Setup

Conda-first — pure `pip install` does not work on Python 3.13 + Intel
macOS because torch and llvmlite have no matching wheels there.

```bash
# Fresh env (creates a conda env named "mkdocs"):
conda env create -n mkdocs -f src/embeddings/environment.yml

# Existing env (most common — the project's mkdocs env already exists):
conda env update -n mkdocs -f src/embeddings/environment.yml
```

If your conda env is named something other than `mkdocs`, substitute it
in the `-n` flag.

## Run

```bash
python src/embeddings/compute_mascot_embeddings.py
```

Takes ~10 seconds on CPU once the CLIP weights are cached (~30 seconds
on first run while the model downloads). Output goes to
`docs/data/mascot-embeddings.json` and is checked into the repo so the
similarity-map page works on every clone without re-running this script.

## When to re-run

After importing a new mascot via
`python skills/update-mascots/update_mascots.py`. That script prints a
reminder line at the end of its summary.

## Options

```
--projection {umap,pca}    2D projection method (default: umap)
```

UMAP is non-linear and clusters tightly; PCA is linear and preserves
overall geometry. With only ~36 mascots either works; UMAP gives
visibly tighter same-species clusters in this dataset.
