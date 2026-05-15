---
---

{% assign project_images = site.static_files | where_exp: "file", "file.path contains '/images/projects/'" | map: "path" | sort %}
{% assign team_images = site.static_files | where_exp: "file", "file.path contains '/images/team/'" | map: "path" | sort %}

<div class="project-hero">
  <h1 class="page-title">TRIO Lab @ Carnegie Mellon University</h1>
  <h3 class="page-subtitle">Welcome to TRIO Lab! We work at the intersection of robotics, intelligence and optimization to build trusworthy autonomous agents for the physical world.</h3>
  <p>🤖 🚧 This website is currently under construction. Please reach out if you have any questions! 🚧 🤖</p>
</div>

{% include section.html %}

## Highlights

{% capture text %}

Our overarching goal is to create physical intelligence that is trustworthy and scalable. To do so, we use and expand the capabilities of optimization tools and artificial intelligence, making them suitable for interactions with the real world.

{%
  include button.html
  link="projects"
  text="Browse projects & open positions"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  images=project_images
  link="projects"
  title="Our Projects"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

Meet our team of Ph.D. students, Master's students, undergraduates, and research assistants! 

{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  images=team_images
  link="team"
  title="Our Team"
  text=text
%}
