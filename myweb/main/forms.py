from django import forms
from django.forms import ModelForm
from.models import Product
class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        widgets={
            "product_name": forms.TextInput(attrs={'class': 'form-control'}),
            "price": forms.NumberInput(attrs={'class': 'form-control'}),
            "location": forms.TextInput(attrs={'class': 'form-control'}),
        }

