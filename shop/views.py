from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q 
from django.contrib.messages import add_message, INFO, SUCCESS
from .models import (
    Item,
    Cart,
    CartItem,
    ItemReviews,
    Order,
    OrderItems
)
from .forms import ReviewForm

@login_required(login_url='login')
def store(request):
    cart = Cart.objects.get(user=request.user)
    count = CartItem.objects.filter(cart=cart).count()
    items = Item.objects.all()
    p = Paginator(items, 50)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {
        'page_obj':page_obj,
        'count':count
        }
    return render(request, 'store.html', context)

@login_required(login_url='login')
def hotdeals(request):
    cart = Cart.objects.get(user=request.user)
    count = CartItem.objects.filter(cart=cart).count()
    items = Item.objects.filter(offer=True)
    context = {
        'items':items,
        'count':count
        }
    return render(request, 'shop/hotdeals.html', context)

class ProductView(LoginRequiredMixin, View):
    def get(self,request, pid):
        form = ReviewForm()
        product = Item.objects.get(id=pid)
        reviews = ItemReviews.objects.filter(item=product)
        cart = Cart.objects.get(user=request.user)
        count = CartItem.objects.filter(cart=cart).count()
        context={
            'product':product,
            'count':count,
            'form':form,
            'reviews':reviews
        }
        return render(request, 'product.html', context)
    def post(self, request,pid):
        form = ReviewForm(request.POST)
        if form.is_valid():
            product = Item.objects.get(id=pid)
            form.instance.item = product
            form.instance.customer = request.user
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
        
        context={
            'form':form,
        }
        return render(request, 'product.html', context)

@login_required(login_url='login')
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    count = CartItem.objects.filter(cart=cart).count()
    items = CartItem.objects.filter(Q(cart=cart))
    total = 0
    for item in items:
        total += item.get_cost()
    context ={
        'items':items,
        'total':total,
        'count':count
        }
    return render(request, 'checkout.html',context)

@login_required(login_url='login')
def cart(request):
    cart = Cart.objects.get(user=request.user)
    count = CartItem.objects.filter(cart=cart).count()
    items = CartItem.objects.filter(Q(cart=cart))
    items_count = 0
    total = 0
    for item in items:
        items_count += item.quantity
        total += item.get_cost()
    
    context={
        'items':items,
        'all':items_count,
        'total':total,
        'count':count
    }
    return render(request, 'cart.html', context)

@login_required(login_url='login')
def add_to_cart(request, pid):
    item = Item.objects.get(id=pid)
    cart = Cart.objects.get(user=request.user)
    items = set(CartItem.objects.filter(cart=cart))
    if item in items:
        add_message(request,INFO, 'Item already is in Cart')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        CartItem.objects.create(cart=cart, product=item)
        add_message(request,SUCCESS, 'Item added to Cart')
        return redirect(request.META.get('HTTP_REFERER'))
    
@login_required(login_url='login')
def delete_from_cart(request, pid):
    cart = Cart.objects.get(user=request.user)
    item = CartItem.objects.filter(Q(cart=cart) &Q(id=pid))
    item.delete()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def increase_quantity(request, pid):
    cart = Cart.objects.get(user = request.user)
    item = CartItem.objects.get(Q(id=pid) & Q(cart=cart))
    item.quantity +=1
    item.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def decrease_quantity(request, pid):
    cart = Cart.objects.get(user = request.user)
    item = CartItem.objects.get(Q(id=pid) & Q(cart=cart))
    if item.quantity == 1:
        item.delete()
    else:
        item.quantity -=1
        item.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def PlaceOrder(request):
    cart = Cart.objects.get(user=request.user)
    items = CartItem.objects.filter(Q(cart=cart))
    if items:
        order = Order.objects.create(cart=cart,ordered=True)
        for item in items:
            OrderItems.objects.create(order=order,item_name=item.product.name,
            item_price=item.product.price,quantity=item.quantity,total_cost=int(item.product.price * item.quantity))
        items.delete()
        ordered = OrderItems.objects.filter(order=order)
        bill = 0
        for o in ordered:
            bill += o.total_cost
        order.bill = bill
        order.save()
    else:
        return redirect('store')
    return redirect('store')

class Orders(LoginRequiredMixin,View):
    def get(self,request):
        user = request.user
        cart = Cart.objects.get(user=user)
        orders = Order.objects.filter(cart=cart)
        count = CartItem.objects.filter(cart=cart).count()
        context = {
            'count':count,
            'orders':orders, 
        }
        return render(request,'orders.html', context)

