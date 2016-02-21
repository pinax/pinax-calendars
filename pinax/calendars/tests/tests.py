from django.test import TestCase

from pinax.calendars.templatetags.pinax_calendars_tags import delta


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
