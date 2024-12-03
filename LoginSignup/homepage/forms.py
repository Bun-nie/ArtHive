from django import forms

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say something...'
        })
    )

    class Meta:
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        from homepage.models import Comments  # Import inside the method
        self.Meta.model = Comments
        super().__init__(*args, **kwargs)
