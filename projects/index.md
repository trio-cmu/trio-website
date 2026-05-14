---
title: Projects
nav:
  order: 2
  tooltip: Software, datasets, and more
---

# {% include icon.html icon="fa-solid fa-wrench" %}Projects and Open Positions

You can find below an overview of ongoing and past projects from the TRIO Lab at Carnegie Mellon University and from prior appointments at Inria, University of Toronto, and EPFL.

## Open Positions

We are always looking for Master's and Undergraduate students to join our lab!  
Interested in collaborating or joining? [Get in touch](/contact/) and let us know which of the below projects you are interested in!

{% include tags.html tags="robotics, optimization, intelligence, software" %}

{% include search-info.html %}

{% include section.html %}

## Featured

<div class="grid" data-style="featured">
{% include list.html component="card" data="projects" filter="featured == true" style="grid" %}
</div>

{% include section.html %}

{% assign other_projects = site['projects'] | data_filter: "featured != true" %}
{% if other_projects.size > 0 %}
## More

<div class="grid" data-style="more">
{% include list.html component="card" data="projects" filter="featured != true" style="grid" %}
</div>
{% endif %}
