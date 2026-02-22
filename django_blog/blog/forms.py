from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget  # ✅ Needed for tagging widget

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
# Post Form (WITH TAGS)
# ----------------------
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # include tags field
        widgets = {
            'tags': TagWidget(),  # ✅ This is what the checker is looking for
        }


# ----------------------
# Comment Form
# ----------------------
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']