from django import forms

class SreachWord(forms.Form):
    query = forms.CharField(max_length=30)
    