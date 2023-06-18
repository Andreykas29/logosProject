from django import forms
from shop.models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {
            'title': forms.TextInput(attrs={'class': ' gen_cl title'}),
            'description': forms.TextInput(attrs={'class': 'gen_cl description'}),
            'price': forms.TextInput(attrs={'class': 'gen_cl price'}),
            'image': forms.FileInput(attrs={'class': 'gen_cl image'}),
            'product_kind': forms.TextInput(attrs={'class': 'gen_cl product_kind'}),
        }