---
hide:
  - navigation
  - toc
---

# Mascot Montage

<style>
  .montage {
    width: 100%;
    aspect-ratio: 16 / 9;
    background: linear-gradient(135deg, #4f5bd5 0%, #962fbf 50%, #d62976 100%);
    border-radius: 12px;
    padding: 1.5%;
    box-sizing: border-box;
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    grid-template-rows: 1fr 1fr 1fr;
    gap: 0.5%;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
    overflow: hidden;
  }
  .montage .cell {
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }
  .montage .cell img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.35));
    transition: transform 0.25s ease;
  }
  .montage .cell img:hover {
    transform: scale(1.08);
  }
  .montage .title {
    grid-column: 4 / span 2;
    grid-row: 2 / span 1;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: #ffffff;
    font-weight: 800;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: clamp(1.5rem, 4vw, 4rem);
    line-height: 1.05;
    letter-spacing: 0.02em;
    text-shadow: 0 4px 16px rgba(0, 0, 0, 0.5), 0 0 2px rgba(0, 0, 0, 0.4);
    padding: 0.5rem;
  }
</style>

<div class="montage">
  <!-- Row 1: 8 mascots -->
  <div class="cell"><img src="../mascots/bioinformatics/neutral.png" alt="Olli the Octopus"></div>
  <div class="cell"><img src="../mascots/biology/neutral.png" alt="Gregor the Tree Frog"></div>
  <div class="cell"><img src="../mascots/blockchain/neutral.png" alt="Rex the Raccoon"></div>
  <div class="cell"><img src="../mascots/calculus/neutral.png" alt="Delta the Slope-Walking Explorer"></div>
  <div class="cell"><img src="../mascots/circuits/neutral.png" alt="Sparky the Lightbulb"></div>
  <div class="cell"><img src="../mascots/cybersecurity/neutral.png" alt="Sentinel the Fox"></div>
  <div class="cell"><img src="../mascots/Dementia/neutral.png" alt="Tokie"></div>
  <div class="cell"><img src="../mascots/digital-citizenship/neutral.png" alt="Maka the River Otter"></div>

  <!-- Row 2: 3 mascots, title (spans 2), 3 mascots -->
  <div class="cell"><img src="../mascots/ecology/neutral.png" alt="Bailey the Beaver"></div>
  <div class="cell"><img src="../mascots/economics-course/neutral.png" alt="Ferris the Fox"></div>
  <div class="cell"><img src="../mascots/functions/neutral.png" alt="Rick the Raccoon"></div>

  <div class="title">Book<br>Mascots</div>

  <div class="cell"><img src="../mascots/genetics/neutral.png" alt="Dottie the Drosophila"></div>
  <div class="cell"><img src="../mascots/infographics/neutral.png" alt="Percy the Peacock"></div>
  <div class="cell"><img src="../mascots/intelligent-textbooks/axiom-neutral.png" alt="Axiom the Owl"></div>

  <!-- Row 3: 8 mascots -->
  <div class="cell"><img src="../mascots/learning-sciences/neutral.png" alt="Bloom the Elephant"></div>
  <div class="cell"><img src="../mascots/moss/neutral.png" alt="Mossby the Tree Frog"></div>
  <div class="cell"><img src="../mascots/pre-calc/neutral.png" alt="Prema"></div>
  <div class="cell"><img src="../mascots/quantum-computing/neutral.png" alt="Fermi the Ferret"></div>
  <div class="cell"><img src="../mascots/statistics-course/neutral.png" alt="Sylvia the Statistical Squirrel"></div>
  <div class="cell"><img src="../mascots/theory-of-knowledge/neutral.png" alt="Sofia the Owl"></div>
  <div class="cell"><img src="../mascots/token-efficiency/neutral.png" alt="Pemba the Red Panda"></div>
  <div class="cell"><img src="../mascots/unicorns/neutral.png" alt="Sparkle the Unicorn"></div>
</div>

A single wide-landscape composition of all 22 mascots from our intelligent textbook
collection, framed around the **Book Mascots** title. Suitable for use as a cover
image, banner, or social-media share card. To export, take a screenshot of the
montage area or open the page on a wide display and capture it at the desired
resolution.
