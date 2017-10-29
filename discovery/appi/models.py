# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CatogoryType(models.Model):
    name_of_catogory = models.CharField(max_length=40)
    type_of_catogory = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
