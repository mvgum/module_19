from django.db import models
from django import forms


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=5, decimal_places=1)
    age =models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=5, decimal_places=1)
    size = models.DecimalField(max_digits=5, decimal_places=1)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ваше имя")

