"""
This script resets the password of the first user it finds to the following password. Use it when you're using the
correct credentials, yet you are unable to log in to the admin site.
"""
password = 'password'


import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'rentProg.settings'
import django
django.setup()
from django.contrib.auth.models import User
users = User.objects.all()
user = users[0]
user.set_password(password)
user.save()
