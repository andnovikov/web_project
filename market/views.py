from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render, reverse

from .models import Item

def index(request):
    item_list = Item.objects.order_by('-item_name')
    context = {'item_list': item_list}
    return render(request, 'market/index.html', context)