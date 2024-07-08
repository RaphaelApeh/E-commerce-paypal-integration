from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,unique=True)
    discription = models.TextField(blank=True,null=True)
    is_sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media')
    time = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0.00,null=True)
    likes = models.ManyToManyField(User,blank=True,related_name='product_likes')

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['-time']

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.name)
