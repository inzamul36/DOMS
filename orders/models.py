from django.db import models

# Create your models here.
class Order (models.Model):
    name = models.CharField(max_length=200);
    phone = models.CharField(max_length=20);
    address = models.TextField();
    delivery_date = models.DateField(blank=True);
    product_id = models.TextField();
    payment_option = models.CharField(max_length=50);
    amount = models.IntegerField();
    order_status = models.CharField(max_length=50);
