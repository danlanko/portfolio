from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name*','name':'name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email*','name':'email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone*','name':'email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message*','name':'email','rows':'7'}))