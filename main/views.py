from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from main.forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

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
    
def show_xml(request):
    products = Product.objects.all()
    data = serializers.serialize('xml', products)
    return HttpResponse(data, content_type='application/xml')

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
   try:
       product_item = Product.objects.get(pk=product_id)
       json_data = serializers.serialize("json", [product_item])
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)