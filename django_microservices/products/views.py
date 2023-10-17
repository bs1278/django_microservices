from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product

@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        # Handle product creation logic
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        
        # Create a new product
        product = Product(name=name, description=description, price=price)
        product.save()
        
        return JsonResponse({"message": "Product created successfully"})
    return JsonResponse({"message": "POST request required for product creation"})

@csrf_exempt
def list_products(request):
    # Retrieve and return a list of products
    products = Product.objects.all()
    product_data = [{"name": product.name, "description": product.description, "price": str(product.price)} for product in products]
    return JsonResponse({"products": product_data})
