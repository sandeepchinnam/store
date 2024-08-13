from django.shortcuts import render, get_object_or_404, redirect
from .models import Rice, CartItem, Order
from .forms import CheckoutForm, OrderForm

def home(request):
    rice_items = Rice.objects.all()
    return render(request, 'store/home.html', {'rice_items': rice_items})

def add_to_cart(request, rice_id):
    rice = get_object_or_404(Rice, id=rice_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.create()

    cart_item, created = CartItem.objects.get_or_create(
        rice=rice,
        session_key=request.session.session_key,
        defaults={'quantity': 1},
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')

def view_cart(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
    cart_items = CartItem.objects.filter(session_key=session_key)
    total_price = sum(item.total_price for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def update_cart(request):
    if request.method == 'POST':
        session_key = request.session.session_key
        if not session_key:
            request.session.create()

        for item_id in request.POST:
            if item_id.startswith('quantity_'):
                cart_item_id = int(item_id.split('_')[1])
                quantity = int(request.POST[item_id])

                cart_item = get_object_or_404(CartItem, id=cart_item_id, session_key=session_key)
                
                if quantity > 0:
                    cart_item.quantity = quantity
                    cart_item.save()
                else:
                    cart_item.delete()

    return redirect('view_cart')

def checkout(request):
    session_key = request.session.session_key
    cart_items = CartItem.objects.filter(session_key=session_key)
    total_price = sum(item.total_price for item in cart_items)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            mobile_number = form.cleaned_data['mobile_number']

            for item in cart_items:
                Order.objects.create(
                    name=name,
                    address=address,
                    mobile_number=mobile_number,
                    rice=item.rice,
                    quantity=item.quantity
                )

            CartItem.objects.filter(session_key=session_key).delete()

            return redirect('home')
    else:
        form = CheckoutForm()

    return render(request, 'store/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'total_price': total_price
    })

from django.shortcuts import render
from .models import Order


def admin_panel(request):
    orders = Order.objects.all()
    return render(request, 'store/admin_panel.html', {'orders': orders})
def cart(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'store/cart.html', {'form': form})
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

@require_POST
def update_delivery_status(request):
    if "delete_order" in request.POST:
        order_id = request.POST.get("delete_order")
        Order.objects.filter(id=order_id).delete()
    else:
        order_ids = request.POST.getlist("delivery_status")
        Order.objects.filter(id__in=order_ids).update(status="OK for Delivery")
    
    return redirect('admin_panel') 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Rice

# View to manage rice items
from django.shortcuts import render
from .models import Rice

def manage_rice_items(request):
    rice_items = Rice.objects.all()
    return render(request, 'manage_rice.html', {'rice_items': rice_items})

# View to save or update a rice item
def save_rice_item(request):
    if request.method == 'POST':
        rice_id = request.POST.get('rice_id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        if rice_id:  # Edit existing rice item
            rice_item = get_object_or_404(Rice, pk=rice_id)
            rice_item.name = name
            rice_item.price = price
            rice_item.quantity = quantity
            rice_item.save()
        else:  # Create new rice item
            Rice.objects.create(name=name, price=price, quantity=quantity)

        return redirect('manage_rice_items')

# View to delete a rice item
def delete_rice_item(request, id):
    rice_item = get_object_or_404(Rice, pk=id)
    rice_item.delete()
    return redirect('manage_rice_items')
