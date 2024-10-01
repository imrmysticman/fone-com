from django import template
from products.models import Product
from orders.models import Order,OrderItem
# Register template library
register = template.Library()

@register.simple_tag
def get_Order(context):
    request = context.get("request")
    user=request.user if request else None
    customer=user.customer
    Order=customer.order
    Products=Order.orderItem
    return Products


