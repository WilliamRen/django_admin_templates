# -*- coding:utf-8 -*-
from django.conf import settings
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.utils.urls import remove_query_param, replace_query_param


class APIPageNumberPagination(PageNumberPagination):
    # Client can control the page using this query parameter.
    page_query_param = settings.PAGE_QUERY_PARAM

    # Client can control the page size using this query parameter.
    # Default is 'None'. Set to eg 'page_size' to enable usage.
    page_size_query_param = settings.PAGE_SIZE_QUERY_PARAM

    # Set to an integer to limit the maximum page size the client may request.
    # Only relevant if 'page_size_query_param' has also been set.
    max_page_size = settings.MAX_PAGE_SIZE

    #display_page_controls = True

    def get_paginated_response(self, data):
        return Response({
            'meta': {
                'count': self.page.paginator.count,
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'html': self.to_html(),
                # 'context': self.get_html_context(),
                'version': self.request.version,
            },
            'results': data
        })

    def get_next_link(self):
        if not self.page.has_next():
            return None
        url = self.request.build_absolute_uri()
        page_number = self.page.next_page_number()
        return replace_query_param(url, self.page_query_param, page_number)

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        url = self.request.build_absolute_uri()
        page_number = self.page.previous_page_number()
        # if page_number == 1:
        #     return remove_query_param(url, self.page_query_param)
        return replace_query_param(url, self.page_query_param, page_number)
