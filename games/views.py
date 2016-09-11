# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import GameSeed, CodeWordsSeed


class GameListView(LoginRequiredMixin, ListView):
    model = GameSeed
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'game_seed_list'

    def get_queryset(self):
        return GameSeed.objects.filter(owner=self.request.user).order_by('-created_at')


class GameDetailView(LoginRequiredMixin, DetailView):
    model = CodeWordsSeed
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
