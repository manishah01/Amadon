from django.shortcuts import render,redirect
from .models import Order, Product
from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    last_order = Order.objects.last() #retrieves last ordered item
    price= last_order.total_price # price of last order 
    orders_made = Order.objects.aggregate(Sum('quantity_ordered'))['quantity_ordered__sum']
    money_spent_at_amadon = Order.objects.aggregate(Sum('total_price'))['total_price__sum']
    context = {
        'orders':orders_made,
        'total': money_spent_at_amadon,
        'bill':price,
    }
    return render(request, "store/receipt.html",context)

def receipt(request):
    if request.method == 'POST':
        this_product = Product.objects.filter(id=request.POST["id"])
        if not this_product:
            return redirect('/')
        else:
            quantity = int(request.POST["quantity"])
            total_charge = quantity*(float(this_product[0].price))
            Order.objects.create (
                quantity_ordered = quantity,
                total_price = total_charge
            )
            return redirect('/checkout')
    else:
        return redirect('/')