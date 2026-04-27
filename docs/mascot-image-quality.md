# Mascot Image Quality

A mascot library is only as good as the underlying image files. Two technical details matter more than any prompt-engineering trick: **the background must be truly transparent**, and **there must be no padding around the character**. This page explains why, and shows the tools and tricks we use to verify both.

## Why transparent backgrounds matter

The same mascot image gets embedded in many surfaces — a light-themed website, a dark-themed website, a slide deck with a colored background, a PDF, a chatbot bubble. If the PNG has any background fill at all, that fill will show up as an ugly rectangle the moment the surrounding surface is a different color.

Concretely:

- **Light/dark mode toggling.** MkDocs Material, like most modern doc sites, supports both light and dark color schemes. A mascot saved on a white background looks fine in light mode and looks like a glowing white sticker in dark mode. A mascot saved on a black background has the opposite problem.
- **Slide decks and printed material.** Authors will drop these mascots onto whatever background the deck template uses. Pastel, dark navy, brand colors — none of those should fight the mascot.
- **Chatbots and avatars.** When a mascot is rendered as a circular avatar, anything in the corners (including a "transparent-looking" near-white) becomes visible.

The rule: every PNG in this repo must have a fully transparent background — alpha channel zero — with no white, off-white, light gray, or checkerboard fill. The image generator's prompt explicitly asks for this, and we still verify after the fact, because models cheat.

### A common failure mode

Many image generators silently produce a *near-white* background that *looks* transparent on a white page but turns into a visible square on a dark page. The fix is always the same: re-export with a real alpha channel, or run the image through a background-removal pass.

## Why padding around the character matters

The second invisible-on-a-white-page problem is **padding**: extra empty pixels around the character that are technically transparent but still part of the image bounds. Padding causes:

- **Inconsistent sizing.** Two mascots with the same `width=200` look like different sizes if one has 30px of padding and the other has none.
- **Awkward text wrap.** When a mascot floats next to a paragraph, padding pushes the text away from the visible character — readers see a gap, not a tight illustration.
- **Bad alignment in grids.** The Mascot Gallery on this site uses a grid-card layout. Cards with padded images look misaligned compared to cards with tight crops.

The rule: trim each PNG so the character touches at least one edge on each axis (top, bottom, left, right) — or comes very close. The character should fill its bounding box.

## Tools we use

### Background removal and trimming

- **`trim-mascot-padding` skill** — a project-side skill that walks a directory, opens each PNG, finds the alpha-channel bounding box, and rewrites the file cropped to that box. Idempotent — running it twice does nothing the second time. This is the workhorse.
- **ImageMagick** — `convert input.png -trim +repage output.png` does the same thing in one shell command. Useful for one-offs.
- **Python + Pillow** — for batch jobs:
  ```python
  from PIL import Image
  im = Image.open("neutral.png")
  bbox = im.getbbox()  # bounding box of non-zero alpha
  im.crop(bbox).save("neutral.png")
  ```
- **remove.bg / Photoroom / Adobe Express** — web tools for stripping near-white backgrounds out of an image when the generator left some behind. Use these *before* trimming padding, not after.
- **GIMP / Photoshop / Pixelmator** — for the rare case that a model bakes a faint shadow halo into the alpha channel. Manual touch-up; usually not needed.

### Verifying transparency

Open the PNG on a known dark background. The mkdocs-material dark mode is convenient for this — flip the theme toggle on a page that embeds the mascot, and any non-transparent fringe will reveal itself instantly.

If you want to be programmatic, look at the alpha histogram with Pillow:

```python
from PIL import Image
im = Image.open("neutral.png").convert("RGBA")
alphas = im.split()[-1].getextrema()  # (min, max)
print(alphas)
```

If `min` is anything other than 0, the corners aren't fully transparent.

## Visualizing padding with a CSS border

The fastest way to *see* whether a mascot has padding is to draw a one-pixel border around the image element on the page. Anywhere the border sits far away from the character, that's padding.

Add this to a `docs/stylesheets/extra.css` (or any custom stylesheet referenced from `mkdocs.yml`):

```css
/* Toggle this on while auditing mascot crops. Remove or comment out for production. */
.mascot-debug img,
.grid.cards img {
    border: 1px solid red;
    background: rgba(255, 0, 255, 0.05); /* magenta tint shows transparent pixels */
}
```

Wire it up in `mkdocs.yml`:

```yaml
extra_css:
  - stylesheets/extra.css
```

Now reload the gallery. Every mascot card shows a red rectangle around the image. A well-cropped mascot's character will touch (or nearly touch) all four sides of the rectangle. A badly cropped one will float in the middle with obvious gaps.

You can also scope the border to one mascot for spot checks by wrapping the image in a `div`:

```markdown
<div class="mascot-debug">
![Olli](mascots/bioinformatics/neutral.png){ width=200 }
</div>
```

When the audit is done, comment the rule out — you don't want red boxes in production.

### Checking on a dark background

While you're auditing, also check the *transparency* with a temporary background:

```css
.mascot-debug img {
    border: 1px solid red;
    background: #111;  /* near-black to expose any white fringe */
}
```

If you see any pale halo around the character, the alpha channel is dirty and the image needs a background-removal pass.

## Quality checklist

Before committing a new mascot to this repo, confirm:

- [ ] PNG opens with a transparent corner pixel (alpha = 0).
- [ ] No visible halo when shown against a dark background.
- [ ] No padding — character touches at least three edges of the bounding box.
- [ ] All seven poses are at consistent scale (e.g., the head is roughly the same size across `neutral`, `welcome`, `thinking`, etc.).
- [ ] File size is reasonable — under ~200KB per pose. Larger files usually mean uncompressed alpha or an unnecessarily large source resolution.
- [ ] Filename matches the standard pose vocabulary: `neutral.png`, `welcome.png`, `thinking.png`, `tip.png`, `encouraging.png`, `warning.png`, `celebration.png`.

A mascot that fails any of these will look subtly broken in at least one place it ends up. Catch it once, here, instead of fixing it across every book that pulls it in.
