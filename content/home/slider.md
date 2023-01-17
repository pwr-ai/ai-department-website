---
widget: slider
weight: 1
active: true
headless: true

design:
  # Slide height is automatic unless you force a specific height (e.g. '400px')
  slide_height: ''
  is_fullscreen: true
  # Automatically transition through slides?
  loop: true
  # Duration of transition between slides (in ms)
  interval: 4000

content:
  slides:
    - title: "Welcome!"
      content: "We are the Department of Artificial Intelligence at Wroclaw University of Science and Technology, founded in 2014 (formerly a Department of Computational Intelligence). Our team researches important data science, machine learning and general artificial intelligence problems involving unstructured data: in other words, images, texts, sounds, networks or signals."
      align: center
      background:
        position: right
        color: '#666'
        brightness: 0.7
        media: neurips.jpg
    - title: Study Artificial Intelligence @ WrUST
      content: There's no AI without an I, apply now!
      align: center
      background:
        position: right
        color: '#666'
        brightness: 0.7
        media: coders.jpg
      link:
        icon: graduation-cap
        icon_pack: fas
        text: Show more
        url: https://studiuj.ai
    - title: Interested in working with us?
      content: 'If you’re interested in joining our group, send an email with your interests and CV to ai@pwr.edu.pl'
      align: right
      background:
        position: center
        color: '#333'
        brightness: 0.5
        media: office_black.jpg
---
