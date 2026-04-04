from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorite_view, name='favorites'),
    path('add/<int:product_id>/',
    views.add_to_favorite, name='add_to_favorite'),
    path('remove/<int:product_id>/',
    views.remove_favorite, name='remove_favorite'),
]