from django.urls import path
from main.views import show_main, create_product, show_product, show_xml,show_json,show_json_by_id,show_xml_by_id, register,login_user,logout_user, edit_product, delete_product, create_product_ajax, edit_product_ajax, delete_product_ajax, register_ajax, login_ajax, logout_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product,name='create_product'),
    path('create-product-ajax/', create_product_ajax,name='create_product_ajax'),
    path('product/<str:id>/', show_product,name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('login/', login_user, name='login'),
    path('login-ajax/', login_ajax, name='login_ajax'),
    path('logout/', logout_user, name='logout'),
    path('logout-ajax/', logout_ajax, name='logout_ajax'),
    path('product/<str:id>/edit', edit_product,name='edit_product'),
    path('product/<str:id>/edit-ajax/', edit_product_ajax,name='edit_product_ajax'),
    path('product/<str:id>/delete', delete_product,name='delete_product'),
    path('product/<str:id>/delete-ajax/', delete_product_ajax,name='delete_product_ajax'),
]