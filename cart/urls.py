from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart_view, name='cart'),
    path('remove/<int:item_id>/',
views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:item_id>/<str:action>/',
views.update_quantity,
name='update_quantity'),
    path('checkout/',
views.checkout_view,
name='checkout'),
    path('create-order/', views.create_order, name='create_order'),
    path('success/', views.order_success, name='order_success'),
    path('my-orders/',
views.my_orders, name='my_orders'),
    path('delete-order/<int:order_id>/',
views.delete_order, name='delete_order'),
]