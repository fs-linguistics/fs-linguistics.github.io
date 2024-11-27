---
title: "Job Offers"
permalink: /job-offers/
---

# List of recent job offers
{% for item in site.job-offers %}
  <ul>
      <li>{{item.date | date: '%B %d, %Y'}}:  <a href="{{ item.url }}">{{ item.title }}</a></li>
  </ul>
{% endfor %}