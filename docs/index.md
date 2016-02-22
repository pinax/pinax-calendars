# pinax-calendars

!!! note "Pinax Ecosystem"
    This app was developed as part of the Pinax ecosystem but is just a Django app
    and can be used independently of other Pinax apps.

    To learn more about Pinax, see <http://pinaxproject.com/>

`pinax-calendars`, formerly named `kairios` is a app that provides Django
utilities for publishing events as a calendar


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
