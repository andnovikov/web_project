from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, settings

from . import views

app_name = 'market'
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('products', views.products, name='products'),
    path('productdetail', views.productdetail, name='productdetail'),
    path('about', views.about, name='about'),
    path('faqs', views.faqs, name='faqs'),
    path('contact', views.contact, name='contact'),
    path('shoppingcart', views.shoppingcart, name='shoppingcart'),
    path('checkout', views.checkout, name='checkout'),
    path('static/market/item/', views.index, name='item_image'),
]