from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
        

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password',)
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text',)