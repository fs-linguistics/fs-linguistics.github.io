---
title: Updating the Webpage
permalink: /updating-the-webpage/
---

To add/edit blog posts or information pages, you don't need to set up Ruby/Jekyll. You only need to add and/or edit some files, which you can even do on the GitHub code repository itself (no actual git knowledge needed!)

## Adding Blog Posts

Adding posts that appear on the blog section on the main page:

1. Create a new file in the `_posts` directory. The file needs to follow the naming convention `YYYY-MM-DD-some-description-here.markdown`.
2. The file should start with a special header. The actual time of day isn't important, but the date will be displayed as part of the post. You can copy and adapt this header, or just copy, rename and update one of the already existing blog posts. (Jekyll will complain about the `post` layout, but for now giving it a dummy value instead of an actual layout gives the best result.)
```
---
layout: post
title: "POST TITLE HERE!"
date: YYYY-MM-DD HH:MM:SS +0100
---
```
3. It's also possible to add another line to the header, `categories`, e.g. `categories: events` or `categories: announcements`. Once/if we have a lot of posts, this might be interesting for filtering the posts, but for now, it's not really important.
4. The rest of the post is the actual content, written in a flavour of Markdown called [Kramdown](https://kramdown.gettalong.org/quickref.html).

## Adding Pages

1. Create a new markdown file in the `pages` folder.
2. Add a header following this format to your file:
```
---
title: PAGE TITLE HERE
permalink: /URL-SUFFIX-HERE/
---
```
3. The rest of the page is the actual content, written in a flavour of Markdown called [Kramdown](https://kramdown.gettalong.org/quickref.html).
4. To create a link to the page to the sidebar, you need to add it to `_data/navigation.yml`. For intra-website links, only the permalink is necessary, not the full URL.

## Installing Ruby/Jekyll and Running the Page Locally

1. [Install Ruby and Jekyll](https://jekyllrb.com/docs/).
2. Clone this repository and navigate to the corresponding directory.
3. To build the site locally, execute `bundle exec jekyll serve`. It's now available in your browser at <http://localhost:4000>. You can stop the build with `CTRL` + `C`.

## Updating Changes Globally

This can be done without installing Ruby and Jekyll, although it's a good idea to try out changes locally first.

1. Push the changes to the shared repo.
2. GitHub will try to rebuild the page including your changes. In the [commits tab](https://github.com/fs-linguistics/fs-linguistics.github.io/commits/master) of this repo, a green checkmark should appear as part of your commit. This can take a couple of minutes.
3. Check the website (hard refresh, if necessary). It sometimes also takes a few minutes between GitHub adding the green checkmark to your commit and the website actually displaying the changes.

## Jekyll Theme Modifications

We're currently using a modified version of the [Minimal Mistakes theme](https://github.com/mmistakes/minimal-mistakes) for Jekyll. The most important changes are:
- `_includes/archive-single.html`: Overriding the blog post layout
- `assets/css/main.scss`: Custom CSS
- `_data/navigation.yml`: Sidebar contents

To override a file from the theme, simply create a new file in our repo that has the same path as the one in the Minimal Mistakes repo.

## Useful Links

- <https://github.com/ssaunier/jekyll-intro>
- <https://michaelsoolee.com/jekyll-post-page/>
- <https://kramdown.gettalong.org/quickref.html>

<br>

---
<br>

Last updated: 27-JAN-2020
