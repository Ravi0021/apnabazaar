from django.contrib import admin
from django.db import models
from . models import Product,Category,Company
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Company)
