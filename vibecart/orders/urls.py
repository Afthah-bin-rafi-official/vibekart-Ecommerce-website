from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('cart', views.show_cart, name='cart'),
    path('add-to-cart', views.add_to_cart, name='add_to_cart'),
    path('remove_item/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
]
