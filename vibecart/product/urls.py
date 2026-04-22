from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('product_list',views.list_products,name='list_product'),
    path('product_detail',views.detail_products,name='detail_product'),
]
