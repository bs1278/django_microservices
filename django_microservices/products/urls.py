from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('list/', views.list_products, name='list_products'),
]
