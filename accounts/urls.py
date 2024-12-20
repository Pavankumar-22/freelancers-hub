from django.urls import path
from .views import *

app_name = 'accounts'  # Register the namespace here

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('dashboard/', dashboard_view, name='dashboard'),
    # path('profile/update/', update_profile, name='update_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
