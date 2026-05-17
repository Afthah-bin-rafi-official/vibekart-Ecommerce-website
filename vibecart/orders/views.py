from django.shortcuts import render, redirect
from customers.models import Customer
from . models import Order, OrderedItem
from product.models import Product
from django.db.models import Sum
# Create your views here.
def show_cart(request):
    if not request.user.is_authenticated:
         return redirect('account') # user login allenkil login page-ilekku redirect cheyyunnu
    user = request.user
    # 1. First, user-inte customer profile edukuka
    customer = Customer.objects.get(user=user)  # Ninakku 'customer' related_name undo ennu nokuka
    
    # 2. User-inte active cart (Order) edukuka
    cart_obj, created = Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )

    total_price = 0
    for item in cart_obj.added_items.all():
        total_price += item.subtotal  # oro item-inteyum subtotal kootunnu
    
    # 3. Aa cart-il ulla items ellam context vazhi template-ileku ayakkuka
    context = {
        'cart': cart_obj,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)



def add_to_cart(request):
    if not request.user.is_authenticated:
         return redirect('account') # user login allenkil login page-ilekku redirect cheyyunnu
    if request.method == "POST":
        user = request.user
        customer, _ = Customer.objects.get_or_create(user=user)

        product_id = request.POST.get("product_id")
        quantity = int(request.POST.get("quantity", 1))
        size = request.POST.get("size")

        product = Product.objects.get(id=product_id)

        # Get or create the active cart
        cart_obj, _ = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE,
        )

        # FIX: Use get_or_create and then update the quantity
        # We don't put quantity in the filter, we put it in 'defaults'
        item, created = OrderedItem.objects.get_or_create(
            owner=cart_obj,
            product=product,
            size=size,
            defaults={'quantity': quantity}
        )
       

        # If the item already existed in the cart, just increase the quantity
        if not created:
            item.quantity += quantity
            item.save()

        return redirect("cart")

def remove_from_cart(request, pk):
     if request.method == "GET": # templates-il <a href> eppozhum GET request aanu
        item = OrderedItem.objects.get(pk=pk)
        if item:
            item.delete()
     return redirect('cart')