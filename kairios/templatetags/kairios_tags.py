import calendar as cal
import datetime

from django import template


register = template.Library()


def delta(year, month, d):
   mm = month + d
   yy = year
   if mm > 12:
       mm, yy = mm % 12, year + mm / 12
   elif mm < 1:
       mm, yy = 12 + mm, year - 1
   return yy, mm


@register.inclusion_tag("kairios/calendar.html")
def calendar(events, date=None, **kwargs):
    cal.setfirstweekday(cal.SUNDAY)
    
    today = datetime.date.today()
    
    if date is None:
        date = today
    
    plus_year, plus_month = delta(date.year, date.month, 1)
    minus_year, minus_month = delta(date.year, date.month, -1)
    
    next = events.month_url(plus_year, plus_month)
    prev = events.month_url(minus_year, minus_month)
    
    events_by_day = events.events_by_day(date.year, date.month)
    
    title = "%s %s" % (cal.month_name[date.month], date.year)
    
    matrix = cal.monthcalendar(date.year, date.month)
    grid = []
    for week in matrix:
        row = []
        for day in week:
            if date.year == today.year and date.month == today.month and today.day == day:
                is_today = True
            else:
                is_today = False
            if day:
                has_event = day in events_by_day
                link = events.day_url(date.year, date.month, day, has_event)
                row.append((day, has_event, link, is_today))
            else:
                row.append(None)
        grid.append(row)
    
    return {
        "title": title,
        "prev": prev,
        "next": next,
        "grid": grid,
    }
