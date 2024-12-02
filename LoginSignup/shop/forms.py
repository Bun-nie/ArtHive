from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    """
    class Meta:
        model = Product
        fields = ['name','price','digital','image']
        widgets = {
            'name': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter name of product here',
                    'rows': 4
                }
            ),
            'price': forms.TextInput(),
            'digital': forms.CheckboxInput(),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Product name',
            'price': 'Product price',
            'digital': 'Product digital',
        }