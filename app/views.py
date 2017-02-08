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
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect, HttpResponseForbidden, HttpResponseBadRequest
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import routers, serializers, viewsets, generics, views, versioning, pagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from drf_multiple_model.views import MultipleModelAPIView

from .models import *
from .serializers import *

logger = logging.getLogger(__name__)


@require_http_methods(['GET', 'POST'])
@login_required(login_url="/admin/login")
def index(request):
    context = json.dumps({})
    status = 200
    return HttpResponse(context, content_type=u"application/json", status=status)


class ExampleAPIView(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
    search_fields = ('title',)
    filter_fields = ('title', 'ctime', 'mtime',)
    ordering_fields = ('ctime', 'mtime',)
    # versioning_class = versioning.NamespaceVersioning
    permission_classes = (AllowAny,)