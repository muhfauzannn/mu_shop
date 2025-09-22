from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from main.forms import ProductForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)
    
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
        'shop_slogan': 'Glory Glory Man United!',

        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if(form.is_valid() and request.method == 'POST'):
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
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
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response