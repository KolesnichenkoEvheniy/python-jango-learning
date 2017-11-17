# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Album

# Create your views here.
def index(request):
    albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'albums': albums
    }
    return HttpResponse(template.render(context, request))

def detail(request, album_id):
    return HttpResponse("<h2>Title "+album_id+"</h2>")