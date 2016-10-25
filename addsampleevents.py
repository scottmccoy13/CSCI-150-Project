import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'rentProg.settings'
import django
django.setup()


from schedule.models import Calendar, Event
from django.utils import timezone
from datetime import timedelta


calendar = Calendar(name='rental calendar', slug='rentalcal')
calendar.save()

Event(title='meet foo at bar',
      calendar=calendar,
      start=timezone.now(),
      end=timezone.now() + timedelta(hours=1)).save()
