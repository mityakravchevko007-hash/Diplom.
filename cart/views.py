from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product
from .models import Order


@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = sum(item.product.price * item.quantity for item in items)

    return render(request, 'cart.html', {
        'cart': cart,
        'items': items,
        'total': total
    })

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('cart')

@login_required
def update_quantity(request, item_id, action):
    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    if action == "increase":
        item.quantity += 1

    elif action == "decrease":
        if item.quantity > 1:
            item.quantity -= 1

    item.save()

    return redirect('cart')

@login_required
def checkout_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()

    total = sum(item.product.price * item.quantity for item in items)

    return render(request, 'checkout.html', {
        'cart': cart,
        'items': items,
        'total': total
    })

@login_required
def create_order(request):
    cart = Cart.objects.get(user=request.user)
    items = cart.items.all()

    if not items:
        return redirect('cart')

    order = Order.objects.create(user=request.user)

    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    items.delete()

    return redirect('order_success')

@login_required
def order_success(request):
    return render(request, 'order_success.html')

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'my_orders.html', {
        'orders': orders
    })

@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.delete()
    return redirect('my_orders')

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'products/product_detail.html', {'product': product})


def add_to_cart(request, product_id):
    return redirect('cart')