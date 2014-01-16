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


@register.inclusion_tag("kairios/calendar.html", takes_context=True)
def calendar(context, events, date=None, **kwargs):
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
            is_today = date.year == today.year and date.month == today.month and today.day == day
            if day:
                day_events = events_by_day.get(day, [])
                link = events.day_url(date.year, date.month, day, bool(day_events))
                row.append((day, day_events, link, is_today))
            else:
                row.append(None)
        grid.append(row)
    
    context.update({
        "title": title,
        "calendar_date": date,
        "prev": prev,
        "next": next,
        "grid": grid,
    })
    return context
