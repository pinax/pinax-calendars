![](http://pinaxproject.com/pinax-design/patches/pinax-calendars.svg)

# Pinax Calendars

[![](https://img.shields.io/pypi/v/pinax-calendars.svg)](https://pypi.python.org/pypi/pinax-calendars/)

[![CircleCI](https://img.shields.io/circleci/project/github/pinax/pinax-calendars.svg)](https://circleci.com/gh/pinax/pinax-calendars)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-calendars.svg)](https://codecov.io/gh/pinax/pinax-calendars)
[![](https://img.shields.io/github/contributors/pinax/pinax-calendars.svg)](https://github.com/pinax/pinax-calendars/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-calendars.svg)](https://github.com/pinax/pinax-calendars/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-calendars.svg)](https://github.com/pinax/pinax-calendars/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Table of Contents

* [About Pinax](#about-pinax)
* [Important Links](#important-links)
* [Overview](#overview)
  * [Supported Django and Python Versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Usage](#usage)
  * [View Mixins](#view-mixins)
  * [Event Queryset Adapter](#event-queryset-adapter)
  * [Template Tag](#template-tag)
  * [Templates](#templates)
  * [Style](#style)  
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)


## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable
Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## Important Links

Where you can find what you need:
* Releases: published to [PyPI](https://pypi.org/search/?q=pinax) or tagged in app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Global documentation: [Pinax documentation website](https://pinaxproject.com/pinax/)
* App specific documentation: app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Support information: [SUPPORT.md](https://github.com/pinax/.github/blob/master/SUPPORT.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Contributing information: [CONTRIBUTING.md](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Current and historical release docs: [Pinax Wiki](https://github.com/pinax/pinax/wiki/)


## pinax-calendars

### Overview

`pinax-calendars`, formerly named `kairios` provides utilities for publishing events as a calendar.

At the moment, it just provides a visual calendar (both large and small)
showing which days have events and optionally linking to a day detail page.

There is a [demo project](https://github.com/pinax/pinax-calendars-demo/) that
you can clone and run to see pinax-calendars in action.

#### Supported Django and Python Versions

Django / Python | 3.6 | 3.7 | 3.8
--------------- | --- | --- | ---   
2.2  |  *  |  *  |  *   
3.0  |  *  |  *  |  * 


## Documentation

### Installation

To install pinax-calendars:

```shell
    $ pip install pinax-calendars
```

Add `pinax.calendars` to your `INSTALLED_APPS` setting:

```python
    INSTALLED_APPS = [
        # other apps
        "pinax.calendars",
    ]
```

### Usage

Using `pinax-calendars` is a combination of setting up a view that can
paginate through months, adapting a queryset of date-based data, and using a
template tag.

The end result is to render a month-based view of all your events.

Example:

```django
{% load pinax_calendars_tags %}

{% calendar events %}
```

where `events` implements the following protocol:

#### `events.day_url(year, month, day, has_event, **kwargs)`

Returns a link to the page for the given day or None.
`has_event` is a boolean telling this method whether
there is an event on the day or not so you can choose whether a day
without an event should link or not.

#### `events.month_url(year, month, **kwargs)`

Returns a link to the page for the given month or None.

#### `events_by_day(year, month, **kwargs)`

Returns a dictionary mapping day number to a list of events on that day.

Note that all methods take additional keyword arguments used for
calculating the return value.

### View Mixins

There are two mixins to make it easier to write monthly (`pinax.calendars.mixins.MonthlyMixin`)
and daily (`pinax.calendars.mixins.DailyMixin`) views.

#### Monthly Mixin

The `MonthlyMixin` will add `month_kwarg_name` and `year_kwarg_name` properties
to the view and default to `"month"` and `"year"` respectively. These should be set
to match the url pattern for the view.

During the `dispatch()` phase of the view lifecycle, these parameters will be
fetched and if they are present, will be coalesced into a `datetime.date` object
passing `1` for the `day` attribute.  If `month` or `year` are not found in the
url, then `timezone.now().date()` will be used.  Either one of these options
will set the `date` property of the view.  This is done so you can provide a
default view that doesn't have the year and month in the url without having
to redirect.

This `date` property can then be used in your view to pass to the template
context as the `{% calendars %}` template tag will need the date you are
viewing.

#### Daily Mixin

The `DailyMixin` will add `month_kwarg_name`, `year_kwarg_name`, and `day_kwargs_name`
properties to the view and default to `"month"`, `"year"`, `"day"` respectively.
These should be set to match the url pattern for the view.

During the `dispatch()` phase of the view lifecycle, these parameters will be
fetched and coalesced into a `datetime.date` object which gets set to
`self.date` on the view.

This `date` property can then be used in your view to pass to the template
context as well as filter your event queryset for just that date.

### Event Queryset Adapter

We use a basic adapter pattern to provide the `calendar` tag with some things
it needs. There is a base adapter provided in `pinax.calendars.adapters.EventAdapter`
but is designed in a way to override parts of it as needed for your use case.

The adapter is providing three functions:

1. computing a daily url, used to link to a daily detail view
2. computing a monthly url, used for monthly pagination
3. structuring event queryset data in a way that can be iterated over in the
   template include.

All three methods receive extra `kwargs` that are passed directly from the
template tag in case you need to do something custom in your site's integration
of `pinax-calendars`.

#### Daily URL

By default, `EventAdapter.day_url_name` is set to `"daily"` and `reverse()` uses
`year`, `month`, and `day` arguments to construct the url.  This is done in the
`EventAdapter.day_url` method which also receives a `has_event` parameter. The
default implementation of `day_url()` will only return a URL if `has_event` is
`True`.

#### Monthly URL

By default, `EventAdapter.month_url_name` is set to `"monthly"` and `reverse()`
uses `year`, and `month` arguments to construct the url.  This is done in the
`EventAdapter.month_url` method.

#### Events By Day

The `EventAdapter.events_by_day` method takes `year` and `month` arguments. By
default, it will construct filter arguments based on the `EventAdapter.date_field_name`
property, which defaults to `"date"`, to filter the `self.queryset` by `year`
and `month` (e.g. `date__year=year, date__month=month`).

It will then collect events into date buckets and return a dictionary of lists.

### Template Tag

The template tag is pretty simple. It expects an adapted queryset along with
the date representing the month that you are wanting to display. If no date is
supplied, then it will assume that you mean the current month.  You can also
optionally supply a timezone in which case `timezone.now` will be localized to
that timezone for the purposes of displaying the current month.

Example:

```django
{% load pinax_calendars_tags %}

{% block body %}
    {% calendar events %}
{% endblock %}
```

### Templates

Default templates are provided by the `pinax-templates` app in the
[calendars](https://github.com/pinax/pinax-templates/tree/master/pinax/templates/templates/pinax/calendars)
section of that project.

Reference pinax-templates
[installation instructions](https://github.com/pinax/pinax-templates/blob/master/README.md#installation)
to include these templates in your project.

View live `pinax-templates` examples and source at [Pinax Templates](https://templates.pinaxproject.com/calendars/templatetags/)!

#### Customizing Templates

Override the default `pinax-templates` templates by copying them into your project
subdirectory `pinax/calendars/` on the template path and modifying as needed.

For example if your project doesn't use Bootstrap, copy the desired templates
then remove Bootstrap and Font Awesome class names from your copies.
Remove class references like `class="btn btn-success"` and `class="icon icon-pencil"` as well as
`bootstrap` from the `{% load i18n bootstrap %}` statement.
Since `bootstrap` template tags and filters are no longer loaded, you'll also need to update
`{{ form|bootstrap }}` to `{{ form }}` since the "bootstrap" filter is no longer available.

#### `calendar.html`

Rendered by the `{% calendar %}` template tag. The template uses semantic
markup to make styling easy and relatively free of framework bias.

The entire block is wrapped in a `div.calendar`, there is a header with some
nav, followed by a table (`table.calendar-table` for which there is a bit of
bootstrap style included below).

```
div.calendar
  div.calendar-heading
    h3.calendar-title
    div.calendar-nav
      a[href=prev]
      span.calendar-date
      a[href=next]
  div.calendar-body
    table.calendar-table
      tr
        td.day.noday
        - or -
        td.day.[day-has-events|day-no-events]
          a.day-number
          - or -
          span.day-number
          div.day-event-list
            div.day-event
```

### Style

If you use pinax-templates `calendar.html` template, you can add
this bit of SCSS to your project (if you are building upon Bootstrap)
to render a full width monthly calendar with responsive squares for each day:

```scss
.calendar-table {
    @extend table;
    td {
        width: 14.2vw;
        height: 14.2vmin;
    }
}
```


## Change Log

### 3.0.0

* Drop Django 1.11, 2.0, and 2.1, and Python 2,7, 3.4, and 3.5 support
* Add Django 2.2 and 3.0, and Python 3.6, 3.7, and 3.8 support
* Update packaging configs
* Direct users to community resources

### 2.0.4

* Remove local template in favor of pinax-templates

### 2.0.3

* fix `reverse` import
* add tests

### 2.0.2

* Update requirements, add django>=1.11
* Update sorting config
* Update documentation
* Remove doc build

### 2.0.1

* fix setup.py LONG_DESCRIPTION for PyPi

### 2.0.0

* Add Django 2.0 compatibility testing
* Drop Django 1.8, 1.9, 1.10 and Python 3.3 support
* Convert CI and coverage to CircleCi and CodeCov
* Add PyPi-compatible long description
* Move documentation to README.md

### 1.1.0

* Added timezone support for calendar [PR #5](https://github.com/pinax/pinax-calendars/pull/5)

### 1.0.0

* Added docs

### 0.6

* Added `adapters.py` and `mixins.py`

### 0.5

* Donated to Pinax from Eldarion
* Renamed from `kairios` to `pinax-calendars`


## Contribute

[Contributing](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) information can be found in the [Pinax community health file repo](https://github.com/pinax/.github).


## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a [Code of Conduct](https://github.com/pinax/.github/blob/master/CODE_OF_CONDUCT.md). We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject) and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-present James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).
