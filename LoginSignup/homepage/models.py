from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Prgrmr: Alimurung
# Create your models here.

class Category(models.Model):
    title_name_single = 'Category'
    title_name_multiple = 'Categories'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    artName = models.CharField(default='Ana', max_length=100, null=False, blank=False)
    artwork = models.ImageField(null=False, blank=False, upload_to='artmedia/')
    description = models.TextField()

    @property
    def image_url(self):
        try:
            url = self.artwork.url
        except:
            url = ''
        return url
    
    def __str__(self):
        return self.description
    
# for comment section
class Comment(models.Model):
    comment_body = models.TextField(blank=True, null=True)
    date_create = models.DateField(auto_now_add=True)
    comment_image = models.ImageField(upload_to='commentmedia/', null=True, blank=True)
    # artwork_ref = models.ForeignKey(Artwork, on_delete=models.CASCADE) # reference to artwork above
    artwork_ref = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True) # reference to the user who made the comment

    # def __str__(self):
    #     return f"{self.user_ref.username} on {self.artwork_ref.artName}"
    def __str__(self):
        return f"{self.user.username} on {self.artwork_ref.artName}"