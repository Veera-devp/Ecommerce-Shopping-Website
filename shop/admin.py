from django.contrib import admin
from .models import Products,Order
# Register your models here.
admin.site.site_header = "Ecommerce Site"
admin.site.site_title = "Ecommerce Simple Site"
admin.site.index_title = "Manage Ecommerce Shopping"

class ProductAdmin(admin.ModelAdmin):
      list_dislay = ('title','price','discount_price','category','description')


admin.site.register(Products,ProductAdmin)
admin.site.register(Order)