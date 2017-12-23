from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class Travel(models.Model):
    destination = models.CharField(max_length=80)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '%s going to %s' % (self.user, self.destination)


class TravelForm(ModelForm):
    class Meta:
        model = Travel
        fields = ['destination', 'start_date', 'end_date']


class SearchForm(forms.Form):
    query = forms.CharField(label='Query', max_length=80)
