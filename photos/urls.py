
from django.conf.urls import url, include

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from photos import views
from pystargram import settings

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='login_success.html'), name="test"),
    url(r'^logintest/$', views.logintest, name="test"),
    url(r'^upload/$', views.create, name='create'),
    url(r'^download/(?P<pk>[0-9]+)/$', views.download, name='download'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]



