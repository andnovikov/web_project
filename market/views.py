from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render, reverse

from .models import Item, Category

def index(request):
    item_list = Item.objects.order_by('-item_name')
    context = {'item_list': item_list}
    return render(request, 'market/index.html', context)

def products(request):
    cat_list = Category.objects.order_by('-category_name')
    item_list = Item.objects.order_by('-item_name')
    context = {'item_list': item_list, 'cat_list': cat_list}
    return render(request, 'market/products.html', context)

def about(request):
    return render(request, 'market/about.html', )

def faqs(request):
    return render(request, 'market/faqs.html', )

def contact(request):
    return render(request, 'market/contact.html', )

def shoppingcart(request):
    return render(request, 'market/shoppingcart.html', )

def checkout(request):
    return render(request, 'market/checkout.html', )

def productdetail(request):
    return render(request, 'market/productdetail.html', )