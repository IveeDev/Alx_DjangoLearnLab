from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Post, Tag
from taggit.forms import TagField

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
    



class PostForm(forms.ModelForm):
    tags = TagField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']