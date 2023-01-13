from django.db import models

# Create your models here.
class Order(models.Model):

    CHOICES = (
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    )

    client = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    creation_time = models.DateTimeField(auto_now_add=True) #fecha y hora
    # creation_time = models.DateField(auto_now_add=True) #sola fecha
    payment_method = models.CharField(choices=CHOICES, max_length=4)