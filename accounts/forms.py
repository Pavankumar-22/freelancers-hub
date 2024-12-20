from django import forms
from django.contrib.auth.models import User
from .models import UserProfile  # Assuming you have a UserProfile model for user details

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Include any other fields you want to allow the user to update

class UserProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']  # Assuming profile_picture is part of the UserProfile model
