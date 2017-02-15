# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import json
from django.contrib import admin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Avg, Count, F, Q
from django.db.models.fields import BLANK_CHOICE_DASH
from django.contrib.admin.models import LogEntry, DELETION
from django.contrib.sessions.models import Session
from django.utils.html import escape
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext, ugettext_lazy as _
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from .models import *


class ExampleResource(resources.ModelResource):
    class Meta:
        model = Example
        import_id_fields = ('id', )
        export_order = ('id', 'title', 'ctime', 'mtime')
        fields = ('id', 'title', 'ctime', 'mtime')


# @admin.register(Example)
class ExampleAdmin(ImportExportModelAdmin):
    resource_class = ExampleResource
    change_list_template = u"admin/import_export/change_list_import_export.html"
    fieldsets = [
        (None, {'fields': ['title', ]}),
    ]
    list_display = (
        "id",
        "title",
        "ctime",
        "mtime",
    )
    list_filter = (
        "ctime",
        "mtime",
    )
    search_fields = ('title', )
    ordering = ('ctime', 'mtime', )
    filter_horizontal = ()
    date_hierarchy = None
    list_per_page = 50

