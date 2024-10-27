from django import forms
from .models import Shoe

class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ['name', 'brand', 'size', 'color', 'price']
