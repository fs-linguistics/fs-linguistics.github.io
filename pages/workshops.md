---
title: Workshops 
permalink: /workshops/
---


We are currently offering workshops every week led by students where we talk about comp ling  related  topics.

[Updating the site](/collections/_workshops/simple_website)

<ul>
    {% for post in site.workshop %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>