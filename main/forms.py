from .models import ShortURL
from django import forms

class create_new_short_URL(forms.ModelForm):
    class Meta:
        model=ShortURL
        fields = {'original_URL'}

        widgets = {
            'original_url' :forms.TextInput(attrs={'class': 'form-control'})
        }
