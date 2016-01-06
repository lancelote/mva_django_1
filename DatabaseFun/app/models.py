from django.db import models


class Artist(models.Model):

    name = models.CharField(verbose_name='artist', max_length=50)
    year_formed = models.PositiveIntegerField()


class Album(models.Model):

    name = models.CharField(verbose_name='album', max_length=50)
    artist = models.ForeignKey(Artist)
