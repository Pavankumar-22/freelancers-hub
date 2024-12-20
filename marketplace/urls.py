from django.urls import path
from . import views

app_name = 'marketplace'

urlpatterns = [
    path('', views.marketplace_home, name='home'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('products/', views.product_list, name='product_list'),
    path('categories/', views.product_categories, name='categories'),
    path('bundled-offers/', views.bundled_offers, name='bundled_offers'),
    path('success-stories/', views.freelancer_stories, name='stories'),
    path('consultation/', views.virtual_consultation, name='consultation'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]
