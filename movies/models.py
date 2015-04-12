# -*- coding: utf-8 -*-
from django.db import models
from people.models import Person
from genre.models import Genre
from django.core import urlresolvers


class Language(models.Model):
    name = models.CharField(max_length=30, verbose_name='Język')

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Język'
        verbose_name_plural = 'Języki'


VOTE_GRADES = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
)


LANGUAGE = (
    ('PL', 'Polski'),
    ('EN', 'English'),
)


class Country(models.Model):
    name = models.CharField(max_length=30, verbose_name='Kraj')

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Kraj'
        verbose_name_plural = 'Kraje'


class Movie(models.Model):
    title = models.CharField(max_length=30, verbose_name='Tytuł')
    year = models.IntegerField(max_length=4, blank=False, null=False, verbose_name='Rok')
    language = models.ForeignKey(Language, blank=True, null=True, verbose_name='Język')
    genre = models.ManyToManyField(Genre, blank=True, null=True, verbose_name='Gatunek')
    country = models.ManyToManyField(Country, blank=True, null=True, verbose_name='Kraj')

    def __unicode__(self):
        return unicode(self.title)

    @property
    def get_admin_url(self):
        return urlresolvers.reverse("admin:%s_%s_change" %
        (self._meta.app_label, self._meta.module_name), args=(self.pk,))

    def get_url(self):
        return u"/%s/%s/%s" % (self._meta.app_label, self._meta.module_name, self.pk)

    class Meta:
        ordering = ['title']
        verbose_name = 'Film'
        verbose_name_plural = 'Filmy'


class Role(models.Model):
    role = models.CharField(max_length=30, verbose_name='Rola')

    def __unicode__(self):
        return unicode(self.role)

    class Meta:
        ordering = ['role']
        verbose_name = 'Rola'
        verbose_name_plural = 'Role'


class MovieRole(models.Model):
    role = models.ForeignKey(Role)
    people = models.ManyToManyField(Person, blank=True, null=True, verbose_name='Osoba')
    movie = models.ForeignKey(Movie, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.role)

    class Meta:
        ordering = ['role']
        verbose_name = 'Rola'
        verbose_name_plural = 'Role'


class Description(models.Model):
    movie = models.ForeignKey(Movie)
    description = models.TextField(verbose_name='Opis filmu')
    language = models.CharField(max_length=2, choices=LANGUAGE, default='PL', verbose_name='Język')

    def __unicode__(self):
        return u"%s %s %s" % (self.movie.title, self.movie.year, self.language)

    class Meta:
        verbose_name = 'Opis filmu'
        verbose_name_plural = 'Opisy filmów'
