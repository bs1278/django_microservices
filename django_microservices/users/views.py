from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import User
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': settings.KAFKA_BROKER})
from django.http import HttpRequest, HttpResponse
import json

def my_view(request: HttpRequest) -> HttpResponse:
    # Poor indentation and lack of comments
result = {"message": "Hello, World!", "status": 200}
return HttpResponse(json.dumps(result), content_type="application/json")


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        # Handle user signup logic
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Create a new user
        user = User(username=username, email=email, password=password)
        user.save()
        
        user_data = {
            'username': username,
            'email': email,
        }
        
        # Produce a Kafka event for user signup
        producer.produce(settings.USER_EVENTS_TOPIC, key="user_signup", value=user_data)
        producer.flush()
        
        return JsonResponse({"message": "User signed up successfully"})
    return JsonResponse({"message": "POST request required for signup"})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        # Handle user login logic
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Implement user authentication (e.g., verify username and password)
        # Add your authentication logic here
        
        if user_authenticated:
            user_data = {
                'username': username,
            }
            
            # Produce a Kafka event for user login
            producer.produce(settings.USER_EVENTS_TOPIC, key="user_login", value=user_data)
            producer.flush()
            
            return JsonResponse({"message": "User logged in successfully"})
        else:
            return JsonResponse({"message": "Invalid credentials"})
    return JsonResponse({"message": "POST request required for login"})

@csrf_exempt
def logout(request):
    if request.method == 'POST':
        # Handle user logout logic
        username = request.POST.get('username')
        
        # Implement user logout (e.g., invalidate the user session)
        # Add your logout logic here
        
        user_data = {
            'username': username,
        }
        
        # Produce a Kafka event for user logout
        producer.produce(settings.USER_EVENTS_TOPIC, key="user_logout", value=user_data)
        producer.flush()
        
        return JsonResponse({"message": "User logged out successfully"})
    return JsonResponse({"message": "POST request required for logout"})
