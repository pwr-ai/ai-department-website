---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Heterogeneous named entity similarity function
subtitle: ''
summary: ''
authors:
- Jan Koco\ŉ
- piasecki
tags: []
categories: []
date: 2012-01-01
lastmod: 2022-01-12T14:26:32+01:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-01-12T13:26:32.127380Z'
publication_types:
- '1'
abstract: Many text processing tasks require to recognize and classify Named Entities.
  Currently available morphological analysers for Polish cannot handle unknown words
  (not included in analyser's lexicon). Polish is a language with rich inflection,
  so comparing two words (even having the same lemma) is a non-trivial task. The aim
  of the similarity function is to match unknown word form with its word form in named-entity
  dictionary. In this article a complex similarity function is presented. It is based
  on a decision function implemented as a Logistic
publication: '*International Conference on Text, Speech and Dialogue*'
---
