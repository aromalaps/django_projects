from .models import Songs
from django import forms

class SongForm(forms.ModelForm):
    class Meta:
        model=Songs
        fields='__all__'