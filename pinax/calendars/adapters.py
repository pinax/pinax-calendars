from collections import defaultdict

from django.core.urlresolvers import reverse


class EventAdapter(object):
    day_url_name = "daily"
    month_url_name = "monthly"
    date_field_name = "date"

    def __init__(self, queryset):
        self.events = queryset

    def day_url(self, year, month, day, has_event, **kwargs):
        if has_event:
            return reverse(self.day_url_name, args=[year, month, day])

    def month_url(self, year, month, **kwargs):
        return reverse(self.month_url_name, args=[year, month])

    def events_by_day(self, year, month, **kwargs):
        days = defaultdict(list)
        query_args = {
            "{}__year".format(self.date_field_name): year,
            "{}__month".format(self.date_field_name): month
        }
        for event in self.events.filter(**query_args).order_by(self.date_field_name):
            days[getattr(event, self.date_field_name).day].append(event)
        return days
