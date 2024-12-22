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
    # Ensure the item_type is either 'product' or 'subscription'
    if item_type not in ['product', 'subscription']:
        raise Http404("Invalid item type")

    # Initialize the cart if it doesn't exist
    if 'cart' not in request.session:
        request.session['cart'] = {}

    cart = request.session['cart']

    # Handle adding a product to the cart
    if item_type == 'product':
        product = get_object_or_404(Product, id=item_id)
        # Use a composite key of item_type and item_id to ensure unique entries
        cart_key = f"product_{item_id}"
        if cart_key in cart:
            cart[cart_key]['quantity'] += 1
        else:
            cart[cart_key] = {
                'name': product.name,
                'price': float(product.price),  # Convert Decimal to float for serialization
                'quantity': 1,
                'type': 'product',
            }

    # Handle adding a subscription to the cart
    elif item_type == 'subscription':
        subscription = get_object_or_404(Subscription, id=item_id)
        # Use a composite key of item_type and item_id to ensure unique entries
        cart_key = f"subscription_{item_id}"
        if cart_key in cart:
            cart[cart_key]['quantity'] += 1
        else:
            cart[cart_key] = {
                'name': subscription.name,
                'price': float(subscription.price),  # Convert Decimal to float for serialization
                'quantity': 1,
                'type': 'subscription',
            }

    # Save the updated cart to session
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
    for cart_key, item in cart.items():
        if cart_key.startswith("subscription_"):  # This item is a subscription
            subscription_id = cart_key.split('_')[1]  # Extract subscription ID from the key
            subscription = get_object_or_404(Subscription, id=subscription_id)
            total_item_price = Decimal(item['quantity']) * Decimal(item['price'])
            subscription_items.append({
                'subscription': subscription,
                'quantity': item['quantity'],
                'price': Decimal(item['price']),
                'total_item_price': total_item_price
            })
            total_subscription_price += total_item_price
        elif cart_key.startswith("product_"):  # This item is a product
            product_id = cart_key.split('_')[1]  # Extract product ID from the key
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

@login_required
def remove_from_cart(request, item_id, item_type):
    # Retrieve the cart from the session
    cart = request.session.get('cart', {})

    # Construct the key based on item type (product or subscription)
    if item_type == 'product':
        cart_key = f"product_{item_id}"
    elif item_type == 'subscription':
        cart_key = f"subscription_{item_id}"
    else:
        raise Http404("Invalid item type")

    # Check if the item exists and remove it
    if cart_key in cart:
        del cart[cart_key]
        print(f"Removed {cart_key} from cart")

    # Save the updated cart back to session
    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart:cart_detail')




@login_required
def place_order(request, subscription_id):
    # Fetch the subscription
    subscription = get_object_or_404(Subscription, id=subscription_id)

    if request.method == 'POST':
        # Logic to place the order, such as adding the subscription to the cart
        cart_item = Cart.objects.create(user=request.user, subscription=subscription)
        return redirect('cart:view_cart')  # Redirect to cart or another page

    return render(request, 'cart/place_order.html', {'subscription': subscription})

@login_required
def checkout(request):
    cart = request.session.get('cart', {})

    if not cart or not any(item.get('quantity') for item in cart.values()):
        return redirect('cart:cart_detail')

    # Calculate total price and shipping cost
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    shipping_cost = cart.get('shipping_cost', 0)
    grand_total = total_price + shipping_cost

    # Add the total price for each item to the cart
    for item in cart.values():
        item['total_item_price'] = item['price'] * item['quantity']

    return render(request, 'cart/checkout.html', {
        'cart': cart,
        'total_price': total_price,
        'shipping_cost': shipping_cost,
        'grand_total': grand_total,
        'is_subscription': False
    })
