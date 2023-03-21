from django.urls import path
from django.urls import re_path as  url
from .views import(
    hotdeals,
    ProductView,
    checkout,
    store,
    cart,
    add_to_cart,
    delete_from_cart,
    increase_quantity,
    decrease_quantity,
    PlaceOrder,
    Orders
)

urlpatterns = [
    path('all/', store, name='store'),
    path('orders/', Orders.as_view(), name='orders'),
    url(r'^products/(?P<pid>\d+)/product', ProductView.as_view(), name='product'),
    url(r'^checkout/', checkout, name='checkout'),
    url(r'^your/cart/', cart, name='cart'),
    url(r'^add/to/cart/(?P<pid>\d+)/item/', add_to_cart, name='addtocart'),
    url(r'^delete/from/cart/(?P<pid>\d+)/item/', delete_from_cart, name='deletefromcart'),
    url(r'^add/plus/1/(?P<pid>\d+)/item/', increase_quantity, name='plus'),
    url(r'^min/1/(?P<pid>\d+)/item/', decrease_quantity, name='minus'),
    url(r'^cart/checkout/', PlaceOrder, name='placeorder'),
]