# About Book Mascots

This site collects pedagogical mascots used across a family of intelligent textbooks. Each mascot is a small cartoon character with a fixed visual identity and a set of standard "poses" — neutral, welcome, thinking, tip, encouraging, warning, celebration — that authors drop into chapters to add personality and to give students consistent visual cues.

## Why pedagogical mascots matter

A mascot is not decoration. When used well, it does real instructional work.

- **Reduced cognitive load.** A recurring character is a known visual landmark. When a student sees Olli the Octopus mid-chapter, they don't have to spend attention parsing a new illustration — they know who this is, and they know what kind of moment it signals.
- **Tone shift without prose.** A "warning" pose communicates *be careful here* faster and more gently than a paragraph of italicized prose. A "celebration" pose at the end of a chapter rewards completion in a way text alone can't.
- **Emotional pacing.** Long-form technical material is grueling. A friendly face every few pages keeps the reader's affect warm and signals that the author is on the student's side.
- **Identity for the book.** Sparkle the Unicorn, Bailey the Beaver, Axiom the Owl — these become the *face* of a textbook. Students remember the mascot long after they've forgotten a specific definition, and the mascot becomes the on-ramp back into the material.
- **Inclusivity and approachability.** A cartoon animal carries no gender, age, or cultural baggage in the way a human illustration does. It lowers the barrier for readers who don't see themselves in stock photography of "the typical student."
- **Consistency across surfaces.** The same mascot poses can appear in the textbook, the lecture slides, the quiz feedback, the chatbot avatar, and the social-media announcement. That continuity reinforces the book as a coherent product rather than a pile of files.

The poses themselves are a small visual vocabulary. Once a reader has learned that *thinking* means "pause and reflect" and *tip* means "here is a shortcut," every subsequent chapter inherits that vocabulary for free.

## How a book mascot is created

The workflow we use across these books is roughly:

1. **Pick a character concept.** Match the species, color palette, and props to the subject matter. *Bailey the Beaver* for ecology (a builder of habitats). *Sentinel the Fox* for cybersecurity ("trust, but verify"). *Delta* — a triangle robot — for calculus. The link between mascot and subject is part of what makes it memorable.
2. **Write a Character Sheet.** A short prose document — name, species, color hex codes, props, personality, "what the hands are doing," background rules. This is the source of truth that every pose prompt re-anchors to. Without it, drift across poses is guaranteed.
3. **Author seven pose prompts.** Each pose prompt embeds the full character sheet, then adds two or three sentences describing the pose-specific gesture (waving for *welcome*, hand-on-chin for *thinking*, etc.). Self-contained prompts matter — image generators do not reliably maintain character identity across a session.
4. **Generate, trim, save.** Run each prompt through an image generator (DALL-E, Midjourney, Imagen, Firefly), trim padding, save as a transparent PNG.
5. **Wire into the book.** Copy the PNGs into `docs/img/mascot/` and reference them from chapter markdown using a small shortcode or admonition pattern.

The expensive step is **#3 and #4**. Getting seven poses that look like the same character — same proportions, same eye color, same prop placement — typically takes many regenerations and several rounds of prompt tightening. This is where most of the cost lives.

## Token costs and image-generation costs

A complete mascot set has real cost behind it, and the cost is dominated by image generation rather than text tokens.

- **Character-bible drafting:** a few thousand input/output tokens. Trivial.
- **Pose prompt authoring:** seven self-contained prompts, each repeating the bible. Maybe 5–10K tokens of LLM work total.
- **Image generation:** seven poses × 3–10 regenerations each to lock in consistency. At commercial rates (a few cents to ~25¢ per image depending on the tool and tier), a finished mascot easily runs **$5–$30** in image-API spend, plus the human time to triage the bad outputs.
- **Touch-up:** background-trimming, centering, occasional manual edits in an image editor.

Across this site that is **20+ mascots × seven poses each = 140+ generated images**. The aggregate cost — in money, in API budget, and especially in iteration time — is non-trivial.

## Not every book needs a unique mascot

A counterintuitive lesson from running this experiment across a couple dozen books: **most books do not need their own mascot.** The marginal pedagogical value of "a brand-new character for *this* book" is usually small once a good general-purpose mascot exists. What students actually benefit from is the *consistency* of the pose vocabulary — neutral, welcome, thinking, tip — not the novelty of the species.

Good defaults:

- A **course series** (e.g. all your math books, or all your science books) can share one mascot. Continuity across volumes is a feature, not a bug.
- A book with a **strong subject-specific identity** — moss biology, ecology, cybersecurity — is a good candidate for a custom mascot, because the species/prop choice carries real meaning.
- A book in a generic domain — "Introduction to Programming," "Study Skills," a tutorial — is usually well served by an existing general-purpose mascot.

Treat custom mascots as a deliberate investment, not a default deliverable.

## Reuse: Claude Code, no image-LLM license required

This is the practical payoff of publishing the mascots here. **Once a mascot exists in this repo, anyone with a Claude Code license can reuse it without paying for a text-to-image model.**

Concretely, an author working in Claude Code can:

- Pull the seven PNGs for *Olli the Octopus* (or any mascot here) directly into their book's `docs/img/mascot/` directory.
- Wire them into chapter markdown the same way the source books do.
- Skip the entire image-generation pipeline — no Midjourney subscription, no OpenAI Images API key, no Firefly seat, no waiting on regenerations.

This matters for two reasons:

1. **Lower the barrier to making a textbook feel finished.** A first-time author working on a small intelligent textbook should not have to set up a second AI subscription just to get a friendly face into their chapters.
2. **Standardize the pose vocabulary.** When multiple books pull from the same mascot library, students who read more than one of them benefit from cross-book consistency in what *thinking* and *warning* and *celebration* look like.

The mascots in this repo are licensed for reuse across our intelligent-textbook projects. Pick one, copy the seven PNGs, and ship.

## What this site is

- A **gallery** ([Mascot Gallery](list-mascots.md)) of every mascot, showing the neutral pose and the character name.
- A **detail page per mascot** showing all seven poses side-by-side.
- The **original prompt files** (`image-prompts.md`) under each mascot directory, so you can regenerate, fork, or adapt a mascot for a related book.
- An **`update-mascots` skill** that scans sibling book projects and brings new mascots into this gallery automatically.

The goal is a small, reusable, low-friction set of pedagogical characters that any author in our orbit can lift wholesale and put to work.
