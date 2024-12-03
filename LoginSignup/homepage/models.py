from django.db import models
from django.contrib.auth.models import User
from .forms import CommentForm

# Prgrmr: Alimurung
# Create your models here.

# FOR CATEGORIES IN DATABASE
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

    artwork = models.ImageField(null=False, blank=False, upload_to='artmedia/')
    description = models.TextField()
    likes = models.ManyToManyField(User, related_name='artwork_post')

    @property
    def image_url(self):
        try:
            url = self.artwork.url
        except:
            url = ''
        return url
    
    def __str__(self):
        return self.description
    
    def total_likes(self):
        return self.likes.count()
    

# FOR THE COMMENT SECTION
class Comments(models.Model):
    artwork_post = models.ForeignKey(
        Artwork, on_delete=models.CASCADE, null=True, blank=True
    ) # get post
    comment_user = models.ForeignKey(
        User, on_delete=models.CASCADE
    ) # record user's name
    comment_image = models.ImageField(null=False, blank=False, upload_to='commentmedia/')  # Image upload field
    comment_text = models.TextField()  # Text for the comment
    date_added = models.DateTimeField(auto_now_add=True)  # Auto-add date when the comment is created
    
    @property
    def image_url(self):
        try:
            url = self.comment_image.url  # Fix: Get URL of the uploaded image
        except:
            url = ''
        return url

    def __str__(self):
        return self.comment_text[:50]  # Return the first 50 characters of the comment text