# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Artykuly(models.Model):
    id = models.IntegerField(primary_key=True)
    kategoria = models.ForeignKey('Kategorie', models.DO_NOTHING)
    tytul = models.CharField(max_length=255)
    wersja_krotka = models.TextField(blank=True, null=True)
    wersja_dluga = models.TextField(blank=True, null=True)
    autor = models.CharField(max_length=200, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    slot1 = models.CharField(max_length=255, blank=True, null=True)
    slot2 = models.CharField(max_length=255, blank=True, null=True)
    slot3 = models.CharField(max_length=255, blank=True, null=True)
    slot4 = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)

    def publish(self):
        self.data = timezone.now()
        self.save()

    def __str__(self):
        return self.tytul

    class Meta:
        managed = False
        db_table = 'artykuly'


class Kategorie(models.Model):
    id = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length=250, blank=True, null=True)
    opis = models.TextField(blank=True, null=True)
    slot1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kategorie'
