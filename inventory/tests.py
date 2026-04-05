from django.test import TestCase
from .models import Product, Category, Tag

class ProductModelTest(TestCase):
    def setUp(self):
        # create categories
        category_names = ['Electronics', 'Books']
        self.categories = [Category.objects.create(name=name) for name in category_names]
        
         # create tags
        tag_names = ['Best Seller', 'New Arrival', 'Gift Idea']
        self.tags = [Tag.objects.create(name=name) for name in tag_names]

        # create product
        Product.objects.create(
            name='Smartphone',
            description='A smartphone with a great camera.',
            category=self.categories[0],
        )

        labtop = Product.objects.create(
            name='Laptop',
            description='A powerful laptop for professionals.',
            category=self.categories[0],
        )
        labtop.tags.set(self.tags)

        book = Product.objects.create(
            name='Murder on the Orient Express',
            description='A detective story about a murder on a train.',
            category=self.categories[1],
        )
        book.tags.set([self.tags[0]])

    # Test database creation number
    def test_product_count(self):
        count = Product.objects.count()
        self.assertEqual(count, 3)

    # Test database creation Product table
    def test_product_creation(self):
        product = Product.objects.get(name='Smartphone')
        self.assertEqual(product.category.name, 'Electronics')
        self.assertEqual(product.description, 'A smartphone with a great camera.')

    # Test database creation Tags table
    def test_product_tags(self):
        laptop = Product.objects.get(name='Laptop')
        self.assertEqual(laptop.tags.count(), 3)
        self.assertEqual(sorted(list(laptop.tags.values_list('name', flat=True))), 
            sorted(['Best Seller', 'New Arrival', 'Gift Idea']))

        book = Product.objects.get(name='Murder on the Orient Express')
        self.assertEqual(book.tags.count(), 1)
        self.assertEqual(book.tags.first().name, 'Best Seller')
    
    # Test search and filter functionality via a request to View
    def test_search_filter_found(self):
        response = self.client.get("/inventory/products/?search=camera&category=Electronics")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Smartphone")

    # Test search and filter functionality via a request to View
    def test_search_filter_not_found(self):
        response = self.client.get("/inventory/products/?search=camera&category=Book")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products']), 0)