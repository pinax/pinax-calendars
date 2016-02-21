from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(BaseAppConfig):

    name = "pinax.calendars"
    label = "pinax_calendars"
    verbose_name = _("Pinax Calendars")
