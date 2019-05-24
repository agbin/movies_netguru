from django import forms
from .models import Comment


class SubmitMovie(forms.Form):
    title = forms.CharField()


class CommentAddForm(forms.ModelForm):
    text = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control',
               'placeholder': 'Add Comment', }
    ))
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Name:'}))

    class Meta:
        model = Comment
        fields = ('name', 'text')