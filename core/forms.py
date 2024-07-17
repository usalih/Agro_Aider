from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content','reply']
        widgets = {
            'content' : forms.Textarea(attrs={'placeholder': 'Add comment ...'}),
            'reply': forms.HiddenInput()
        }

