from django.test import TestCase
from .models import Product, Category, Tag

class ProductModelTest(TestCase):
    def setUp(self):
        # create category
        self.category = Category.objects.create(name='Electronics')
        
        # create tags
        tag_names = ['Best Seller', 'New Arrival', 'Gift Idea']
        self.tags = [Tag.objects.create(name=name) for name in tag_names]

        # create product
        self.product = Product.objects.create(
            name='Smartphone',
            description='A smartphone with a great camera.',
            category=self.category,
        )

        def test_product_creation(self):
            product = Product.objects.get(name='Smartphone')
            self.assertEqual(product.category.name, 'Electronics')
            self.assertEqual(product.description, 'A smartphone with a great camera.')