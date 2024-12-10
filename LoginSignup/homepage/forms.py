from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_body', 'comment_image']
        widgets = {
            'comment_body':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter a comment',
                }

            ),
            'comment_image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }

        labels = {
            'comment_body':'Comment_body',
            'comment_image':'Comment_image',
        }