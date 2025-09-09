from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    # Get all products from database
    products = Product.objects.all()
    
    # Get featured products
    featured_products = Product.objects.filter(is_featured=True)
    
    # Get products by category
    jerseys = Product.objects.filter(category='jersey')
    accessories = Product.objects.filter(category='accessories')
    
    # Count products
    total_products = Product.objects.count()
    featured_count = featured_products.count()
    
    context = {
        'app_name': 'Manchester Shop',
        'shop_description': 'Official Manchester United Merchandise Store',
        'name': 'Muhammad Fauzan',
        'npm': '2406496302',
        'class': 'E',
        
        # Product data
        'products': products,
        'featured_products': featured_products,
        'jerseys': jerseys,
        'accessories': accessories,
        
        # Statistics
        'total_products': total_products,
        'featured_count': featured_count,
        
        # Categories for navigation
        'categories': Product.CATEGORY_CHOICES,
        
        # Shop info
        'currency': 'IDR',
        'shop_slogan': 'Glory Glory Man United!'
    }

    return render(request, "main.html", context)
