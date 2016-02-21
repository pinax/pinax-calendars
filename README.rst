pinax-calendars
=======

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/

.. image:: https://img.shields.io/travis/pinax/pinax-calendars.svg
    :target: https://travis-ci.org/pinax/pinax-calendars

.. image:: https://img.shields.io/coveralls/pinax/pinax-calendars.svg
    :target: https://coveralls.io/r/pinax/pinax-calendars

.. image:: https://img.shields.io/pypi/dm/pinax-calendars.svg
    :target:  https://pypi.python.org/pypi/pinax-calendars/

.. image:: https://img.shields.io/pypi/v/pinax-calendars.svg
    :target:  https://pypi.python.org/pypi/pinax-calendars/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target:  https://pypi.python.org/pypi/pinax-calendars/

Provides utilities for publishing events as a calendar.

At the moment, it just provides a visual calendar (both large and small)
showing which days have events and optionally linking to a day detail page.


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
