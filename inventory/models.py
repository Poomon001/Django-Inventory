from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=50, 
        unique=True,                        # Ensure no duplicate and indexed for faster lookups
        verbose_name="Category Name"        # Label in forms and admin
    )

    class Meta:
        verbose_name_plural = "Categories"  # correct model name in plural
        ordering = ["name"]                 # Default ordering by name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=50, 
        unique=True,                        # Ensure no duplicate and indexed for faster lookups
        verbose_name="Tag Name"             # Label in forms and admin
    )

    class Meta:
        ordering = ["name"]                 # Default ordering by name

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name="Product Name"         # Label in forms and admin
    )

    description = models.TextField(
        default="",
        blank=True,                         # Allow empty descriptions
        verbose_name="Description"          # Label in forms and admin
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,           # Prevent deletion of category if products exist
        related_name="products",            # Access products from category
        verbose_name="Category"             # Label in forms and admin
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,                         # Allow products without tags
        related_name="products",            # Access products from tag
        verbose_name="Tags"                 # Label in forms and admin
    )

    created_at = models.DateTimeField(
        auto_now_add=True,                  # Automatically set on creation
        editable=False,                     # Prevent manual editing in admin
    )

    updated_at = models.DateTimeField(
        auto_now=True,                      # Automatically update on save
        editable=False,                     # Prevent manual editing in admin
    )

    class Meta:
        ordering = ["-created_at"]          # Default ordering by newest first

    def __str__(self):
        return self.name

