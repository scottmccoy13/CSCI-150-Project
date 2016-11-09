from . import views
from django.conf.urls import url

app_name = 'login'

urlpatterns = {
    url(r'^register/$', views.UserFormView.as_view(), name='index'),
}