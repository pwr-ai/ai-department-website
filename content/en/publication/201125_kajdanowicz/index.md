---
title: "UCSG-Net - Unsupervised Discovering of Constructive Solid Geometry Tree"
authors:
- Kacper Kania
- Maciej Zięba
- kajdanowicz
date: "2020-12-06T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2020-10-24T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *Advances in Neural Information Processing Systems (NeurIPS 2020)*
publication_short: In *NeurIPS*

abstract: Signed distance field (SDF) is a prominent implicit representation of 3D meshes. Methods that are based on such representation achieved state-of-the-art 3D shape reconstruction quality. However, these methods struggle to reconstruct non-convex shapes. One remedy is to incorporate a constructive solid geometry framework (CSG) that represents a shape as a decomposition into primitives. It allows to embody a 3D shape of high complexity and non-convexity with a simple tree representation of Boolean operations. Nevertheless, existing approaches are supervised and require the entire CSG parse tree that is given upfront during the training process. On the contrary, we propose a model that extracts a CSG parse tree without any supervision - UCSG-Net. Our model predicts parameters of primitives and binarizes their SDF representation through differentiable indicator function. It is achieved jointly with discovering the structure of a Boolean operators tree. The model selects dynamically which operator combination over primitives leads to the reconstruction of high fidelity. We evaluate our method on 2D and 3D autoencoding tasks. We show that the predicted parse tree representation is interpretable and can be used in CAD software. 

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags:
- Deep Learning
- Representation Learning 
featured: true

links:
- name: NeurIPS Proceedings
  url: https://papers.nips.cc/paper/2020/hash/63d5fb54a858dd033fe90e6e4a74b0f0-Abstract.html
url_pdf: https://papers.nips.cc/paper/2020/file/63d5fb54a858dd033fe90e6e4a74b0f0-Paper.pdf
url_code: https://github.com/kacperkan/ucsgnet
url_dataset: https://github.com/kacperkan/ucsgnet/tree/master/data
url_poster: https://github.com/kacperkan/ucsgnet/raw/master/docs/poster.pdf
url_project: https://kacperkan.github.io/ucsgnet/
# url_slides: ''
# url_source: '#'
url_video: https://www.youtube.com/watch?v=s1p4UHtUG3g 

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Pixabay**](https://pixabay.com/photos/tree-nature-wood-kahl-log-tribe-3097419/)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: [2017_kajdanowicz_ncn_sonata] 
 

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---
{{< youtube s1p4UHtUG3g >}}
