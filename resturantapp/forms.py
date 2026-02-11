from django import forms
from . models import *


class FoodUpload(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['category', 'name', 'description', 'price', 'image' ]

class CategoryUpload(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']