# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(max_length=1024)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias')
    body = models.CharField(max_length=4096)
    author = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_created=True, auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'post'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board:post_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_create_date()

    def get_next_post(self):
        return self.get_next_by_create_date()










