from django.db import models

from AppCafe import forms

class VariedadCafe(models.Model):

    nombre = models.CharField(max_length=40)
    marca  = models.CharField(max_length=40)
    precio = models.IntegerField()

class VariedadTe(models.Model):

    nombre = models.CharField(max_length=40)
    marca  = models.CharField(max_length=40)
    precio = models.IntegerField()

class VariedadGaseosa(models.Model):

    nombre = models.CharField(max_length=40)
    marca  = models.CharField(max_length=40)
    precio = models.IntegerField()

class Formscafe(forms.Form):

    nombre = forms.CharField(max_length=40)
    marca  = forms.CharField(max_length=40)
    precio = forms.IntegerField()