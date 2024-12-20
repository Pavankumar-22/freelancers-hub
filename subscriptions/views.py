from django.shortcuts import render, redirect, get_object_or_404
from .models import Subscription
from django.contrib.auth.decorators import login_required

def subscription_list(request):
    categories = {
        'software_subscriptions': Subscription.objects.filter(category='Software'),
        'cloud_subscriptions': Subscription.objects.filter(category='Cloud'),
        'productivity_subscriptions': Subscription.objects.filter(category='Productivity'),
        'learning_subscriptions': Subscription.objects.filter(category='Learning'),
        'freelancing_subscriptions': Subscription.objects.filter(category='Freelancing'),
    }

    # Check if an Add to Cart action has been triggered
    if request.method == 'GET' and 'add_to_cart' in request.GET:
        subscription_id = request.GET.get('add_to_cart')
        subscription = get_object_or_404(Subscription, id=subscription_id)
        
        # Get the current cart from the session
        cart = request.session.get('cart', {})

        # If the subscription is already in the cart, increment the quantity
        if subscription_id in cart:
            cart[subscription_id]['quantity'] += 1
        else:
            # Add the subscription to the cart with an initial quantity of 1
            cart[subscription_id] = {
                'name': subscription.name,
                'price': subscription.price,
                'quantity': 1
            }

        # Save the updated cart back to the session
        request.session['cart'] = cart

        # Redirect back to the subscription list page to show the updated cart
        return redirect('subscriptions:subscription_list')

    # Render the subscription list page with categories
    return render(request, 'subscriptions/subscription_list.html', categories)
