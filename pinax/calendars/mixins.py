import datetime

from django.utils import timezone


class DailyMixin(object):

    month_kwarg_name = "month"
    year_kwarg_name = "year"
    day_kwarg_name = "day"

    def dispatch(self, request, *args, **kwargs):
        self.month = self.kwargs.get(self.month_kwarg_name)
        self.year = self.kwargs.get(self.year_kwarg_name)
        self.day = self.kwargs.get(self.day_kwarg_name)
        self.date = datetime.date(
            year=int(self.year),
            month=int(self.month),
            day=int(self.day)
        )
        return super(DailyMixin, self).dispatch(request, *args, **kwargs)


class MonthlyMixin(object):

    month_kwarg_name = "month"
    year_kwarg_name = "year"

    def dispatch(self, request, *args, **kwargs):
        self.month = self.kwargs.get(self.month_kwarg_name)
        self.year = self.kwargs.get(self.year_kwarg_name)
        if self.month and self.year:
            self.date = datetime.date(
                year=int(self.year),
                month=int(self.month),
                day=1
            )
        else:
            self.date = timezone.now().date()
        return super(MonthlyMixin, self).dispatch(request, *args, **kwargs)
