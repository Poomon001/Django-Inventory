from django.contrib import admin
from .models import Category, Tag, Product

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Tag)
# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]                                                # Search bar in admin


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]                                                # Search bar in admin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created_at", "updated_at"]      # Display Product fields in admin
    search_fields = ["name", "description"]                                 # Search bar in admin