---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Gender recognition using neural networks and ASR techniques
subtitle: ''
summary: ''
authors:
- Jerzy Sas
- Aleksander Sas
tags: []
categories: []
date: 2013-01-01
lastmod: 2022-01-12T14:27:10+01:00
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
publishDate: '2022-01-12T13:27:10.429239Z'
publication_types:
- '2'
abstract: The paper presents the simple technique of speaker gender recognition that
  uses MFCC features typically applied in automatic speech recognition. Artificial
  neural network is used as a classifier. The speech signal is first divided into
  20 ms frames. For each frame, Mel-Frequency Cepstral Coefficients are extracted
  and the created feature vector is provided into a neural network classifier, which
  individually classifies each frame as male or female sample. Finally, the whole
  utterance is classified by selecting the class, for which the sum of
publication: '*Journal of Medical Informatics & Technologies*'
---
