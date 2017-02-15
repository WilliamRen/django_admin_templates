# -*- coding: utf-8 -*-
import os
import re
import django
from django.db import models
from django.db.models.signals import post_save, post_delete, post_syncdb
from django.db.models.signals import class_prepared
from django.db.models import Avg, Count, F, Q
from django.contrib.auth.models import User, Group, Permission, ContentType
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth import get_user_model
from mongoengine import *


@python_2_unicode_compatible
class Example(models.Model):
    title = models.CharField(verbose_name=_("title"), max_length=200, blank=True, null=True, default="")
    ctime = models.DateTimeField(verbose_name=_("create time"), auto_now_add=True, )
    mtime = models.DateTimeField(verbose_name=_("update time"), auto_now=True, )

    def __str__(self):
        return u'%s' % self.title

    def save(self, *args, **kwargs):
        super(Example, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Example')
        verbose_name_plural = _('Example')
        ordering = ('ctime',)


class Choice(EmbeddedDocument):
    choice_text = StringField(max_length=200)
    votes = IntField(default=0)


class Poll(Document):
    question = StringField(max_length=200)
    pub_date = DateTimeField(help_text='date published')
    choices = ListField(EmbeddedDocumentField(Choice))

    meta = {
        'indexes': [
            'question',
            ('pub_date', '+question')
        ]
    }

