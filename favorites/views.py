from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Favourite



@login_required
def favorite_view(request):
    favorites = Favourite.objects.filter(user=request.user)

    return render(request, 'favorites.html', {
        'favorites': favorites
    })



@login_required
def add_to_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    Favourite.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect('favorites')



@login_required
def remove_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    Favourite.objects.filter(
        user=request.user,
        product=product
    ).delete()

    return redirect('favorites')