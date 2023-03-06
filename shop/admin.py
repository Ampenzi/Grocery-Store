from django.contrib import admin
from .models import(
    Item,
    Cart,
    CartItem,
    ItemReviews,
    Order,
    OrderItems
)

class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ['name', 'price', 'offer']
    list_display_links = ['name']
admin.site.register(Item, ItemAdmin)

class CartManager(admin.ModelAdmin):
    model=Cart
    list_display= ['user', 'created_on']

admin.site.register(Cart,CartManager)

class CartItemManger(admin.ModelAdmin):
    model = CartItem
    list_display = ['cart', 'product', 'quantity']

admin.site.register(CartItem,CartItemManger)

class ReviewsAdmin(admin.ModelAdmin):
    model = ItemReviews
    list_display = ['item', 'review']

admin.site.register(ItemReviews, ReviewsAdmin)

class OrderItemsAdminInline(admin.TabularInline):
    model = OrderItems

class OrderAdmin(admin.ModelAdmin):
    model= Order
    list_display = ['cart', 'paid', 'ordered', 'bill','date']
    inlines = [OrderItemsAdminInline,]
admin.site.register(Order, OrderAdmin)