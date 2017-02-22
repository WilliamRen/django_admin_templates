# -*- coding: utf-8 -*-
import os
import json
from django.contrib import admin
from django.contrib.admin import sites
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Avg, Count, F, Q
from django.db.models.fields import BLANK_CHOICE_DASH
from django.contrib.admin.models import LogEntry, DELETION
from django.contrib.sessions.models import Session
from django.utils.html import escape
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.admin.sites import AdminSite
from django.utils.module_loading import autodiscover_modules


__all__ = ["AdminSitePlus", "site", ]


class AdminSitePlus(AdminSite):
    site_title = _('site title')

    # Text to put in each page's <h1>.
    site_header = _('site header')

    # Text to put at the top of the admin index page.
    index_title = _('index title')

    # URL for the "View site" link at the top of each admin page.
    site_url = '/admin/'


site = AdminSitePlus()
