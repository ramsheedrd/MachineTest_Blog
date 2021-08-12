from django import forms
from .models import PostModel

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = [
            'heading',
            'tags',
            'category',
            'content'
        ]
        widgets = {'tags': forms.TextInput(attrs={'data-role': 'tagsinput'})}