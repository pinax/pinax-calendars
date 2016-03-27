Pinax Calendars
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
    
    
Pinax
------

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. 
This collection can be found at http://pinaxproject.com.

This app was developed as part of the Pinax ecosystem but is just a Django app and can be used independently of other Pinax apps.


pinax-calendars
-----------------

``pinax-calendars`` provides utilities for publishing events as a calendar.

At the moment, it just provides a visual calendar (both large and small)
showing which days have events and optionally linking to a day detail page.

There is a `demo project <https://github.com/pinax/pinax-calendars-demo>`_ that
you can clone and run to see it in action.


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


Documentation
----------------

The ``pinax-calendars`` documentation can be found at http://pinax-calendars.readthedocs.org/en/latest/. The Pinax documentation is available at http://pinaxproject.com/pinax/. If you would like to help us improve our documentation or write more documentation, please join our Pinax Project Slack team and let us know!


Contribute
----------------

See this blog post http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/ including a video, or our How to Contribute (http://pinaxproject.com/pinax/how_to_contribute/) section for an overview on how contributing to Pinax works. For concrete contribution ideas, please see our Ways to Contribute/What We Need Help With (http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any question we recommend you join our Pinax Slack team (http://slack.pinaxproject.com) and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our Open Source and Self-Care blog post (http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).  


Code of Conduct
-----------------

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a code of conduct, which can be found here  http://pinaxproject.com/pinax/code_of_conduct/. 
We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.



Pinax Project Blog and Twitter
-------------------------------

For updates and news regarding the Pinax Project, please follow us on Twitter at @pinaxproject and check out our blog http://blog.pinaxproject.com.

