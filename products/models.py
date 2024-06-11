from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    cat_desc = models.CharField(max_length=254, null=True, blank=True)
    cat_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Condition(models.Model):

    class Meta:
        verbose_name_plural = "Condition"

    name = models.CharField(max_length=254, help_text="", blank=False)
    condition_desc = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    # Define Size Choices inside the Product model class
    SIZE_CHOICES = (
        ("XS", "Extra Small"),
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra Large"),
    )
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=254, blank=False)
    color = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    fabric = models.CharField(max_length=254)
    size = models.CharField(
        max_length=2, choices=SIZE_CHOICES, default="M"
    )  # Added size field with default value 'M'
    condition = models.ForeignKey(
        "Condition", null=True, blank=True, on_delete=models.SET_NULL
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    stock = models.IntegerField(default=1)
    likes = models.ManyToManyField(User, related_name="product_likes", blank=True)
    image1_alt_text = models.TextField(null=True, blank=False)
    image2_alt_text = models.TextField(null=True, blank=False)
    image3_alt_text = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.likes.count()
