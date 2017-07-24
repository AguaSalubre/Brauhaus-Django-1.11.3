# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def brauhaus(request):
    context = {}
    template = 'brauhaus.html'
    return render(request,template,context)

def gaststaette(request):
    context = {}
    template = 'gaststaette.html'
    return render(request,template,context)

def veranstaltungen(request):
    context = {}
    template = 'veranstaltungen.html'
    return render(request,template,context)

def stammtische(request):
    context = {}
    template = 'stammtische.html'
    return render(request,template,context)

def mediathek(request):
    context = {}
    template = 'mediathek.html'
    return render(request,template,context)

def shop(request):
    context = {}
    template = 'shop.html'
    return render(request,template,context)


