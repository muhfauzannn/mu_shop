from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from main.forms import ProductForm
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'
    
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

@login_required(login_url='/login')
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
@csrf_exempt
def create_product_ajax(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            
            # Create form with the data
            form = ProductForm(data)
            
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user
                product.save()
                
                return JsonResponse({
                    'success': True,
                    'message': 'Product created successfully!',
                    'product': {
                        'id': product.id,
                        'name': product.name,
                        'price': str(product.price),
                        'category': product.category
                    }
                })
            else:
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
                
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    
    return JsonResponse({'success': False, 'message': 'Only POST method allowed'})

@login_required(login_url='/login')
def show_product(request, id):
    context = {
        'product': {'id': id}  # Pass only the ID for AJAX loading
    }
    return render(request, "show_product.html", context)
    
def show_xml(request):
    products = Product.objects.all()
    data = serializers.serialize('xml', products)
    return HttpResponse(data, content_type='application/xml')

def show_json(request):
    products = Product.objects.all()
    data = [{
        'id': product.id,
        'name': product.name,
        'price': str(product.price),
        'description': product.description,
        'thumbnail': product.thumbnail,
        'category': product.category,
        'is_featured': product.is_featured,
        'created_at': product.created_at.isoformat() if product.created_at else None,
        'updated_at': product.updated_at.isoformat() if product.updated_at else None,
        'user_id': product.user_id,
        } for product in products]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
#    try:
#        product_item = Product.objects.get(pk=product_id)
#        json_data = serializers.serialize("json", [product_item])
#        return HttpResponse(json_data, content_type="application/json")
#    except Product.DoesNotExist:
#        return HttpResponse(status=404)
    try:
        product_item = Product.objects.get(pk=product_id)
        data = {
            'id': product_item.id,
            'name': product_item.name,
            'price': str(product_item.price),
            'description': product_item.description,
            'thumbnail': product_item.thumbnail,
            'category': product_item.category,
            'is_featured': product_item.is_featured,
            'created_at': product_item.created_at.isoformat() if product_item.created_at else None,
            'updated_at': product_item.updated_at.isoformat() if product_item.updated_at else None,
            'user_id': product_item.user.username if product_item.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
   
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

@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form = UserCreationForm(data)
            
            if form.is_valid():
                user = form.save()
                return JsonResponse({
                    'success': True,
                    'message': 'Account created successfully! You can now login.',
                    'username': user.username
                })
            else:
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
                
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    
    return JsonResponse({'success': False, 'message': 'Only POST method allowed'})

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

@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form = AuthenticationForm(data=data)
            
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                
                return JsonResponse({
                    'success': True,
                    'message': f'Welcome back, {user.username}!',
                    'username': user.username,
                    'redirect_url': reverse("main:show_main")
                })
            else:
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
                
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    
    return JsonResponse({'success': False, 'message': 'Only POST method allowed'})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def logout_ajax(request):
    if request.method == 'POST':
        try:
            logout(request)
            return JsonResponse({
                'success': True,
                'message': 'You have been successfully logged out.',
                'redirect_url': reverse('main:login')
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    
    return JsonResponse({'success': False, 'message': 'Only POST method allowed'})

@login_required(login_url='/login')
def edit_product(request,id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    context = {
        'form': form,
        'product': product
    }
    return render(request,'edit_product.html', context)

@login_required(login_url='/login')
@csrf_exempt
def edit_product_ajax(request, id):
    if request.method == 'POST':
        try:
            product = get_object_or_404(Product, pk=id)
            
            # Parse JSON data from request body
            data = json.loads(request.body)
            
            # Create form with the data and existing product instance
            form = ProductForm(data, instance=product)
            
            if form.is_valid():
                updated_product = form.save()
                
                return JsonResponse({
                    'success': True,
                    'message': 'Product updated successfully!',
                    'product': {
                        'id': updated_product.id,
                        'name': updated_product.name,
                        'price': str(updated_product.price),
                        'category': updated_product.category
                    }
                })
            else:
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
                
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    
    return JsonResponse({'success': False, 'message': 'Only POST method allowed'})

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('main:show_main')

@login_required(login_url='/login')
@csrf_exempt
def delete_product_ajax(request, id):
    if request.method == 'POST':
        try:
            product = get_object_or_404(Product, pk=id)
            
            # Check if the current user is the owner of the product
            if product.user != request.user:
                return JsonResponse({
                    'success': False,
                    'message': 'You are not authorized to delete this product.'
                }, status=403)
            
            product_name = product.name
            product.delete()
            
            return JsonResponse({
                'success': True,
                'message': f'Product "{product_name}" has been deleted successfully!'
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    
    return JsonResponse({'success': False, 'message': 'Only POST method allowed'})