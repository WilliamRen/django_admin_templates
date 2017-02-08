# -*- coding:utf-8 -*-
from rest_framework import serializers, viewsets
from django.contrib.auth.models import User, Group

from .models import *


class DateTimeFieldWihTZ(serializers.DateTimeField):
    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeFieldWihTZ, self).to_representation(value)


class ExampleSerializer(serializers.HyperlinkedModelSerializer):
    ctime = DateTimeFieldWihTZ(format="%Y-%m-%d %H:%M:%S", read_only=True)
    mtime = DateTimeFieldWihTZ(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Example
        fields = ('title', 'ctime', 'mtime',)


