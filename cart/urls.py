from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    # path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_cart/<int:item_id>/<str:item_type>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove_from_cart/<int:item_id>/<str:item_type>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('place-order/<int:subscription_id>/', views.place_order, name='place_order'),
]
