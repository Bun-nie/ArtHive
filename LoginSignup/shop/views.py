import json
import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import *


# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()
def shop(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0,}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    categories = ShopCategory.objects.all()
    context = {'products': products, 'cartItems': cartItems, 'shop_category' : categories}
    return render(request, 'shop/shop.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order':order, 'cartItems':cartItems}
    return render(request, 'shop/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems':cartItems}
    return render(request, 'shop/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    order.update_total()

    return JsonResponse({
        'message': 'Item was added or updated',
        'order_total': order.get_total_price(),
        'item_quantity': orderItem.quantity
    })

@csrf_exempt
def processOrder(request):
    user = get_object_or_404(settings.AUTH_USER_MODEL, id=request.user.id)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                zipcode=data['shipping']['zipcode'],
                country = data['shipping']['country'],
            )

    else:
        print('User not logged in')
    return JsonResponse('Payment submitted..', safe=False)

@login_required(login_url='login')
def render_product_form(request):
    user = get_object_or_404(User, id=request.user.id)

    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            print('Form Valid')
            report = form.save(commit=False)
            report.user = user
            report.save()
            return redirect('shop')
    else:
        print('Form Not Valid')
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def view_product(request, product_id):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0,}
        cartItems = order['get_cart_items']
    categories = ShopCategory.objects.all()
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product, 'cartItems': cartItems, 'shop_category': categories}
    return render(request,"view_product.html",context)
