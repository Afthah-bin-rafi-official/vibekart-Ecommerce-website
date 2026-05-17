from django.db import models
from customers.models import Customer
from product.models import Product

class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'), (DELETE,'Delete'))
    
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    
    # Ellaa choices-um ivide add cheyyunnathaanu nallathu
    STATUS_CHOICES=( 
        (CART_STAGE, 'Cart'),
        (ORDER_CONFIRMED, 'Order Confirmed'),
        (ORDER_PROCESSED,'Order Processed'), 
        (ORDER_DELIVERED,'Order Delivered'), 
        (ORDER_REJECTED,'Order Rejected')
    )
    
    order_status = models.IntegerField(choices=STATUS_CHOICES,
                                        default=CART_STAGE)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL,
                               null=True, related_name='orders')
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,
                                 null=True, related_name='added_carts')
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=10, default='M')
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, 
                              related_name='added_items')

    # Ithu add cheythaal, same product same size-il duplicate aayi varilla
    class Meta:
        unique_together = ('owner', 'product', 'size')

    
    @property
    def subtotal(self):
        return self.product.price * self.quantity
