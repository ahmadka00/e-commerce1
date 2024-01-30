from django.shortcuts import render, get_object_or_404
from .basket import Basket
from store.models import Product
from django.http import JsonResponse

def basket_summary(request):
    return render(request, 'basket/summary.html')


def add_basket(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        basket_qty = basket.__len__()
        response = JsonResponse({'qty':basket_qty})
        return response

def delete_basket(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        print(product_id)
        basket.delete(product=product_id)
        response = JsonResponse({'Success': True})
        return response

def update_basket(basket):
    pass