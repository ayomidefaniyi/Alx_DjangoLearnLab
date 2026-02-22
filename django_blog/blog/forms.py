from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag


# ----------------------
# Custom Registration Form
# ----------------------
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# ----------------------
# Profile Update Form
# ----------------------
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


# ----------------------
# Post Form (UPDATED WITH TAGS)
# ----------------------
class PostForm(forms.ModelForm):

    # 👇 This allows selecting multiple tags
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


# ----------------------
# Comment Form
# ----------------------
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']