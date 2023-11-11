---
title: Updating the Webpage
permalink: /updating-the-webpage/
---

To add/edit blog posts or information pages, you don't need to set up Ruby/Jekyll. You only need to add and/or edit some files, which you can even do on the GitHub code repository itself (no actual git knowledge needed!)

Overview of this page:

- [Adding a blog post](#adding-blog-posts)
- [Adding a (non-blog) page](#adding-pages)
- [Previewing changes locally](#installing-rubyjekyll-and-previewing-the-page-locally)
- [Committing changes to the website](#updating-changes-globally)
- [GitHub security alerts](#security-alerts)
- [Changing the blog layout/theme](#jekyll-theme-modifications)
- [Links to Jekyll and Kramdown tutorials](#useful-links)

## Adding Blog Posts

### Quick and Dirty method

1. Go to the [posts folder in the repo](https://github.com/fs-linguistics/fs-linguistics.github.io/tree/master/_posts) and click on add file and either upload your post as a Markdown file or create a new file.
2. Accept GitHub's suggestion to create a new pull request by clicking 'propose changes'
3. Wait for someone to take a look at your pull request and accept or comment on it.

As for the file, add the following header:

```
---
layout: post
title: "POST TITLE HERE!"
date: YYYY-MM-DD
---
```

Save the file as `YYYY-MM-DD-helpful-title.md`.

### Less Quick, but still speedy

1. Create a new file in the `_posts` directory using the python script:
```
cd _posts
python3 make_post.py "Name Of Post"
```
2. Create a new branch and pull request following the guide for [updating changes globally](#updating-changes-globally).

### Manual method

Adding posts that appear on the blog section on the main page:

1. Create a new branch for your update (see [updating changes globally](#updating-changes-globally))
2. Create a new file in the `_posts` directory. The file needs to follow the naming convention `YYYY-MM-DD-some-description-here.markdown`.
3. The file should start with a special header. You can copy and adapt this header, or just copy, rename and update one of the already existing blog posts. (Jekyll will complain about the `post` layout, but for now giving it a dummy value instead of an actual layout gives the best result.)
```
---
layout: post
title: "POST TITLE HERE!"
date: YYYY-MM-DD
---
```
4. It's also possible to add another line to the header, `categories`, e.g. `categories: events` or `categories: announcements`. Once/if we have a lot of posts, this might be interesting for filtering the posts, but for now, it's not really important.
5. The rest of the post is the actual content, written in a flavour of Markdown called [Kramdown](https://kramdown.gettalong.org/quickref.html).
6. You can add images or other files if you put them in a subfolder of `files`.
7. Create a new pull request and wait for feedback.

## Adding Pages

1. Create a new branch for your new page (see [updating changes globally](#updating-changes-globally)).
2. Create a new markdown file in the `pages` folder.
3. Add a header following this format to your file:
```
---
title: PAGE TITLE HERE
permalink: /URL-SUFFIX-HERE/
---
```
4. The rest of the page is the actual content, written in a flavour of Markdown called [Kramdown](https://kramdown.gettalong.org/quickref.html).
5. To create a link to the page to the sidebar, you need to add it to `_data/navigation.yml`. For intra-website links, only the permalink is necessary, not the full URL.
6. You can add images or other files if you put them in a subfolder of `files`.
7. Create a new pull request and wait for feedback.

## Installing Ruby/Jekyll and Previewing the Page Locally

1. [Install Ruby and Jekyll](https://jekyllrb.com/docs/) (scroll past the requirements and open the guide that matches your operating system; the guides tell you how to install everything you need).
2. Clone this repository: `git clone https://github.com/fs-linguistics/fs-linguistics.github.io.git` and navigate to the corresponding directory.
3. Run `bundle install` to get all of the packages our website relies on.
4. To build the site locally, run `bundle exec jekyll serve`. It's now available in your browser at <http://localhost:4000>. You can stop the build with `CTRL` + `C`. (Don't worry about messages like `Build Warning: Layout 'post' requested in _posts/some-date-and-title-here.markdown does not exist.`)

## Updating Changes Globally

This can be done without installing Ruby and Jekyll, although it's a good idea to try out changes locally first.

We have implemented some controls to avoid breaking changes. Instead of pushing your changes to the shared repo, you now have to create a pull request containing your changes. Depending on how comfortable you feel with the GitHub website and/or CLI, there's two approaches: creating the pull request on the website or on the command line using the GitHub CLI.

### Pull Requests (GitHub)

1. Check out a new branch, make and commit your changes.
```
git checkout -b fix-typos
git add .
git commit -m "Fix typos on all pages of the website"
```
2. Push your new branch.
```
git push
```
3. Create a new pull request on [Github](https://github.com/fs-linguistics/fs-linguistics.github.io/issues), give it an informative title (e.g. "Fix typos on the website").
4. Associate your pull request with the branch you created.
5. Wait for someone (i.e. John or Nicolai) to take a look at your pull request and merge or comment on it.

### Pull Requests (Github CLI)

1. Check out a new branch, make and commit your changes.
```
git checkout -b fix-typos
git add .
git commit -m "Fix typos on all pages of the website"
```
2. Create a pull request using gh.
```
gh pr create -t "Fix typos on the website"
```
3. Answer the questions.
4. Check the pull request looks correct on the website.
5. Wait for someone (i.e. John or Nicolai) to take a look at your pull request and merge or comment on it.

## Security Alerts

Every now and then, GitHub has a security concern for some package that is used to construct the website.

If GitHub provides a [pull request](https://github.com/fs-linguistics/fs-linguistics.github.io/pulls) for this via *@dependabot* with a name like "Bump activesupport from 6.0.2.1 to 6.0.3.1", simply accept the pull request and you're done.

Otherwise, there might just be an alert in the [Security](https://github.com/fs-linguistics/fs-linguistics.github.io/security) tab of the website's GitHub project.
You can click on the button that invites you to perform a Dependabot security update, which will create a pull request for you that you just need to accept.
Alternatively, the security alert will also tell you how to solve the problem yourself: Just add the code it suggests (`gem "gem-name-here", ">= version.number.here"`) to the end of the [Gemfile](https://github.com/fs-linguistics/fs-linguistics.github.io/blob/master/Gemfile), and then run:
```
gem install gem-name-here
gem update gem-name-here
bundle update gem-name-here
bundle install
```
This will update [Gemfile.lock](https://github.com/fs-linguistics/fs-linguistics.github.io/blob/master/Gemfile.lock).
Commit and push the changes.

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
