from django import forms
from django.forms import ModelForm

from .models import Quote

class QuoteForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Quote #the model on which to base our form.
        #these are the fields from models that we want to look in our form.
        fields = [
            'name', 'position', 'company', 'address',
            'phone', 'email', 'web', 'description',
            'sitestatus', 'priority', 'jobfile',
        ]