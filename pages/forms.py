from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=40, label='Your Name')
    email = forms.EmailField(required=False, label='Your Email address')
    subject = forms.CharField(max_length=60)
    message = forms.CharField(widget=forms.Textarea)