from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from subscriptions.models import Subscription
from marketplace.models import Product

from django.http import Http404

@login_required
def add_to_cart(request, item_id, item_type):
    """
    Add an item to the cart (either a product or subscription).
    :param item_id: The ID of the item (product or subscription)
    :param item_type: The type of the item ('product' or 'subscription')
    """
    # Check if the item type is valid
    if item_type not in ['product', 'subscription']:
        raise Http404("Invalid item type")

    # Get or initialize the cart in the session
    if 'cart' not in request.session:
        request.session['cart'] = {}

    cart = request.session['cart']

    # Handle adding a product
    if item_type == 'product':
        # Fetch the product
        product = get_object_or_404(Product, id=item_id)

        # Add or update the product in the cart
        if str(item_id) in cart:
            cart[str(item_id)]['quantity'] += 1
        else:
            cart[str(item_id)] = {
                'name': product.name,
                'price': float(product.price),  # Convert Decimal to float for serialization
                'quantity': 1,
            }

    # Handle adding a subscription
    elif item_type == 'subscription':
        # Fetch the subscription
        subscription = get_object_or_404(Subscription, id=item_id)

        # Add or update the subscription in the cart
        if str(item_id) in cart:
            cart[str(item_id)]['quantity'] += 1
        else:
            cart[str(item_id)] = {
                'name': subscription.name,
                'price': float(subscription.price),  # Convert Decimal to float for serialization
                'quantity': 1,
            }

    # Save the cart back to the session
    request.session['cart'] = cart
    request.session.modified = True

    # Redirect back to the previous page (marketplace product list or subscription list)
    if item_type == 'product':
        return redirect('marketplace:product_list')
    elif item_type == 'subscription':
        return redirect('subscriptions:subscription_list')


@login_required
def view_cart(request):
    # Get the user's cart
    cart = Cart.objects.filter(user=request.user).first()
    
    if cart:
        cart_items = CartItem.objects.filter(cart=cart)
    else:
        cart_items = []

    return render(request, 'marketplace/cart.html', {'cart_items': cart_items})
from decimal import Decimal

@login_required
def cart_detail(request):
    # Retrieve the cart from session and ensure it defaults to a dictionary
    cart = request.session.get('cart', {})

    # Ensure cart is a dictionary, not a list
    if not isinstance(cart, dict):
        cart = {}

    cart_items = []
    total_price = Decimal('0.00')  # Use Decimal for precise calculations
    subscription_items = []  # List to hold subscriptions in the cart
    total_subscription_price = Decimal('0.00')  # Total price for subscriptions

    # Iterate over the cart to separate products and subscriptions
    for product_id, item in cart.items():
        if 'subscription_id' in item:  # This item is a subscription
            subscription = get_object_or_404(Subscription, id=item['subscription_id'])
            total_item_price = Decimal(item['quantity']) * Decimal(item['price'])
            subscription_items.append({
                'subscription': subscription,
                'quantity': item['quantity'],
                'price': Decimal(item['price']),
                'total_item_price': total_item_price
            })
            total_subscription_price += total_item_price
        else:  # This item is a product
            product = get_object_or_404(Product, id=product_id)
            total_item_price = Decimal(item['quantity']) * Decimal(item['price'])
            cart_items.append({
                'product': product,
                'quantity': item['quantity'],
                'price': Decimal(item['price']),  # Restore Decimal for display
                'total_item_price': total_item_price
            })
            total_price += total_item_price

    # Total price will include both products and subscriptions
    grand_total = total_price + total_subscription_price

    return render(request, 'cart/cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'subscription_items': subscription_items,
        'total_subscription_price': total_subscription_price,
        'grand_total': grand_total
    })

def clear_session(request):
    request.session.flush()
    return redirect('marketplace:product_list')

@login_required
def remove_from_cart(request, product_id):
    # Retrieve the cart from session
    cart = request.session.get('cart', {})

    # Remove the product from the cart if it exists
    if str(product_id) in cart:
        del cart[str(product_id)]

    # Save the updated cart back to the session
    request.session['cart'] = cart

    # Redirect to the cart details page
    return redirect('cart:cart_detail')
# cart/views.py
from django.shortcuts import render, get_object_or_404, redirect
from subscriptions.models import Subscription  # Import Subscription model
from .models import Cart  # Assuming you have a Cart model

@login_required
def checkout(request):
    # Check if the user is checking out a subscription
    subscription_id = request.GET.get('subscription_id')
    if subscription_id:
        subscription = get_object_or_404(Subscription, id=subscription_id)
        return render(request, 'cart/checkout.html', {'subscription': subscription, 'is_subscription': True})

    # Otherwise, proceed with the cart checkout
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart:cart_detail')

    return render(request, 'cart/checkout.html', {'cart': cart, 'is_subscription': False})

@login_required
def place_order(request, subscription_id):
    # Fetch the subscription
    subscription = get_object_or_404(Subscription, id=subscription_id)

    if request.method == 'POST':
        # Logic to place the order, such as adding the subscription to the cart
        cart_item = Cart.objects.create(user=request.user, subscription=subscription)
        return redirect('cart:view_cart')  # Redirect to cart or another page

    return render(request, 'cart/place_order.html', {'subscription': subscription})