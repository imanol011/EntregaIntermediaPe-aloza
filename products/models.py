from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    price = models.FloatField(verbose_name='Precio')
    stock = models.BooleanField(default=True, verbose_name='En Stock')
    # image = models.ImageField(upload_to='products', verbose_name='Imagen')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)