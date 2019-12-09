from django import forms

from .models import product


class productForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ('product_name', 'desc', 'category', 'sub_category', 'price', 'image')