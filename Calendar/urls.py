from django.conf.urls import url
from django.views.generic import TemplateView

from Calendar.views import full_calendar

urlpatterns = [
    url(r'^$', full_calendar, name='calendar')
]
