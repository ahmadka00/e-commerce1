from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_page', args=[self.slug])
    
    def __str__(self):
        return self.name
    


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField(default=1)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', )

    def save(self, *args, **kwargs):
        if self.quantity == 0:
            self.in_stock = False
        elif self.quantity > 0:
            self.in_stock = True
        super().save(*args, **kwargs)
    

    def get_absolute_url(self):
        return reverse('store:product_page', args=[self.slug])
    
    def __str__(self):
        return self.title