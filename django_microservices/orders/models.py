from django.db import models

class Order(models.Model):
    user_id = models.IntegerField()  
    product_id = models.IntegerField()  
    order_date = models.DateTimeField(auto_now_add=True)
