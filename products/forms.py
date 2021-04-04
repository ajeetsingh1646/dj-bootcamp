from django import forms

from .models import Product
# class ProductForm(forms.Form):
#     title = forms.CharField()
    
class ProductModelForm(forms.ModelForm):
    #title = forms.CharField()  # to override meta title
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'inventory'
        ]
    
    # data validations
    def clean_title(self):
        data = self.cleaned_data.get('title')
        if len(data)<4:
            raise forms.ValidationError("Title is not long enough. Enter a VALID title.")
        return data
    
    def clean_content(self):
        data = self.cleaned_data.get('content')
        if len(data) < 5:
            raise forms.ValidationError("Content should be minimum 5 characters.")
        return data

    def clean_prices(self):
        data = self.cleaned_data.get('price')
        if data < 10.00:
            raise forms.ValidationError("Price of the product should be greater than 10 rupees.")
        return data

    def clean_inventory(self):
        data = self.cleaned_data.get('inventory')
        if data < 0:
            raise forms.ValidatiionError("Number of products can't be negative.")
        return data


