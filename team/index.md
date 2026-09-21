---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# Our team

<p class="team-intro">Meet the people working together to build trustworthy robotics, intelligence, and optimization at Carnegie Mellon University.</p>

<div class="team-grid">
  {% assign principal_investigators = site.members | where: "role", "principal-investigator" | sort: "name" %}
  {% for member in principal_investigators %}
    {% include portrait.html lookup=member.slug %}
  {% endfor %}
  {% for group in site.data.team_groups %}
    {% unless group.role == "principal-investigator" %}
      {% assign members = site.members | where: "role", group.role | sort: "name" %}
      {% for member in members %}
        {% include portrait.html lookup=member.slug %}
      {% endfor %}
    {% endunless %}
  {% endfor %}
</div>

{% include section.html %}

{% include carousel.html class="team-carousel" aria_label="Life at TRIO Lab" items=site.data.team_carousel %}

{% include section.html background="images/background-new.png" dark=false %}

<h2 class="team-join-title">Join the team</h2>
<p class="team-intro">Interested in collaborating or joining TRIO? We'd love to hear from you.</p>
<div class="team-join-action">
  <a class="button" href="{{ '/contact/' | relative_url }}">Get in touch <span aria-hidden="true">&rarr;</span></a>
</div>
