from django.contrib import admin
from .models import Family, User, Product


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class Product(admin.ModelAdmin):
    pass
