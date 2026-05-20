# Image Prompts: Nexus the Spider

Self-contained AI image generation prompts for all seven poses. Each prompt
includes the full base character description so it can be used independently.
Generate at 512×512 or 1024×1024 pixels with a fully transparent background.

---

## Base Description (embedded in every prompt below)

A modern flat vector illustration of Nexus the Spider, a friendly pedagogical
mascot for a context graph and enterprise AI textbook. Nexus is a small,
round-bodied spider with a deep indigo/blue-purple body and warm orange accent
highlights. Nexus wears small round glasses. The character has a friendly,
curious expression. Small and compact, suitable for icon-sized display.
Style: modern flat vector, clean lines, transparent background, suitable for
embedding in educational content. No text in image.

---

## 1. Neutral Pose — `neutral.png`

Please generate a neutral pose for Nexus the Spider.

A modern flat vector illustration of Nexus the Spider, a friendly pedagogical
mascot for a context graph and enterprise AI textbook. Nexus is a small,
round-bodied spider with a deep indigo/blue-purple body and warm orange accent
highlights. Nexus wears small round glasses. The character has a friendly,
curious expression. Small and compact, suitable for icon-sized display.
Style: modern flat vector, clean lines, transparent background, suitable for
embedding in educational content. No text in image.

Nexus stands upright in a relaxed, neutral pose facing the viewer directly,
with a calm and friendly closed-mouth smile. All legs rest naturally at the
sides with no specific gesture. The pose is balanced and unassuming —
suitable as a general-purpose or default illustration.

Please generate a new png image now with a fully transparent background.
The background MUST be fully transparent. DO NOT use a white, black, or
checkered background.

---

## 2. Welcome Pose — `welcome.png`

Please generate a welcome pose for Nexus the Spider.

A modern flat vector illustration of Nexus the Spider, a friendly pedagogical
mascot for a context graph and enterprise AI textbook. Nexus is a small,
round-bodied spider with a deep indigo/blue-purple body and warm orange accent
highlights. Nexus wears small round glasses. The character has a friendly,
curious expression. Small and compact, suitable for icon-sized display.
Style: modern flat vector, clean lines, transparent background, suitable for
embedding in educational content. No text in image.

Nexus is waving cheerfully with one front leg/arm, facing the viewer with a
warm, welcoming expression. The pose suggests "welcome" and "let's get
started."

Please generate a new png image now with a fully transparent background.
The background MUST be fully transparent. DO NOT use a white, black, or
checkered background.

---

## 3. Thinking Pose — `thinking.png`

Please generate a thinking pose for Nexus the Spider.

A modern flat vector illustration of Nexus the Spider, a friendly pedagogical
mascot for a context graph and enterprise AI textbook. Nexus is a small,
round-bodied spider with a deep indigo/blue-purple body and warm orange accent
highlights. Nexus wears small round glasses. The character has a friendly,
curious expression. Small and compact, suitable for icon-sized display.
Style: modern flat vector, clean lines, transparent background, suitable for
embedding in educational content. No text in image.

Nexus has one front leg raised to chin in a thoughtful pose, with a small
lightbulb or thought bubble above the head. The pose suggests deep thinking
and discovery.

Please generate a new png image now with a fully transparent background.
The background MUST be fully transparent. DO NOT use a white, black, or
checkered background.

---

## 4. Tip Pose — `tip.png`

Please generate a tip pose for Nexus the Spider.

A modern flat vector illustration of Nexus the Spider, a friendly pedagogical
mascot for a context graph and enterprise AI textbook. Nexus is a small,
round-bodied spider with a deep indigo/blue-purple body and warm orange accent
highlights. Nexus wears small round glasses. The character has a friendly,
curious expression. Small and compact, suitable for icon-sized display.
Style: modern flat vector, clean lines, transparent background, suitable for
embedding in educational content. No text in image.

Nexus is pointing upward with one front leg as if sharing an important tip.
Expression is helpful and knowing. A small orange star or sparkle near the
pointing gesture.

Please generate a new png image now with a fully transparent background.
The background MUST be fully transparent. DO NOT use a white, black, or
checkered background.

---

## 5. Warning Pose — `warning.png`

Please generate a friendly warning pose for Nexus the Spider.

A modern flat vector illustration of Nexus the Spider, a friendly pedagogical
mascot for a context graph and enterprise AI textbook. Nexus is a small,
round-bodied spider with a deep indigo/blue-purple body and warm orange accent
highlights. Nexus wears small round glasses. The character has a friendly,
curious expression. Small and compact, suitable for icon-sized display.
Style: modern flat vector, clean lines, transparent background, suitable for
embedding in educational content. No text in image.

Nexus holds up two front legs in a gentle "stop" or "be careful" gesture.
Expression is concerned but caring. A small exclamation mark or caution
symbol nearby.

Please generate a new png image now with a fully transparent background.
The background MUST be fully transparent. DO NOT use a white, black, or
checkered background.

---

## 6. Encouraging Pose — `encouraging.png`

Please generate an encouraging pose for Nexus the Spider.

A modern flat vector illustration of Nexus the Spider, a friendly pedagogical
mascot for a context graph and enterprise AI textbook. Nexus is a small,
round-bodied spider with a deep indigo/blue-purple body and warm orange accent
highlights. Nexus wears small round glasses. The character has a friendly,
curious expression. Small and compact, suitable for icon-sized display.
Style: modern flat vector, clean lines, transparent background, suitable for
embedding in educational content. No text in image.

Nexus gives a thumbs-up (or equivalent raised-leg gesture) with a warm,
reassuring smile. The pose radiates confidence and "you can do it" energy.

Please generate a new png image now with a fully transparent background.
The background MUST be fully transparent. DO NOT use a white, black, or
checkered background.

---

## 7. Celebration Pose — `celebration.png`

Please generate a celebration pose for Nexus the Spider.

A modern flat vector illustration of Nexus the Spider, a friendly pedagogical
mascot for a context graph and enterprise AI textbook. Nexus is a small,
round-bodied spider with a deep indigo/blue-purple body and warm orange accent
highlights. Nexus wears small round glasses. The character has a friendly,
curious expression. Small and compact, suitable for icon-sized display.
Style: modern flat vector, clean lines, transparent background, suitable for
embedding in educational content. No text in image.

Nexus raises multiple legs/arms in celebration. Expression is joyful and
proud. Small orange and indigo confetti or stars surround the character.

Please generate a new png image now with a fully transparent background.
The background MUST be fully transparent. DO NOT use a white, black, or
checkered background.

---

## Usage Notes

- Generate at **512×512** or **1024×1024** pixels
- Background **must be fully transparent** (PNG format)
- After generating, run the padding trimmer to remove excess empty space:

```bash
python ../../../scripts/trim-padding-from-image.py docs/img/mascot/neutral.png
python ../../../scripts/trim-padding-from-image.py docs/img/mascot/welcome.png
python ../../../scripts/trim-padding-from-image.py docs/img/mascot/thinking.png
python ../../../scripts/trim-padding-from-image.py docs/img/mascot/tip.png
python ../../../scripts/trim-padding-from-image.py docs/img/mascot/warning.png
python ../../../scripts/trim-padding-from-image.py docs/img/mascot/encouraging.png
python ../../../scripts/trim-padding-from-image.py docs/img/mascot/celebration.png
```
