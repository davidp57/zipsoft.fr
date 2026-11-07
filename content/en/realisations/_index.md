---
title: "Projects"
# A data folder, not a page: the home page shows these cards (layouts/home.html).
# Neither the section nor the cards are built; the old /en/projects/ URL redirects to the home page.
build:
  render: never
  list: never
cascade:
  - target:
      kind: page
    build:
      render: never
      list: always
---
