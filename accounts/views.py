from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Login view
# Login view
def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome {user.username}!")  # Optional: Add welcome message
            return redirect('home:dashboard')  # Ensure 'dashboard' is the correct URL name
        else:
            print('form not valid')
    return render(request, 'accounts/login.html', {'form': form})

# Signup view

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('accounts:login')
        else:
            messages.error(request, "There was an error with your registration.")
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

# Logout view (using Django's built-in LogoutView)
def logout_view(request):
    logout(request)  # Logs out the user
    messages.success(request, "You have successfully logged out.")  # Success message
    return redirect('home:dashboard') # Redirect to home after logout

def dashboard_view(request):
    return render(request, 'home:dashboard.html')

# Profile view (only accessible to logged-in users)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserProfilePictureForm
from .models import UserProfile

@login_required
def profile_view(request):
    # Ensure the user has a profile
    if not hasattr(request.user, 'userprofile'):
        UserProfile.objects.create(user=request.user)

    user_form = UserProfileForm(instance=request.user)
    profile_form = UserProfilePictureForm(instance=request.user.userprofile)

    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })



@login_required
def edit_profile(request):
    if request.method == 'POST':
        # Handle form submission for profile editing
        user_form = UserProfileForm(request.POST, instance=request.user)
        profile_form = UserProfilePictureForm(request.POST, request.FILES, instance=request.user.userprofile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # Save the updated user info
            profile_form.save()  # Save the updated profile picture
            return redirect('accounts:profile')  # Redirect back to the profile page
    
    else:
        # Prepopulate the forms with current data
        user_form = UserProfileForm(instance=request.user)
        profile_form = UserProfilePictureForm(instance=request.user.userprofile)

    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


# @login_required
# def update_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Save the profile picture and associate it with the logged-in user
#             profile = form.save(commit=False)
#             profile.user = request.user  # Link the profile with the current user
#             profile.save()
#             return redirect('profile')  # Redirect to profile page after saving

#     else:
#         form = ProfileForm()

#     return render(request, 'accounts/update_profile.html', {'form': form})