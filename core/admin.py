from django.contrib import admin

from .models import Category,Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','is_sold']
    search_fields = ['name','discription']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)