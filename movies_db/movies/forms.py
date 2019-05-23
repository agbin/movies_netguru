from django import forms


class SubmitMovie(forms.Form):
    title = forms.CharField()