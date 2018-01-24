from django.conf.urls import url
from django.views.generic import View

urlpatterns = [
    url(r"^(?P<year>\d{4})/(?P<month>\d{1,2})/$", View.as_view(), name="monthly"),
    url(r"^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$", View.as_view(), name="daily"),
]
