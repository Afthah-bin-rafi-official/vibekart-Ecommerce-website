from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    featured_products = Product.objects.order_by('-priority').filter(delete_status=Product.LIVE)[:4]
    latest_products = Product.objects.order_by('-id').filter(delete_status=Product.LIVE)[:8]
    context = {
        'featured_products': featured_products,
        'latest_products': latest_products,
    }
    print(context)
    return render(request, 'index.html', context)

def list_products(request):
    """_summary_
    returns products list
    Args:
        request (_type_): _description_
    Returns:
        _type_: _description_
    """
    page =   1
    if request.GET:
        page = request.GET.get('page', 1)
    product_list = Product.objects.order_by('-priority').filter(delete_status=Product.LIVE)
    product_paginator = Paginator(product_list, 4) # Show 4 products per page
    product_list = product_paginator.get_page(page)
    context = {
        'products': product_list
    }
    return render(request,'products.html', context)

def detail_products(request,pk):
    product = Product.objects.get(pk=pk)
    context={'product': product}
    if request.POST:
        print(request.POST)
    return render(request,'product_detail.html', context)