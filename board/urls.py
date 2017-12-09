
from django.conf.urls import url, include

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from board.views import PostListView
from photos import views
from pystargram import settings


urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    url(r'^$', PostListView.as_view(), name="index"),
    url(r'^post/$', TemplateView.as_view(template_name='post.html'), name="post"),

]



