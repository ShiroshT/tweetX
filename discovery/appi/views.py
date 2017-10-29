# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Context
from django.http import HttpResponseRedirect, HttpResponse
from appi.models import CatogoryType

# Create your views here.


def index(request):
    category_list = CatogoryType.objects.all()
    context_dict = {'categories': category_list}

    return render(request, 'appi/index.html', context_dict)