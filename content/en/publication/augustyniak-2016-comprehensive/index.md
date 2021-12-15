---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Comprehensive study on lexicon-based ensemble classification sentiment analysis
subtitle: ""
summary: ""
authors:
  - augustyniak
  - szymanski
  - kajdanowicz
  - Wlodzimierz Tuliglowicz
tags:
  - "Ensemble Classification"
  - "Machine Learning"
  - "Opinion Mining"
  - "Sentiment Analysis"
  - "Sentiment Lexicon Generation"
  - "Ensemble"
  - "Lexicons"
  - "Supervised Learning"
categories: []
date: "2016-01-01"
lastmod: 2020-12-05T18:11:43+01:00
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
publishDate: "2020-12-05T17:11:42.353102Z"
publication_types:
  - "2"
abstract:
  We propose a novel method for counting sentiment orientation that outperforms
  supervised learning approaches in time and memory complexity and is not statistically
  significantly different from them in accuracy. Our method consists of a novel approach
  to generating unigram, bigram and trigram lexicons. The proposed method, called
  frequentiment, is based on calculating the frequency of features (words) in the
  document and averaging their impact on the sentiment score as opposed to documents
  that do not contain these features. Afterwards, we use ensemble classification to
  improve the overall accuracy of the method. What is important is that the frequentiment-based
  lexicons with sentiment threshold selection outperform other popular lexicons and
  some supervised learners, while being 3-5 times faster than the supervised approach.
  We compare 37 methods (lexicons, ensembles with lexicon's predictions as input and
  supervised learners) applied to 10 Amazon review data sets and provide the first
  statistical comparison of the sentiment annotation methods that include ensemble
  approaches. It is one of the most comprehensive comparisons of domain sentiment
  analysis in the literature.
publication: "*Entropy*"
url_pdf: http://www.mdpi.com/1099-4300/18/1/4
doi: 10.3390/e18010004
---
