---
title: Workshops 
permalink: /student-workshops/
---


We offer workshops every once in a while led by students which cover topics related to (computational) linguistics and programming.

To stay up-to-date with the workshops, join the WhatsApp community or [our moodle](https://moodle.zdv.uni-tuebingen.de/enrol/index.php?id=428)

Workshops we've offered:

{% for item in site.workshops %}
  <ul>
      <li>{{item.date | date: '%B %d, %Y'}}:  <a href="{{ item.url }}">{{ item.title }}</a></li>
  </ul>
{% endfor %}
