import datetime

from django.db import models
from django.test import TestCase
from django.urls import reverse

from pinax.calendars.adapters import EventAdapter
from pinax.calendars.templatetags.pinax_calendars_tags import calendar, delta


class EventModel(models.Model):
    date = models.DateTimeField()


class Tests(TestCase):

    def test_delta_previous(self):
        """
        plus_year, plus_month = delta(date.year, date.month, 1)
        minus_year, minus_month = delta(date.year, date.month, -1)
        """
        self.assertEqual(delta(2016, 2, -1), (2016, 1))
        self.assertEqual(delta(2016, 1, -1), (2015, 12))

    def test_delta_next(self):
        """
        plus_year, plus_month = delta(date.year, date.month, 1)
        minus_year, minus_month = delta(date.year, date.month, -1)
        """
        self.assertEqual(delta(2016, 2, 1), (2016, 3))
        self.assertEqual(delta(2015, 12, 1), (2016, 1))

    def test_calendar_prev_next(self):
        events = EventAdapter(EventModel.objects.none())

        context = {}
        cal = calendar(context, events, datetime.datetime(2017, 2, 1))
        self.assertEqual(cal["prev"], reverse("monthly", args=[2017, 1]))
        self.assertEqual(cal["next"], reverse("monthly", args=[2017, 3]))
