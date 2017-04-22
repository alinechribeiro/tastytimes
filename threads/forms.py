from django import forms
from .models import Thread, Post


class ThreadForm(forms.ModelForm):
    name = forms.CharField(label="Thread name")
    ##That is not a required field. We want to see it on the form, but we don’t care if it’s not included, as it will be missing from our request.POST if it’s not checked.
    ##That way, we avoid any validation errors that might stop the process when all we want is to be able to tell whether or not is a poll! 
    is_a_poll = forms.BooleanField(label="Include a poll?", required=False)

    class Meta:
        model = Thread
        fields = ['name']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['comment']
