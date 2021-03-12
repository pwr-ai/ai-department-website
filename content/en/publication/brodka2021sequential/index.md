---
title: "Sequential seeding in multilayer networks"
authors:
- brodka
- Jaroslaw Jankowski
- michalski
date: "2021-03-10T00:00:00Z"
doi: "https://doi.org/10.1063/5.0023427"

# Schedule page publish date (NOT publication's date).
publishDate: "2021-03-10T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "*Chaos: An Interdisciplinary Journal of Nonlinear Science, 31, 033130*"
publication_short: "*Chaos, 31, 033130*"

abstract: Multilayer networks are the underlying structures of multiple real-world systems where we have more than one type of interaction/relation between nodes: social, biological, computer, or communication, to name only a few. In many cases, they are helpful in modeling processes that happen on top of them, which leads to gaining more knowledge about these phenomena. One example of such a process is the spread of influence. Here, the members of a social system spread the influence across the network by contacting each other, sharing opinions or ideas, or—explicitly—by persuasion. Due to the importance of this process, researchers investigate which members of a social network should be chosen as initiators of influence spread to maximize the effect. In this work, we follow this direction and develop and evaluate the sequential seeding technique for multilayer networks. Until now, such techniques were evaluated only using simple one layer networks. The results show that sequential seeding in multilayer networks outperforms the traditional approach by increasing the coverage and allowing to save the seeding budget. However, it also extends the duration of the spreading process.
Sequential seeding is a node activation strategy for influence spreading, which distributes activations over time instead of performing all of them at once. It proved its superiority in a majority of seeding scenarios. However, the research until now was limited to simple one layer static networks reflecting only one type of relation. In this paper, we address that gap by extending sequential seeding to a multilayer network scenario. We have performed an extensive evaluation using four real networks and six synthetic (three random networks and three multilayer networks) of various sizes and with a various number of layers. Our results show that sequential seeding outperforms the traditional approach by increasing the coverage and increasing the duration of spread, confirming findings from previous research for one layer networks. What is more, we have evaluated additional aspects of sequential seeding, namely, the savings in the seeding budget. This aspect has not been evaluated in previous research. The findings presented in this work allow redesigning influence spreading strategies to increase the coverage with limited seeding budget, allowing for more effective spreading in multilayer networks.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags:
- Networ Science
- Multilayer Networks
- Spreading Processes
- Sequential Seading
featured: true

links:
- name: Paper website
url: https://aip.scitation.org/doi/full/10.1063/5.0023427
url_pdf: https://aip.scitation.org/doi/pdf/10.1063/5.0023427
url_code_GitHub: https://github.com/pbrodka/SQ4MLN
url_code_CodeOcean https://codeocean.com/capsule/3751385/tree/v1
url_dataset: https://github.com/pbrodka/SQ4MLN
url_arxiv: https://arxiv.org/abs/2009.05335
#url_poster: https://github.com/kacperkan/ucsgnet/raw/master/docs/poster.pdf
#url_project: https://kacperkan.github.io/ucsgnet/
# url_slides: ''
# url_source: '#'
#url_video: https://www.youtube.com/watch?v=s1p4UHtUG3g 

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: ''
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: [2017_brodka_multispread] 
 

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---

