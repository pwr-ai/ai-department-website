---
# Documentation: https://wowchemy.com/docs/managing-content/

title:
  Comprehensive analysis of aspect term extraction methods using various text
  embeddings
subtitle: ""
summary: ""
authors:
  - augustyniak
  - kajdanowicz
  - kazienko
tags: []
categories: []
date: "2019-01-01"
lastmod: 2020-12-05T18:11:51+01:00
featured: true
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: "2020-12-05T17:11:50.083271Z"
publication_types:
  - "0"
abstract:
  Recently, a variety of model designs and methods have blossomed in the context
  of the sentiment analysis domain. However, there is still a lack of wide and comprehensive
  studies of aspect-based sentiment analysis (ABSA). We want to fill this gap and
  propose a comparison with ablation analysis of aspect term extraction using various
  text embedding methods. We particularly focused on architectures based on long short-term
  memory (LSTM) with optional conditional random field (CRF) enhancement using different
  pre-trained word embeddings. Moreover, we analyzed the influence on performance
  of extending the word vectorization step with character embedding. The experimental
  results on SemEval datasets revealed that not only does bi-directional long short-term
  memory (BiLSTM) outperform regular LSTM, but also word embedding coverage and its
  source highly affect aspect detection performance. An additional CRF layer consistently
  improves the results as well.
publication: "*arXiv*"
---
