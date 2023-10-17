from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        # Handle order creation logic
        user_id = request.POST.get('user_id')
        product_id = request.POST.get('product_id')
        
        # Create a new order
        order = Order(user_id=user_id, product_id=product_id)
        order.save()
        
        return JsonResponse({"message": "Order created successfully"})
    return JsonResponse({"message": "POST request required for order creation"})

@csrf_exempt
def list_orders(request):
    # Retrieve and return a list of orders
    orders = Order.objects.all()
    order_data = [{"user_id": order.user_id, "product_id": order.product_id, "order_date": order.order_date} for order in orders]
    return JsonResponse({"orders": order_data})
