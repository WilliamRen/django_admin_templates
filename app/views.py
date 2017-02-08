# -*- coding:utf-8 -*-
import json
import logging
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Avg, Count, F, Q
from django.contrib import messages
from django.views.decorators.http import *
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect, HttpResponseForbidden, HttpResponseBadRequest


logger = logging.getLogger(__name__)


@require_http_methods(['GET', 'POST'])
@login_required(login_url="/admin/login")
def index(request):
    context = json.dumps({})
    status = 200
    return HttpResponse(context, content_type=u"application/json", status=status)