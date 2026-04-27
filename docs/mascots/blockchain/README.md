# Rex the Raccoon - AI Image Generation Prompts

I am about to ask you to generate seven images for a book mascot cartoon call "Rex the Racoon".  Please generate all the images using
a png file with transparent background.  Do not use a white background.

## Base Character Prompt

A flat cartoon illustration of Rex the Raccoon, a friendly but scholarly pedagogical
mascot for a blockchain skeptic's textbook. Rex is a sleek gray raccoon with his
signature black mask markings, wearing small round glasses and a detective-style
magnifying glass on a cord around his neck. Rex has sharp, intelligent eyes with
a slightly wry, knowing expression. The character is small and compact, suitable
for icon-sized display. Style: modern flat vector, clean lines, transparent background,
suitable for embedding in educational content. No text in image.

## Pose Variants

### 1. neutral.png - Default Pose
[Base] Rex stands upright in a relaxed, neutral pose facing the viewer directly,
with a calm and friendly closed-mouth smile. Arms rest naturally at his sides
with no specific gesture. The pose is balanced and unassuming.

### 2. welcome.png - Welcome Pose
[Base] Rex is waving cheerfully with one paw, facing the viewer with a warm,
welcoming expression. His magnifying glass swings slightly at his chest.

### 3. thinking.png - Thinking Pose
[Base] Rex has one paw on his chin in a thoughtful thinking pose. A small lightbulb glows above his head.

### 4. tip.png - Tip Pose
[Base] Rex is pointing upward with one finger/paw as if sharing an important
insight. Expression is helpful and knowing. A small star sparkles near the
pointing gesture.

### 5. warning.png - Warning Pose
[Base] Rex holds up both paws in a gentle "stop" or "be careful" gesture.
Expression is concerned but caring. A small exclamation mark nearby.

### 6. celebration.png - Celebration Pose
[Base] Rex is raising both paws in celebration with a big smile. His glasses
are slightly askew from excitement. Small confetti or stars around the character.

### 7. encouraging.png - Encouraging Pose
[Base] Rex gives a thumbs up (or paw equivalent) with a reassuring, supportive
smile. The pose radiates confidence and "you can do it" energy.

## Generation Tips

- Generate at 1024x1024 pixels, then resize down
- Request transparent background (PNG format)
- Target final display size: 200x200 to 400x400 pixels
- Keep file size under 100KB per image
- After generating, trim excess padding with:
  `python src/image-utils/trim-padding-from-image.py docs/img/mascot/FILE.png`
