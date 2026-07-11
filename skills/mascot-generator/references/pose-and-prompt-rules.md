# Pose And Prompt Rules

## Canonical Pose Set

| Pose | Filename | Use | Required Gesture |
| --- | --- | --- | --- |
| Neutral | `neutral.png` | General-purpose notes and sidebars | relaxed, facing viewer |
| Welcome | `welcome.png` | Chapter openings | wave or inviting gesture |
| Tip | `tip.png` | hints and practical guidance | raised finger, pointer-like gesture, or equivalent |
| Thinking | `thinking.png` | key concepts and reflection | thoughtful pose, eyes slightly upward or focused |
| Encouraging | `encouraging.png` | difficult material | supportive thumbs-up, open-palmed encouragement, or equivalent |
| Warning | `warning.png` | pitfalls and common mistakes | gentle pause/check gesture, concerned but not frightened |
| Celebration | `celebration.png` | achievements and completion | arms/wings/features raised, restrained confetti optional |

Use these filenames exactly. The gallery convention orders cards as neutral, welcome, tip, thinking, encouraging, warning, celebration.

## Prompt Requirements

Every pose prompt must include:

- use case: pedagogical mascot pose for an interactive textbook
- character identity and role
- exact visual base description from the character sheet
- art style, composition, no-text rule, and background rule
- one pose-specific gesture/expression
- forbidden props, extra characters, watermarks, speech bubbles, and text

Keep the character full body, centered, and icon-friendly. Avoid detailed scenic backgrounds; mascot assets must work as small admonition images.

## Character Sheet Image

Generate `character-sheet.png` as a clean character reference sheet. It should show one large neutral full-body view plus smaller callouts or pose thumbnails when possible. It may contain labels only if the user wants a labeled reference; otherwise avoid text to keep image generation reliable.

## Common Failure Checks

- Same character across all seven images.
- No accidental clothing/accessory drift across poses.
- No extra mascot, duplicate limbs, cropped feet, or hidden hands.
- No background shadows or textured floor when transparency/chroma key is required.
- No green in the character when using `#00FF00`.
- The warning pose looks careful and instructional, not scary.
- The celebration pose is joyful but not visually cluttered.
