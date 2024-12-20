from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, BundledOffer, SuccessStory, ConsultationService

# Home page for the marketplace
def marketplace_home(request):
    return render(request, 'marketplace/home.html', {'title': 'Marketplace'})

# Product categories view (now pulling data from the database)
def product_categories(request):
    categories = Category.objects.all()  # Fetch all categories from the database
    return render(request, 'marketplace/categories.html', {'categories': categories})

# Bundled offers page (now pulling data from the database)
def bundled_offers(request):
    offers = BundledOffer.objects.all()  # Fetch all bundled offers from the database
    return render(request, 'marketplace/bundled_offers.html', {'offers': offers})

# Freelancer Success Stories (now pulling data from the database)
def freelancer_stories(request):
    stories = SuccessStory.objects.all()  # Fetch all success stories from the database
    return render(request, 'marketplace/stories.html', {'stories': stories})

# View for virtual consultation services (now pulling data from the database)
def virtual_consultation(request):
    consultations = ConsultationService.objects.all()  # Fetch all consultations from the database
    return render(request, 'marketplace/consultation.html', {'consultations': consultations})

# Product list view (no changes needed, just fetching products from the database)
def product_list(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'marketplace/product_list.html', {'products': products})

# Product detail view (no changes needed, just retrieving product by id)
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'marketplace/product_detail.html', {'product': product})

# Add to cart functionality (no changes needed)
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Initialize the cart in the session as a dictionary if it doesn't exist
    if 'cart' not in request.session:
        request.session['cart'] = {}

    cart = request.session['cart']

    # Add product to the cart or update its quantity
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),  # Convert Decimal to float for JSON serialization
            'quantity': 1,
        }

    # Save the updated cart back into the session
    request.session['cart'] = cart
    request.session.modified = True  # Mark session as modified to ensure changes are saved

    return redirect('marketplace:product_list')  # Redirect to the product list page