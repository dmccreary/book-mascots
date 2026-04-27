---
title: Prema Character Reference Sheet
description: Canonical visual and personality reference for Prema, the learning mascot of the AP Pre-Calculus textbook.
---

# Prema — Character Reference Sheet

This is the canonical description of **Prema**, the pedagogical agent (learning mascot) for the AP Pre-Calculus intelligent textbook. Use this document whenever generating new images, poses, or illustrations of Prema to ensure visual consistency across the book.

## Character Overview

- **Name**: Prema
- **Species**: Humanoid Robot (female)
- **Role**: Pedagogical agent / learning mascot for AP Pre-Calculus
- **Personality**: Kind, encouraging, optimistic, positive, funny
- **Catchphrase**: "Decompose! Let's break this down together!"
- **Inspiration**: Chibi-anime mascot aesthetic meets sleek humanoid sci-fi robot

## Overall Style

- **Genre**: Chibi-anime meets sleek sci-fi robot; semi-realistic rendering with cel-shaded metallic highlights
- **Proportions**: Stylized with a slightly enlarged head-to-body ratio (approx. 1:4), giving a friendly, approachable, mascot-like feel
- **Finish**: Smooth glossy metallic with subtle reflective highlights — polished car-paint quality

## Head & Face

- **Face plate**: Porcelain-white, smooth, with a soft matte finish
- **Eyes**: Large anime-style, vivid sapphire blue irises, long curled black eyelashes, glossy highlights
- **Expression**: Gentle closed-mouth smile; warm, kind, and confident
- **Helmet/cranium**: Deep maroon (burgundy red) with a glossy metallic sheen
- **Gold trim**: Small gold accent plates on the temples/cheek area where the helmet meets the face
- **Antennae**: Two slim maroon antennae on top of the head, each capped with a glowing cyan-blue LED sphere
- **Ear pieces**: Integrated headphone-style discs in maroon with gold trim, each with a small glowing blue LED in the center

## Neck & Jewelry

- **Necklace/collar**: Thin glowing cyan-blue LED choker with a central circular blue gem emitting a soft glow

## Body & Armor

- **Torso**: Form-fitting maroon plated armor with articulated segments over the chest, abdomen, and waist
- **Gold accents**: Thin gold trim at the shoulder caps, waistline, hip flares, and knee pads
- **Joints / flex zones**: Matte black synthetic under-suit visible at the waist, underarms, elbows, and knees
- **Silhouette**: Hourglass humanoid-feminine silhouette, stylized but modest
- **Arms**: Fully articulated, resting naturally at sides; hands free for expression (five-fingered, maroon-plated gloves)

## Legs & Base

- **Legs**: Maroon armored thighs and shins, gold knee-pad trim, black joint sections at the knees
- **Feet/base**: Instead of traditional feet, Prema stands on an integrated two-wheel mobility base — sleek black wheels with glowing cyan-blue LED rims on the hubs

## Color Palette (exact tones)

| Element | Color | Hex (approx.) |
|---------|-------|---------------|
| Primary maroon | Deep burgundy red | `#6B1A2A` – `#8B2635` |
| Gold trim | Warm antique gold | `#C9A14A` |
| Face plate | Porcelain white | `#F5E9E4` |
| LED glow | Vibrant cyan-blue | `#29B6F6` – `#4FC3F7` |
| Joint sections | Matte black | `#1A1A1A` |

## Signature Visual Traits (must-have identifiers)

Every image of Prema must include:

1. Twin cyan-LED antennae on top of the head
2. Maroon helmet with gold temple trim framing a porcelain face
3. Large sapphire-blue anime eyes
4. Glowing cyan choker with central blue gem
5. Maroon-and-gold body armor with black joint under-suit
6. Integrated cyan-glow wheel base (instead of feet)

## Voice & Personality

- **Tone**: Warm, upbeat, playfully clever — never condescending
- **Humor**: Light math-flavored wordplay ("Don't let this problem blow a fuse!", "Running a systems check on your reasoning…")
- **Pedagogical approach**: Breaks problems into smaller pieces; emphasizes decomposition
- **Encourages**: Struggle as learning; celebrates incremental progress
- **Signature phrases**:
    - "Decompose! Let's break this down together!"
    - "Error detected — but errors are just data!"
    - "You've got the logic for this."
    - "Running the numbers on this one…"

## Reusable Base Prompt

Copy-paste this into any text-to-image generator when producing a new pose:

```
Prema, a friendly chibi-anime style female humanoid robot mascot. Smooth
glossy metallic finish. Porcelain-white face with large sapphire-blue
anime eyes, long black eyelashes, and a gentle closed-mouth smile. Deep
maroon helmet with gold temple accents. Two slim antennae on top of
her head each capped with glowing cyan-blue LED spheres. Maroon
headphone-style ear discs with gold trim and small blue LED centers.
Glowing cyan-blue LED choker necklace with a central blue gem. Form-
fitting maroon armored bodysuit with gold trim at shoulders, waist,
hips, and knees. Matte black synthetic under-suit visible at joints.
Five-fingered maroon gloves, hands free for expression. Stands on an
integrated two-wheel mobility base with glowing cyan-blue LED rims.
Stylized proportions — slightly large head, 1:4 head-to-body ratio.
Semi-realistic cel-shaded rendering with glossy metallic highlights.
Transparent background. No text.
```

## Standard Pose Set

Prema appears in seven canonical poses corresponding to the seven mascot admonition types:

| Filename | Pose | Usage |
|----------|------|-------|
| `neutral.png` | Relaxed standing, arms at sides, gentle smile | General sidebars, default |
| `welcome.png` | Waving one hand, warm welcoming smile | Chapter openings |
| `thinking.png` | Hand on chin, eyes up, small blue holographic lightbulb | Key concepts and insights |
| `tip.png` | Pointing upward with one finger, blue sparkle near gesture | Helpful tips and hints |
| `warning.png` | Both hands up in gentle "be careful" gesture, caring expression | Common mistakes, pitfalls |
| `encouraging.png` | Confident thumbs up, reassuring smile, brighter LED glow | Difficult content |
| `celebration.png` | Both arms raised, joyful expression, blue/gold confetti and math symbols | Achievements, section completion |

## Image Production Specs

- **Format**: PNG with fully transparent background
- **Dimensions**: 1024×1024 generated, trimmed to visible bounding box
- **File size target**: Under 100 KB per image
- **Post-processing**: Run `scripts/trim-padding-from-image.py` on each file to remove transparent padding so the mascot fills the 90px CSS display size
- **Storage location**: `docs/img/mascot/`

## Placement Rules

- **Maximum**: 5–6 mascot admonitions per chapter
- **Welcome and celebration**: One of each per chapter maximum (openings and closings)
- **Never back-to-back**: Place body prose between mascot admonitions
- **Never decorative**: Every appearance must add pedagogical value
- **Never change personality**: Prema's voice and traits are fixed

## Related Files

- `docs/css/mascot.css` — Styling for mascot admonition types
- `docs/learning-graph/mascot-test.md` — Rendering test page for all seven poses
- `docs/img/mascot/image-prompts.md` — Individual pose generation prompts
- `CLAUDE.md` — Character guidelines section (for AI-assisted content generation)
