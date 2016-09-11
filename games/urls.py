# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the GameListView
    url(
        regex=r'^$',
        view=views.GameListView.as_view(),
        name='index'
    ),
    # URL pattern for the GameDetailView
    url(
        regex=r'^(?P<pk>[0-9]+)/$',
        view=views.GameDetailView.as_view(),
        name='detail'
    ),
]
