---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team


Meet our team of Ph.D. students, Master's students, undergraduates, and research assistants! 


{% include carousel.html class="team-carousel" aria_label="Team image carousel" items=site.data.team_carousel %}


{% include section.html %}

{% include list.html data="members" component="portrait" filter="role == 'principal-investigator'" sort="name" %}
{% include list.html data="members" component="portrait" filter="role == 'phd'" sort="name" %}
{% include list.html data="members" component="portrait" filter="role == 'phd-incoming'" sort="name" %}
{% include list.html data="members" component="portrait" filter="role == 'masters'" sort="name" %}
{% include list.html data="members" component="portrait" filter="role == 'visitor'" sort="name" %}
{% include list.html data="members" component="portrait" filter="role == 'research-assistant'" sort="name" %}
{% include list.html data="members" component="portrait" filter="role == 'undergrad'" sort="name" %}
{% include list.html data="members" component="portrait" filter="role != 'principal-investigator' and role != 'phd' and role != 'phd-incoming' and role != 'masters' and role != 'visitor' and role != 'research-assistant' and role != 'undergrad'" sort="name" %}

{% include section.html background="images/background-new.png" dark=false %}

Interested in collaborating or joining the team? See our [contact page](/contact/) for details.

{% include section.html %}

{% capture content %}

{% endcapture %}

{% include grid.html style="square" content=content %}
