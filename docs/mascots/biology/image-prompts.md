# Gregor the Tree Frog — AI Image Generation Prompts

Use these prompts to generate the seven mascot images with a consistent style.
Recommended tools: DALL-E 3 (ChatGPT), Midjourney, or Adobe Firefly.
Target resolution: **512×512 px** or **1024×1024 px**, then resize to 200×200 px for web.
Format: **PNG with transparent background**.

---

## Base Character Description

Copy this base into every prompt below:

```
Please generate a new png image based on the image above.  
The image has a frog in the center but it the background
is transparent.

A modern flat vector illustration of Gregor the Tree Frog, a friendly
pedagogical mascot for an college placement Biology high school textbook. Gregor is a
small, round-bodied tree frog with bright lime-green skin, large expressive
golden eyes with round pupils, and a cream-white underbelly. He wears a
tiny white lab coat and holds a small round magnifying glass. His expression
is curious and warm. The character is compact and icon-sized.
Style: modern flat vector, bold outlines, vibrant colors, on a
transparent background, no text in image, suitable for embedding in
educational web pages.  All parts of the body should be filled in with
non-transparent pixel values.  Use a minimum of padding around the body.
```

---

## Pose 0 — Neutral (neutral.png)

For general-purpose use, sidebars, introductions, or any context where
no specific pose is needed. This is the default reference pose.

```
[BASE] Gregor stands upright in a relaxed, neutral pose, facing the viewer
directly with a calm, friendly expression — a gentle closed-mouth smile. He
holds the magnifying glass loosely at his side with both front legs resting
naturally. No special gesture, no prop emphasis. The pose is balanced and
unassuming, suitable as a general-purpose illustration.
```

---

## Pose 1 — Welcome (welcome.png)

For chapter openings.

```
Please use the description above and make a new Welcome pose.

Generate a new png with a transparent background image of Gregor the frog giving a welcome.
Gregor is waving one front leg cheerfully at the viewer with a big,
warm smile. His other hand holds the magnifying glass at his side. The pose
radiates "welcome, let's get started!" energy. He faces slightly toward the
viewer with an open, inviting posture.
```

---

## Pose 2 — Thinking (thinking.png)

For key concepts and insights.

```
Please generate a new image.
This is an image of Gregor the frog above in a thinking pose.
Gregor rests one front leg against his chin in a classic thinking pose,
looking slightly upward. A small bright lightbulb glows above his head. His
golden eyes are wide with curiosity and discovery. The magnifying glass rests
at his side.  Fill in the body of the frog with non-transparent pixels.
```

---

## Pose 3 — Tip (tip.png)

For helpful hints and college placement exam strategies.

```
[BASE]

Create a new image for Gregor giving a tip.
Gregor holds up one front leg with the index finger pointing upward, as
if sharing an important tip. A small yellow star or sparkle appears near the
pointing gesture. His expression is knowing and helpful, with a slight smile.
Make sure that within the body of the frog there are NO transparent pixels.
```

---

## Pose 4 — Warning (warning.png)

For common mistakes and misconceptions to avoid.

```
Create a new image for Gregor giving a friendly warning.
Gregor holds up both front legs with open palms in a gentle "stop" or
"be careful" gesture. His golden eyes are wide with a concerned but caring
expression. A small red exclamation mark or caution triangle appears nearby.
Make sure that within the body of the frog there are NO transparent pixels.
All transparent pixels within the body should be white for Gregor's lab coat.
Convert all the transparent pixels in the lab coat to be a solid white.

```

---

## Pose 5 — Celebration (celebration.png)

For section completions and achievements.

```
Create a new image for Gregor doing a
Gregor leaps upward with both arms raised in joyful celebration, his
mouth open in a wide, happy smile. Small green and yellow confetti pieces and
tiny stars scatter around him. His eyes are squinted with joy.
```

---

## Pose 6 — Encouraging (encouraging.png)

For difficult content and moments where students may feel frustrated.

```
Generate a new png image of Gregor the frog on a transparent background.
This pose is for an encouraging gesture.
Gregor gives a confident thumbs-up with one front leg while smiling
warmly and reassuringly at the viewer. His posture is relaxed and supportive.
The pose radiates "you can do it" and "I believe in you" energy.
```

---

## Image Checklist

After generating all six images, verify:

- [ ] All images have a **transparent or white background**
- [ ] Consistent art style across all seven poses
- [ ] Gregor looks like the same character in each pose
- [ ] Lab coat and golden eyes are visible in each
- [ ] File names match exactly: `neutral.png`, `welcome.png`, `thinking.png`,
      `tip.png`, `warning.png`, `celebration.png`, `encouraging.png`
- [ ] Each file is **under 100KB** (resize/compress if needed)

Place all six images in: `docs/img/mascot/`
