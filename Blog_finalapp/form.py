from .models import Blog_post, log
from django import forms


class Blog_form(forms.ModelForm):
    class Meta:
        model = Blog_post
        fields = '__all__'


class log_form(forms.ModelForm):
    class Meta:
        model = log
        fields = '__all__'