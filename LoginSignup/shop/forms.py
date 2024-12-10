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

    shop_category = forms.ModelChoiceField(
        queryset=ShopCategory.objects.all(),  # Fetch all categories
        empty_label="Select a category...",  # Placeholder text
        widget=forms.Select(
            attrs={
                'class': 'input-field',
                'id': 'shop_category_id',
                'style': 'width: 490px; color: black;',
            }
        ),
    )

    class Meta:
        model = Product
        fields = ['name','price','description','image', 'shop_category']
        widgets = {
            'name': forms.Textarea(
                attrs={
                    'class': 'input-field',
                    'placeholder': 'Name of Listing',
                    'rows': 1
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class': 'input-field',
                    'placeholder': 'Price'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'input-field',
                    'placeholder': 'Product Description',
                    'rows': 4
                }
            ),
            'image': forms.ClearableFileInput(attrs={'class': 'image-field'}),
        }