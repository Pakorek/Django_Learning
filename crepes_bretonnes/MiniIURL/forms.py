from django import forms
from .models import MiniURL


class URLGenForm(forms.ModelForm):
    class Meta:
        model = MiniURL
        fields = ('url', 'created_by')
