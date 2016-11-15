from . import views
from django.conf.urls import url

app_name = 'login'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$',views.login_user, name = 'login_user'),
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
]