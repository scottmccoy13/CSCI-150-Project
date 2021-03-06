"""rentProg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from login import urls

urlpatterns = [
    url(r'^', include('login.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^calendar/', include('Calendar.urls')),
    url(r'^CustomerData/', include('CustomerData.urls')),
    url(r'^assetdata/', include('AssetData.urls')),
    url(r'^schedule/', include('schedule.urls'))
]
