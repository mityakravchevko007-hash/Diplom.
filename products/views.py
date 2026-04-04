from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.db.models import Q
from cart.models import Cart, CartItem
from favorites.models import Favourite
from django.contrib.auth.decorators import login_required


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('products:product_list')


@login_required
def add_to_favourites(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    Favourite.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect('products:product_list')



def product_list(request, category_id=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)


    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)


    query = request.GET.get('q')
    if query:
        products = products.filter(Q(name__icontains=query))

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)


@login_required
def add_to_cart(request, product_id):
    return redirect('products:product_list')

@login_required
def add_to_favourites(request, product_id):
    return redirect('products:product_list')