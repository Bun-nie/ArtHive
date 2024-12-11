from django import forms
from .models import Comment, Artwork


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_body', 'comment_image']
        widgets = {
            'comment_body': forms.Textarea(
                attrs={
                    'class': 'input-field',
                    'placeholder': 'Enter a comment',
                    'rows': 1,
                }
            ),
            'comment_image': forms.ClearableFileInput(
                attrs={
                    'class': 'image-field',
                    'placeholder': 'Add Image',
                }
            )
        }

    # Explicitly mark comment_image as optional if not handled at the model level
    comment_image = forms.ImageField(required=False)

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['artName', 'description', 'artwork']
        widgets = {
            'artName': forms.Textarea(
                attrs={
                    'class': 'input-field',
                    'placeholder': 'Enter new Artname',
                    'rows': 1,
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'input-field',
                    'placeholder': 'Enter new Description',
                    'rows': 3,
                    'cols': 20,
                }
            ),
            'artwork': forms.ClearableFileInput(
                attrs={
                    'class': 'image-field',
                    'placeholder': 'Add Image',
                }
            )
        }

