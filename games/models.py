from __future__ import unicode_literals

from random import shuffle
from django.db import models
from django.http import HttpResponseServerError, HttpResponseBadRequest

from teachmodern.users.models import User
from django.contrib.postgres.fields import JSONField


class GameSeed(models.Model):
    CODE_WORDS = 1
    GameTypes = (
        (CODE_WORDS, 'code words'),
    )

    name = models.CharField(max_length=200)
    game_type = models.IntegerField(choices=GameTypes, default=CODE_WORDS)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date last updated')
    deleted_at = models.DateTimeField(
        verbose_name='date soft deleted',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class CodeWordsSeed(GameSeed):
    words = JSONField()

    def get_words(self, cube_width=5):
        if isinstance(self.words, list):
            shuffle(self.words)
            return self.words[0:(cube_width * cube_width)]
        else:
            raise HttpResponseServerError
