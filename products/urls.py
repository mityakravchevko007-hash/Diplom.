from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<int:category_id>/', views.product_list, name='product_by_category'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add-to-favourites/<int:product_id>/', views.add_to_favourites, name='add_to_favourites'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]