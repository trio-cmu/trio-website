---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# Our team

<p class="team-intro">Meet the people working together to build trustworthy robotics, intelligence, and optimization at Carnegie Mellon University.</p>

<div class="team-lead">
  {% assign principal_investigators = site.members | where: "role", "principal-investigator" | sort: "name" %}
  {% for member in principal_investigators %}
    <div class="team-lead-card">
      {% include portrait.html lookup=member.slug clickable=false %}
      <div class="team-lead-links">
        {% for link in member.links %}
          {% assign key = link[0] %}
          {% assign value = link[1] %}
          {% include button.html type=key link=value text="" style="bare" %}
        {% endfor %}
      </div>
    </div>
  {% endfor %}
</div>

{% include section.html %}

<div class="team-grid">
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
