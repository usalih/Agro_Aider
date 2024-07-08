from django import forms
from .models import Comment, Reply

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content' : forms.Textarea(attrs={'placeholder': 'Add comment ...'}),
        }
        labels = {
            'content': '',
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
