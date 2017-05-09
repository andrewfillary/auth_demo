from django.test import TestCase
from products.views import all_products
from django.core.urlresolvers import resolve

# Create your tests here.

class ProductPageTest(TestCase):

    def test_products_page_resolves(self):
        products_page = resolve('/products')
        self.assertEqual(products_page.func, all_products)
