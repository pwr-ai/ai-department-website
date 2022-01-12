---
# Documentation: https://wowchemy.com/docs/managing-content/

title: The influence of fitness caching on modern evolutionary methods and fair computation
  load measurement
subtitle: ''
summary: ''
authors:
- Michal W Przewozniczek
- Marcin M Komarnicki
tags: []
categories: []
date: 2018-01-01
lastmod: 2022-01-12T14:28:52+01:00
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
publishDate: '2022-01-12T13:28:51.978012Z'
publication_types:
- '1'
abstract: Any evolutionary method may store the fitness values for the genotypes it
  has already rated. Any time the fitness is to be computed, the check may be made
  if the fitness for the same genotype was not computed earlier. If so, then instead
  of re-evaluating the same genotype, the stored value from the repository may be
  returned. Such technique will be denoted as fitness caching. It is easy to implement
  in any evolutionary method, and it minimizes the number of fitness function evaluations
  (FFE), which is desirable. Despite its simplicity fitness
publication: '*Proceedings of the Genetic and Evolutionary Computation Conference
  Companion*'
---
