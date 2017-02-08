# -*- coding:utf-8 -*-
from rest_framework import serializers, viewsets
from django.contrib.auth.models import User, Group

from .models import *


class ExampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Example
        fields = ('title', 'ctime', 'mtime',)

