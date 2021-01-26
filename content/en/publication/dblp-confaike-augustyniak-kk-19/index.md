---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Aspect Detection using Word and Char Embeddings with (Bi) LSTM and CRF
subtitle: ''
summary: ''
authors:
  - augustyniak
  - kajdanowicz
  - kazienko
tags: []
categories: []
date: '2019-01-01'
lastmod: 2020-12-05T18:11:47+01:00
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
publishDate: '2020-12-05T17:11:46.376704Z'
publication_types:
- '1'
abstract: 'We proposed a new accurate aspect extraction method that makes use of both word and character-based embeddings. We have conducted experiments of various models of aspect extraction using LSTM and BiLSTM including CRF enhancement on five different pre-trained word embeddings extended with character embeddings. The results revealed that BiLSTM outperforms regular LSTM, but also word embedding coverage in train and test sets profoundly impacted aspect detection performance. Moreover, the additional CRF layer consistently improves the results across different models and text embeddings. Summing up, we obtained state-of-the-art F-score results for SemEval Restaurants (85%) and Laptops (80%).'
publication: '*2nd IEEE International Conference on Artificial Intelligence and Knowledge
  Engineering, AIKE 2019, Sardinia, Italy, June 3-5, 2019*'
url_pdf: https://arxiv.org/pdf/1909.01276
doi: 10.1109/AIKE.2019.00016
---
