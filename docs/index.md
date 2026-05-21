---
title: "Book Mascots"
description: "A gallery of sample book mascots designed for reuse in new textbooks based on prior designs."
image: img/cover.png
og:image: img/cover.png
---
# Intelligent Textbook Mascots

This git repository contains a database of reusable mascot characters used across 
intelligent textbook projects.  This repository is designed to be used with an AI Skill
to help you select an existing mascot design to match to your textbook or
to quickly create variations of existing designs using a token-efficient process.
This process can be done even if you do not have an API key to an image
generation LLM.  This process enlarges the number of users (teachers) that can use
textbook generators that include mascots
in their books without the need for "expensive" image generation tools.
It also has skills that can generate new mascots using a high-quality image prompts.
In this case "expensive" would be around $3 USD per textbook for using an image
generation API.  This adds up when teachers need to generate many textbooks.

## Mascot Image Structure

The intelligent textbooks skill libraries use mascot images placed in the directory `PROJECT/img/mascot'

Each mascot has a set of at least seven poses:

1. neutral.png
2. welcome.png
3. tip.png
4. thinking.png
5. encouraging.png
6. warning.png
7. celebration.png

All images MUST be PNG files with transparent backgrounds (alpha channel).

We provide installation scripts to install the mascot images. There is a linux version
that runs on any Mac, Linux, or Windows System for Linus (WSL) or Windows PowerShell
version that runs on some Windows systems.  You must have permissions to run these
installation scripts.

## Integrations with Intelligent Book Skills

Our chapter content generator skill looks for a document called a "character-sheet.md"
that will provide guidance on how the  mascot can be
used to add personality and visual cues throughout a book.  

If you do not have a tool that
generates images (text to image generator) we encourage you to reuse these mascots for your
textbook.  They are Licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](license.md).  They are free to use in your classrooms but
you cannot resell them for commercial purposes.

## Ways to View The Mascots

We provide three ways to view the mascots:

1. [Browse the mascot gallery →](list-mascots.md) - this is just an alphabetical listing of all the mascots.
2. [Listing by Animal/Robot Name (species directory)](./mascot-species-directory.md)
3. [Similarity Map](./mascot-similarity.md) - 2D map of icons grouped by similarity - note the load times are sometimes longer for this view

## Installation

[Installation](./install-mascot.md)


