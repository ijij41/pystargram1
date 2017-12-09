# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, get_object_or_404
from models import Photo
from forms import PhotoForm
from django.shortcuts import redirect
from pystargram import settings
from django.utils.encoding import smart_str
import mimetypes
from wsgiref.util import FileWrapper



# Create your views here.
@login_required
def logintest(request):
    return HttpResponseRedirect('http://yahoo.com')


def create(request):
    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return redirect(obj)

    ctx = {
        'form': form,
    }
    return render(request, 'edit.html', ctx)


def download(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    file_path = photo.image.path
    file_wrapper = FileWrapper(file(file_path, 'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype)
    response['Content-Disposition'] = 'attachment; filename=%s' % file_path
    return response



def detail(request, pk):
    # photo = Photo.objects.get(pk=pk)
    photo = get_object_or_404(Photo, pk=pk)
    # messages = (
    #     '<p>{pk}번 사진 보여줄게요!</p>'.format(pk=photo.pk),
    #     '<p>주소는 {url}</p>'.format(url=photo.image.url),
    #     '<p><img src="{url}" /></p>'.format(url=photo.image.url),
    # )
    # ctx={
    #     'messages':'\<p\>{pk}번 사진 보여줄게요!\</p\>'.format(pk=photo.pk)+"\n"+
    #     '<p>주소는 {url}</p>'.format(url=photo.image.url)+
    #     '<p><img src="{url}" /></p>'.format(url=photo.image.url)
    # }
    ctx = {
        'photo':photo,
    }

    return render(request, 'detail.html', ctx)
    # return HttpResponse('\n'.join(messages))





