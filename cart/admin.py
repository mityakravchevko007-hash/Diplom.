from .models import Cart, CartItem
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    inlines = [OrderItemInline]
    ordering = ('-created_at',)


admin.site.register(Order, OrderAdmin)

admin.site.register(Cart)
admin.site.register(CartItem)

