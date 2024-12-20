from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.service_list, name='service_list'),  # List all services
    path('<int:id>/', views.service_detail, name='detail'),  # Service detail page
]
