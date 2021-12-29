from django.forms import ModelForm
from .models import Critics


class CriticsForm(ModelForm):
    class Meta:
        model = Critics
        fields = ['title', 'description']