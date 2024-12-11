from django import forms
from .models import Comment

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
