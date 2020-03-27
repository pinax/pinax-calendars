from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import gettext_lazy as _


class AppConfig(BaseAppConfig):

    name = "pinax.calendars"
    label = "pinax_calendars"
    verbose_name = _("Pinax Calendars")
