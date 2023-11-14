---
title: Workshops 
permalink: /workshops/
---


We are currently offering workshops every week led by students where we talk about comp ling  related  topics.

Workshops we've offered:

{% for item in site.workshops %}
  <ul>
      <li><a href="{{ item.url }}">{{ item.title }}</a></li>
  </ul>
{% endfor %}
