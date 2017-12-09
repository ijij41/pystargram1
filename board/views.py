# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView

from board.models import Post

class PostListView(ListView):
    # http://localhost:8000/board/?page=2
    # template_name = 'blog/post_all.html'
    template_name = 'test_post_list.html'
    content_object_name ='post_list'
    paginate_by = 1

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(DetailView):
    modle = Post
    #
    # def get_queryset(self):
    #     return Post.objects.all()





