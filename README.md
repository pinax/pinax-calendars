![](http://pinaxproject.com/pinax-design/patches/pinax-calendars.svg)

# Pinax Calendars

[![](https://img.shields.io/pypi/v/pinax-stripe.svg)](https://pypi.python.org/pypi/pinax-calendars/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://pypi.python.org/pypi/pinax-calendars/)

[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-calendars.svg)](https://codecov.io/gh/pinax/pinax-calendars)
[![CircleCI](https://circleci.com/gh/pinax/pinax-calendars.svg?style=svg)](https://circleci.com/gh/pinax/pinax-calendars)
![](https://img.shields.io/github/contributors/pinax/pinax-calendars.svg)
![](https://img.shields.io/github/issues-pr/pinax/pinax-calendars.svg)
![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-calendars.svg)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
        
## Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. 
This collection can be found at http://pinaxproject.com.

This app was developed as part of the Pinax ecosystem but is just a Django app and can be used independently of other Pinax apps.


## pinax-calendars

``pinax-calendars``, formerly named `kairios` provides utilities for publishing events as a calendar.

At the moment, it just provides a visual calendar (both large and small)
showing which days have events and optionally linking to a day detail page.

There is a `demo project <https://github.com/pinax/pinax-calendars-demo>`_ that
you can clone and run to see it in action.


## Development

The source repository can be found at https://github.com/pinax/pinax-calendars/
and a demo project can be cloned and run locally to see how it all works from
https://github.com/pinax/pinax-calendars-demo/


## Quickstart

Install the package:

    pip install pinax-calendars

Add `pinax.calendars` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        # other apps
        "pinax.calendars",
    )
    
 
## Usage

Using `pinax-calendars` is a combination of setting up at least view that can
paginate through months, adapting a queryset of date based data, and using a
template tag.

The end result is to render a month based view of all your events.

### View Mixins

There are two mixins to make it easier to write monthly (`pinax.calendars.mixins.MonthlyMixin`)
and daily (`pinax.calendars.mixins.DailyMixin`) views.

### Monthly Mixin

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

### Daily Mixin

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

<!--
Usage
-----

::

    {% load pinax_calendars_tags %}

    ...

    {% calendar events %}


where ``events`` implements the following protocol:

``events.day_url(year, month, day, has_event, **kwargs)``
  return a link to the page for the given day or None if there is not to
  be a day link. ``has_event`` is a boolean telling this method whether
  there is an event on the day or not so you can choose whether a day
  without an event should link or not.

``events.month_url(year, month, **kwargs)``
  return a link to the page for the given month or None if there is not
  to be a month link.

``events_by_day(year, month, **kwargs)``
  return a dictionary mapping day number to a list of events on that day.

Note that all methods take additional key-word arguments that can be used in
the calculation of the return value.
-->

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

```
{% load pinax_calendars_tags %}

{% block body %}
    {% calendar events %}
{% endblock %}
```

### Template Include

We ship a [template include fragment](https://github.com/pinax/pinax-calendars/blob/master/pinax/calendars/templates/pinax/calendars/calendar.html)
that the tag will render and include wherever you place the tag. It uses semantic
markup to make styling it easy and free from any framework bias (as much as
possible, at least).

The template path, in case you want to override it, is at
`pinax/calendars/calendar.html`.

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

If you use the included template that the `{% calendar %}` tag includes as-is,
then you can add this bit of LESS to your project if you are building upon
Bootstrap:

```less
.calendar-table {
    .table;
    .table-bordered;
    td {
        width: 14.2vw;
        height: 14.2vmin;
    }
}
```

This will render a full width monthly calendar with responsive squares for each
day.


## ChangeLog

### 1.1.0

* Added timezone support for calendar [PR #5](https://github.com/pinax/pinax-calendars/pull/5)


### 1.0.0

* Added docs


### 0.6

* Added `adapters.py` and `mixins.py`


### 0.5

* Donated to Pinax from Eldarion
* Renamed from `kairios` to `pinax-calendars`


## Documentation

The ``pinax-calendars`` documentation can be found at http://pinax-calendars.readthedocs.org/en/latest/. The Pinax documentation is available at http://pinaxproject.com/pinax/. If you would like to help us improve our documentation or write more documentation, please join our Pinax Project Slack team and let us know!


## Contribute

See this blog post http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/ including a video, or our How to Contribute (http://pinaxproject.com/pinax/how_to_contribute/) section for an overview on how contributing to Pinax works. For concrete contribution ideas, please see our Ways to Contribute/What We Need Help With (http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any question we recommend you join our Pinax Slack team (http://slack.pinaxproject.com) and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our Open Source and Self-Care blog post (http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).  


## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a code of conduct, which can be found here  http://pinaxproject.com/pinax/code_of_conduct/. 
We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Pinax Project Blog and Twitter

For updates and news regarding the Pinax Project, please follow us on Twitter at @pinaxproject and check out our blog http://blog.pinaxproject.com.