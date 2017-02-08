# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ExampleConfig(AppConfig):
    name = 'example'
    label = 'example'
    verbose_name = _("example")
