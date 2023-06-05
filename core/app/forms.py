from django import forms
from app.models import *
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','content','author_name')
