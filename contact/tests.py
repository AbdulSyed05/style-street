from django.test import TestCase
from .forms import ContactUsForm


class TestingContactUsForm(TestCase):
    """
    Testing ContactUs Form
    """

    def test_name_required(self):
        form = ContactUsForm({"name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors.keys())
        self.assertEqual(form.errors["name"][0], "This field is required.")

    def test_description_required(self):
        form = ContactUsForm({"email": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("description", form.errors.keys())
        self.assertEqual(form.errors["description"][0], "This field is required.")

    def test_description_required(self):
        form = ContactUsForm({"message": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("size", form.errors.keys())
        self.assertEqual(form.errors["size"][0], "This field is required.")
