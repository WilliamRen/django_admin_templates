# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import *


class VideoForm(forms.ModelForm):

    class Meta:
        model = Example
        exclude = []
        widgets = {
            'video': forms.ClearableFileInput,
        }

    # class Media:
    #     css = {
    #         "all": [
    #             "css/bootstrap.css",
    #             "css/bootstrap-progressbar-2.3.2.css",
    #         ]
    #     }
    #     js = [
    #         'js/jquery.js',
    #         'js/bootstrap.js',
    #         'js/bootstrap-progressbar.js',
    #     ]
