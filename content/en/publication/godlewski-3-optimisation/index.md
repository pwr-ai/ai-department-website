---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Optimisation of Polish tagger parameters
subtitle: ''
summary: ''
authors:
- Grzegorz Godlewski
- Maciej Piasecki
tags: []
categories: []
date: 2022-01-01
lastmod: 2022-01-12T14:28:55+01:00
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
publishDate: '2022-01-12T13:28:55.066853Z'
publication_types:
- '2'
abstract: The large tagset of the IPI PAN Corpus of Polish enforced a modular architecture
  of the Polish tagger called TaKIPI. The architecture introduce several parameters,
  for learning and tagging, that are difficult to be properly adjusted manually. In
  this paper a method of optimisation of the parameters values based on Genetic Algorithm
  is presented. A chromosome is a set of values, a specimen is a tagger together with
  the learning process, and the fitness function is a test of the tagger's accuracy.
  The optimisation process is
publication: '*Proceedings of Artificial Intelligence Studies*'
---
