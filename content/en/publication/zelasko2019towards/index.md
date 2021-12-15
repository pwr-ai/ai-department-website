---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Towards better understanding of spontaneous conversations: Overcoming automatic
  speech recognition errors with intent recognition'
subtitle: ''
summary: ''
authors:
- Piotr Zelasko
- Mikołaj Morzy
- szymański
- Jan Mizgajski
- Adrian Szymczak
- augustyniak
- Yishay Carmiel
tags: []
categories: []
date: '2019-01-01'
lastmod: 2020-12-05T18:11:46+01:00
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
publishDate: '2020-12-05T17:11:45.061263Z'
publication_types:
- '0'
abstract: In this paper we present a method for correcting automatic speech recognition
  (ASR) errors using a finite state transducer (FST) intent recognition framework.
  Intent recognition is a powerful technique for dialog flow management in turn-oriented,
  human-machine dialogs. This technique can also be very useful in the context of
  human-human dialogs, though it serves a different purpose of key insight extraction
  from conversations. We argue that currently available intent recognition techniques
  are not applicable to human-human dialogs due to the complex structure of turn-taking
  and various disfluencies encountered in spontaneous conversations, exacerbated by
  speech recognition errors and scarcity of domain-specific labeled data. Without
  efficient key insight extraction techniques, raw human-human dialog transcripts
  remain significantly unexploited. Our contribution consists of a novel FST for intent
  indexing and an algorithm for fuzzy intent search over the lattice - a compact graph
  encoding of ASR's hypotheses. We also develop a pruning strategy to constrain the
  fuzziness of the FST index search. Extracted intents represent linguistic domain
  knowledge and help us improve (rescore) the original transcript. We compare our
  method with a baseline, which uses only the most likely transcript hypothesis (best
  path), and find an increase in the total number of recognized intents by 25.1%.
publication: '*arXiv*'
url_pdf: https://arxiv.org/pdf/1908.07888
---
