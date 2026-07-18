---
title: Mascot Similarity Map
description: A 2D display of all the mascot icons.  You can zoom and pan and click on any mascot to find out more.
hide:
  toc
---
# Mascot Similarity Map

This page projects every mascot's neutral pose into a 2D layout using
**visual similarity** — mascots that look alike (color palette, art
style, species silhouette) cluster near each other. The embedding is
computed with [OpenAI CLIP](https://openai.com/research/clip) (image
side, ViT-B/32), and the 2D layout is produced by
[UMAP](https://umap-learn.readthedocs.io/) over the 512-dimensional
CLIP space. A textual-similarity view based on the prompt descriptions
(rather than the images) is a planned follow-up.

Hover any mascot for its name and textbook title; click any mascot to
open its full page. Use the Plotly toolbar in the top-right to pan,
zoom, or reset the view.

<div id="map" style="width: 100%; height: 80vh; min-height: 600px; border: solid blue 2px; background: aliceblue"></div>

<script>
(() => {
  // The page lives at /<base>/mascot-similarity/ (mkdocs default
  // use_directory_urls=true), so all data + image paths need a "../"
  // prefix to escape the page's own directory.
  const plotlyUrl = "https://cdn.plot.ly/plotly-basic-2.35.2.min.js";

  function loadPlotly() {
    if (window.Plotly) return Promise.resolve(window.Plotly);

    return new Promise((resolve, reject) => {
      let script = document.getElementById("plotly-basic-script");
      const isNewScript = !script;
      if (!script) {
        script = document.createElement("script");
        script.id = "plotly-basic-script";
        script.src = plotlyUrl;
      }
      script.addEventListener("load", () => resolve(window.Plotly), { once: true });
      script.addEventListener(
        "error",
        () => reject(new Error("Could not load Plotly from " + plotlyUrl)),
        { once: true },
      );
      if (isNewScript) document.head.appendChild(script);
    });
  }

  Promise.all([
    loadPlotly(),
    fetch("../data/mascot-embeddings.json").then(r => {
      if (!r.ok) throw new Error(`Could not load mascot data (${r.status})`);
      return r.json();
    }),
  ])
    .then(([Plotly, data]) => renderMap(Plotly, data))
    .catch(e => {
      document.getElementById("map").textContent =
        "Could not load the mascot similarity map. Please try again.";
      console.error(e);
    });

  function renderMap(Plotly, data) {
    const pts = data.points;
    const trace = {
      x: pts.map(p => p.x),
      y: pts.map(p => p.y),
      mode: "markers",
      type: "scatter",
      marker: { size: 60, opacity: 0 },
      customdata: pts.map(p => [p.slug, p.name, p.title]),
      hovertemplate:
        "<b>%{customdata[1]}</b><br>%{customdata[2]}<extra></extra>",
    };
    const layout = {
      images: pts.map(p => ({
        source: "../" + p.neutral,
        x: p.x, y: p.y,
        sizex: 50, sizey: 50,
        xanchor: "center", yanchor: "middle",
        xref: "x", yref: "y",
        layer: "below",
      })),
      xaxis: {
        visible: false,
        range: [0, data.viewport[0]],
        scaleanchor: "y",
      },
      yaxis: {
        visible: false,
        range: [0, data.viewport[1]],
      },
      title: {
        text: "Mascot Similarity",
        x: 0.5,
        xanchor: "center",
        font: { color: "black", size: 22 },
      },
      hovermode: "closest",
      margin: { l: 20, r: 20, t: 60, b: 20 },
      dragmode: "pan",
      plot_bgcolor: "aliceblue",
      paper_bgcolor: "rgba(0,0,0,0)",
    };
    Plotly.newPlot("map", [trace], layout, {
      responsive: true,
      displaylogo: false,
      modeBarButtonsToRemove: ["lasso2d", "select2d", "autoScale2d"],
    });
    document.getElementById("map").on("plotly_click", (e) => {
      const slug = e.points[0].customdata[0];
      window.location.href = `../mascots/${slug}/`;
    });
  }
})();
</script>
