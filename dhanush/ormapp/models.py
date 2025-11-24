from django.db import models
from django.contrib import admin
class products (models.Model):
    productname = models.CharField(max_length=30)
    quantity = models.FloatField()
    mrp = models.FloatField()
    price = models.FloatField()
    total = models.FloatField()
    savings = models.FloatField()
class productsAdmin(admin.ModelAdmin):
    list_display =["productname","quantity","mrp","price","total","savings"] 