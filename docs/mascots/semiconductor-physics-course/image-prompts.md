# Nova — Image Generation Prompts

Self-contained prompts for generating each of Nova's seven poses. Each
prompt embeds the full base character description so it can be pasted
into any AI image generator (ChatGPT/DALL-E, Midjourney, Stable Diffusion)
without referring to a separate base block.

**Output requirements for every pose:**

- PNG file, fully transparent background
- 1024 x 1024 pixels (will be displayed at 90px in admonitions)
- Centered subject, minimal padding
- No text or watermarks in the image

After generating, run the padding trimmer on each file:

```bash
python $BK_HOME/src/image-utils/trim-padding-from-image.py docs/img/mascot/neutral.png
python $BK_HOME/src/image-utils/trim-padding-from-image.py docs/img/mascot/welcome.png
python $BK_HOME/src/image-utils/trim-padding-from-image.py docs/img/mascot/thinking.png
python $BK_HOME/src/image-utils/trim-padding-from-image.py docs/img/mascot/tip.png
python $BK_HOME/src/image-utils/trim-padding-from-image.py docs/img/mascot/warning.png
python $BK_HOME/src/image-utils/trim-padding-from-image.py docs/img/mascot/encouraging.png
python $BK_HOME/src/image-utils/trim-padding-from-image.py docs/img/mascot/celebration.png
```

---

I am about to ask you to generate 7 mascot image poses for a semiconductor physics textbook.
Please try to make all the images use a consistent drawing style.

## 1. Neutral / Default Pose — `neutral.png`

```
Please generate a new neutral pose for Nova the Electron Sprite.

A modern flat-vector illustration of Nova, a friendly pedagogical mascot
for a college-level semiconductor physics textbook. Nova is an
anthropomorphized electron — a round, smooth cyan-blue sphere (#0288d1)
with a soft outer glow halo. A faint "−" minus-charge symbol marks the
body. Nova has small, expressive cartoon arms and hands extending from
the sphere. Big friendly cartoon eyes, no outlined facial features,
playful smile. Bright orange (#ff9800) is used sparingly for small energy
sparks. Style: modern flat vector, clean bold fills, soft radial glow
halo, no gradients beyond the glow. No text, no watermark.

Pose: Nova floats upright in a relaxed, neutral pose facing the viewer
directly with a calm, friendly closed-mouth smile. Hands rest naturally
at the sides with no specific gesture. The pose is balanced and
unassuming — suitable as a general-purpose or default illustration.

Filename: neutral.png

Please generate a new PNG image now with a fully transparent background.
The background MUST be fully transparent. DO NOT use a white, black, or
checkered background.
```

---

## 2. Welcome / Introduction Pose — `welcome.png`

```
Please generate a new welcome pose for Nova the Electron Sprite.

A modern flat-vector illustration of Nova, a friendly pedagogical mascot
for a college-level semiconductor physics textbook. Nova is an
anthropomorphized electron — a round, smooth cyan-blue sphere (#0288d1)
with a soft outer glow halo. A faint "−" minus-charge symbol marks the
body. Nova has small, expressive cartoon arms and hands extending from
the sphere. Big friendly cartoon eyes, no outlined facial features,
playful smile. Bright orange (#ff9800) is used sparingly for small energy
sparks. Style: modern flat vector, clean bold fills, soft radial glow
halo, no gradients beyond the glow. No text, no watermark.

Pose: Nova waves cheerfully with one raised hand, facing the viewer with
a warm, welcoming smile. The free hand sits at the side. A small orange
spark trails the waving hand to suggest movement and energy. The pose
reads as "welcome" and "let's get started."

Filename: welcome.png

Please generate a new PNG image now with a fully transparent background.
The background MUST be fully transparent. DO NOT use a white, black, or
checkered background.
```

---

## 3. Thinking / Teaching Pose — `thinking.png`

```
Please generate a new thinking pose for Nova the Electron Sprite.

A modern flat-vector illustration of Nova, a friendly pedagogical mascot
for a college-level semiconductor physics textbook. Nova is an
anthropomorphized electron — a round, smooth cyan-blue sphere (#0288d1)
with a soft outer glow halo. A faint "−" minus-charge symbol marks the
body. Nova has small, expressive cartoon arms and hands extending from
the sphere. Big friendly cartoon eyes, no outlined facial features,
playful smile. Bright orange (#ff9800) is used sparingly for small energy
sparks. Style: modern flat vector, clean bold fills, soft radial glow
halo, no gradients beyond the glow. No text, no watermark.

Pose: Nova holds one hand under the chin in a thoughtful gesture, eyes
glancing slightly upward. A small lightbulb or thought bubble glows above
Nova's head with a soft orange tint. The expression suggests focused
curiosity and discovery.

Filename: thinking.png

Please generate a new PNG image now with a fully transparent background.
The background MUST be fully transparent. DO NOT use a white, black, or
checkered background.
```

---

## 4. Pointing / Tip Pose — `tip.png`

```
Please generate a new tip pose for Nova the Electron Sprite.

A modern flat-vector illustration of Nova, a friendly pedagogical mascot
for a college-level semiconductor physics textbook. Nova is an
anthropomorphized electron — a round, smooth cyan-blue sphere (#0288d1)
with a soft outer glow halo. A faint "−" minus-charge symbol marks the
body. Nova has small, expressive cartoon arms and hands extending from
the sphere. Big friendly cartoon eyes, no outlined facial features,
playful smile. Bright orange (#ff9800) is used sparingly for small energy
sparks. Style: modern flat vector, clean bold fills, soft radial glow
halo, no gradients beyond the glow. No text, no watermark.

Pose: Nova points upward with one index finger as if sharing an important
tip. The expression is helpful and knowing, with a small confident smirk.
A small orange star or sparkle floats just above the pointing fingertip.

Filename: tip.png

Please generate a new PNG image now with a fully transparent background.
The background MUST be fully transparent. DO NOT use a white, black, or
checkered background.
```

---

## 5. Warning / Caution Pose — `warning.png`

```
Please generate a new friendly warning pose for Nova the Electron Sprite.

A modern flat-vector illustration of Nova, a friendly pedagogical mascot
for a college-level semiconductor physics textbook. Nova is an
anthropomorphized electron — a round, smooth cyan-blue sphere (#0288d1)
with a soft outer glow halo. A faint "−" minus-charge symbol marks the
body. Nova has small, expressive cartoon arms and hands extending from
the sphere. Big friendly cartoon eyes, no outlined facial features,
playful smile. Bright orange (#ff9800) is used sparingly for small energy
sparks. Style: modern flat vector, clean bold fills, soft radial glow
halo, no gradients beyond the glow. No text, no watermark.

Pose: Nova holds up both hands in a gentle "stop" or "be careful"
gesture, palms facing forward. The expression is concerned but caring —
slightly raised eyebrows, small worried smile. A small orange exclamation
mark floats near the head.

Filename: warning.png

Please generate a new PNG image now with a fully transparent background.
The background MUST be fully transparent. DO NOT use a white, black, or
checkered background.
```

---

## 6. Encouraging Pose — `encouraging.png`

```
Please generate a new encouraging pose for Nova the Electron Sprite.

A modern flat-vector illustration of Nova, a friendly pedagogical mascot
for a college-level semiconductor physics textbook. Nova is an
anthropomorphized electron — a round, smooth cyan-blue sphere (#0288d1)
with a soft outer glow halo. A faint "−" minus-charge symbol marks the
body. Nova has small, expressive cartoon arms and hands extending from
the sphere. Big friendly cartoon eyes, no outlined facial features,
playful smile. Bright orange (#ff9800) is used sparingly for small energy
sparks. Style: modern flat vector, clean bold fills, soft radial glow
halo, no gradients beyond the glow. No text, no watermark.

Pose: Nova gives a confident thumbs-up with one hand, with a reassuring,
supportive smile and a slight head tilt. The pose radiates "you can do
it" energy. Small orange sparks shimmer around the thumbs-up hand.

Filename: encouraging.png

Please generate a new PNG image now with a fully transparent background.
The background MUST be fully transparent. DO NOT use a white, black, or
checkered background.
```

---

## 7. Celebration Pose — `celebration.png`

```
Please generate a new celebration pose for Nova the Electron Sprite.

A modern flat-vector illustration of Nova, a friendly pedagogical mascot
for a college-level semiconductor physics textbook. Nova is an
anthropomorphized electron — a round, smooth cyan-blue sphere (#0288d1)
with a soft outer glow halo. A faint "−" minus-charge symbol marks the
body. Nova has small, expressive cartoon arms and hands extending from
the sphere. Big friendly cartoon eyes, no outlined facial features,
playful smile. Bright orange (#ff9800) is used sparingly for small energy
sparks. Style: modern flat vector, clean bold fills, soft radial glow
halo, no gradients beyond the glow. No text, no watermark.

Pose: Nova jumps upward with both arms raised in celebration, eyes
squinted in a wide joyful smile. The outer glow halo is noticeably
brighter and larger than in the other poses — Nova has "leapt to a higher
energy level." Small orange and pale-yellow sparks, confetti-like
particles, and a few small lightning bolts radiate outward from Nova.

Filename: celebration.png

Please generate a new PNG image now with a fully transparent background.
The background MUST be fully transparent. DO NOT use a white, black, or
checkered background.
```
