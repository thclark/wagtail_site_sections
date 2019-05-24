# Wagtail Site Sections [![Build Status](https://travis-ci.com/thclark/wagtail_site_sections.svg?branch=master)](https://travis-ci.com/thclark/wagtail_site_sections)

Common wagtail streamfield blocks for quickly building website sections.

Hero panels, "our team" views, product list, FAQs, etc) added to pages as wagtail stream fields.


## Why

You're creating a website and app for an awesome startup. Or club, or business or whatever. So you download a bunch of
component templates for the front end.

> *Man, they look great!!! Built by professional designers, everything looks totes amazeballs!*

You'll turn this into a proper app eventually, so wordpress is out. You want something serving your site and 
So you build a fantastic looking site. But the client really ought to be able to edit their own website content... 
they need either:
- A CMS.
- Knowledge of how to chop and change their site around at the code level, then rebuild and deploy it to wherever.

Sigh. And:
- I don't want to be charging my clients a half day every time they need a site tweak, it feels wrong.
- I don't want to be hassled by clients for site tweaks, its annoying and there are bigger fish to fry.

So lets just set them up with any ol' page structure they want!

Enter wagtail streamfield - the [docs]() for streamfield show you how to quickly and flexibly create streamfield blocks
to manage sections like this.

If you need flexibility, create your own blocks! But in my experience, most sites need exactly the same BS time after time.
So here it is. A bunch of common blocks for building website chunks.

Either copy/paste them, install this app and use everything out of the box, or subclass blocks from this app to customise.


## An Example

I built [traffickingpast.uk](TODO) using wagtail_site_blocks.  

I took templates from [creative-tim](https://www.creative-tim.com/product/material-kit-pro-react), built site pages
and an app, using wagtail in headless mode to administer the app contents (stories, legislation records and locations
for the map).

But the site pages were practically uneditable by my clients - they'd need to know how to edit the JSX as well as
understand the git flow in order to deploy changes. It's a big ask, and not what those ridiculously clever and dedicated
historians were put on earth to do.

I was already using [wagtail-react-streamfield](TODO) to render the contents of the stories, so figured why not do the same
with page content? I just added a streamfield with wagtail_site_blocks to my BasePage model and bingo... no technical
skill required to make substantial edits to the site.


## Emotional gratification

I don't publish OSS for money. I do it:
 - to have impact on the world
 - for the emotional gratification of helping people out
 - to repay all the OSS developers who've made me better and quicker at what I do.

**Bottom line: Star this repo on Github if you use or like it, that's my payment! :)** 


## Architectural decision - streamfields not snippets

I could just as easily have made each section a SectionSnippet (of some different type), rather than using streamfield. But:
 - This is somewhat less flexible in terms of arranging page content
 - It's less easily extensible to add new sections
 - Data is stored off the Page Model in a different table, and I think it's best to keep Page data (which eventually all
 gets rendered to what is essentially a static page) all in one place rahter than creating unnecessary joins)


## Templates

**"But, where are the templates?!"** is a natural question. Answer: There aren't any templates so far... but you can add
yours straightforwardly.

I run all my wagtail installations in headless mode with a react front end, so can only justify putting in place the
templates for managing the sections on wagtail (for now). If there's enough traffic to be concerned about performance of
a SPA instead of server-side rendered pages, I'll add gatsby into the mix to pre-build the site pages.
That'll scale epically.

If you'd like to make a PR so this can be used more easily in a non-headless mode, I'm very open to collaboration :)


## Displaying sections on the front end

### Create components

Its up to you how you wire them up, but you basically need a nice looking component for each section type which accepts
as props the schema of the section (see below for section schema).

### React: Turn streamfield data into component props

On the frontend, I use react (see aforementioned nanorant about using wagtail in a headless mode). 

I use my other library, [wagtail-react-streamfield]() to extract streamfield data as component props, and render the 
streamfield as lists/hierarchies of components, selecting component by streamfield type.


## Roadmap

I'd like to include many more sections. I'm adding as I use them on a site. If you need a section, either:
- Fork, add, and make a PR. I'll review when I have time and if it meets quality then I'll add.
- write out the schema for the section you want and chuck that into an issue. I'll consider adding at some point but no promises.
- If you want "some point" to be very soon, and want "no promises" to be "promises" then that's cool but I'll need to be paid ;)


## Requirements

Wagtail_site_sections is tested on Django 2.1 or later and Wagtail 2.3 or later.


## Supported Versions

Python: 3.6

Django: 2.1

Wagtail: 2.3


## Getting started

Installing from pip:

```
pip install wagtail_site_sections
```

### If you already have your own page models and don't want to add another table/app...
Add the following to your *Page model:
```
```

### Or if you want to use the SectionsPage model...

Add to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...,
    'wagtail_site_sections',
    ...
]
```
Run the migrations:
```
python manage.py migrate wagtail_site_sections
```
Then add a SectionPage to your CMS and give it a whirl.

