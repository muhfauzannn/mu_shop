from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from main.forms import ProductForm

# Create your views here.
def show_main(request):
    # Get all products from database
    products = Product.objects.all()
    
    # Get featured products
    featured_products = Product.objects.filter(is_featured=True)
    
    # Get products by category
    jerseys = Product.objects.filter(category='jersey')
    accessories = Product.objects.filter(category='accessories')
    
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
        
        
        # Categories for navigation
        'categories': Product.CATEGORY_CHOICES,
        
        # Shop info
        'currency': 'IDR',
        'shop_slogan': 'Glory Glory Man United!'
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if(form.is_valid() and request.method == 'POST'):
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product.html", context)
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context={
        'product': product
    }
    return render(request,"show_product.html", context)
    
