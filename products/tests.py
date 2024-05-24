from django.test import TestCase
from .forms import ProductForm


class TestingProductForm(TestCase):
    """
    Testing Product Form
    """

    def test_name_required(self):
        form = ProductForm({'name': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_description_required(self):
        form = ProductForm({'description': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')
    
    def test_description_required(self):
        form = ProductForm({'size': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('size', form.errors.keys())
        self.assertEqual(form.errors['size'][0], 'This field is required.')
    
    def test_price_required(self):
        form = ProductForm({'price': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_stock_required(self):
        form = ProductForm({'stock': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('stock', form.errors.keys())
        self.assertEqual(form.errors['stock'][0], 'This field is required.')
