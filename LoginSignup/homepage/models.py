from django.db import models
from django.contrib.auth.models import User

# Prgrmr: Alimurung
# Create your models here.

class Category(models.Model):
    title_name_single = 'Category'
    title_name_multiple = 'Categories'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
    
    # this is for the photos of the artworks
class Artwork(models.Model):
    title_name_single = 'Artwork'
    title_name_multiple = 'Artworks'

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )

    artwork = models.ImageField(null=False, blank=False)
    description = models.TextField()

    @property
    def image_url(self):
        try:
            url = self.image_url
        except:
            url = ''
        return url
    
    def __str__(self):
        return self.description