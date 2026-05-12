---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team


Meet our team of Ph.D. students, Master's students, undergraduates, and research assistants! 

{% include section.html %}

{% include list.html data="members" component="portrait" filter="role == 'principal-investigator'" %}
{% include list.html data="members" component="portrait" filter="role != 'principal-investigator'" %}

{% include section.html background="images/background-new.png" dark=false %}

Interested in collaborating or joining the team? See our [contact page](/contact/) for details.

{% include section.html %}

{% capture content %}

{% endcapture %}

{% include grid.html style="square" content=content %}
