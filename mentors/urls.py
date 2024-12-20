# mentors/urls.py
from django.urls import path
from . import views

app_name = 'mentors'

urlpatterns = [
    path('', views.mentor_list, name='mentor_list'),
    path('<int:id>/', views.mentor_detail, name='mentor_detail'),
]
