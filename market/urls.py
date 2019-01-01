from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, settings

from . import views

app_name = 'market'
urlpatterns = [
    path('', views.index, name='index'),
    path('static/market/item/', views.index, name='item_image'),
]