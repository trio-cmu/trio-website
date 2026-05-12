---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
# some backup from below
#{%
#  include button.html
#  type="phone"
#  text="(412) 867-5309"
#  link="+1-555-867-5309"
#%}
#{% include section.html %}
#
#{% capture col1 %}
#
#{%
#  include figure.html
#  image="images/photo.jpg"
#  caption="Lorem ipsum"
#%}
#
#{% endcapture %}
#
#{% capture col2 %}
#
#{%
#  include figure.html
#  image="images/photo.jpg"
#  caption="Lorem ipsum"
#%}
#
#{% endcapture %}
#
#{% include cols.html col1=col1 col2=col2 col3=col3 %}
#{% include cols.html col1=col1 col2=col2 %}
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

We are actively growing our lab. If you are an incoming student, an interested collaborator, or just generally curious about what we do, please check out our [projects page](/projects/) for open positions and get in touch! 

{% capture col1 %}

{% include icon.html icon="fa-solid fa-door-open" %} **PI Office**  
Scaife Hall, Room 218

{% endcapture %}

{% capture col2 %}

{% include icon.html icon="fa-solid fa-robot" %} **Lab Space**  
Scaife Hall, Room B15

{% endcapture %}

{% capture col3 %}

{% include icon.html icon="fa-solid fa-phone" %} **Phone**  
(412) 268-2508

{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}

{%
  include button.html
  type="email"
  text="fduembgen@cmu.edu"
  link="mailto:fduembgen@cmu.edu"
%}
{%
  include button.html
  type="address"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://maps.app.goo.gl/kUELcocF9kgT6hnP8"
%}


{% include section.html %}

{% capture col1 %}
Lorem ipsum dolor sit amet  
consectetur adipiscing elit  
sed do eiusmod tempor
{% endcapture %}

{% capture col2 %}
Lorem ipsum dolor sit amet  
consectetur adipiscing elit  
sed do eiusmod tempor
{% endcapture %}

{% capture col3 %}
Lorem ipsum dolor sit amet  
consectetur adipiscing elit  
sed do eiusmod tempor
{% endcapture %}

