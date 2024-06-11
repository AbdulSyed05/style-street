from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    message = models.TextField(max_length=250, blank=False)

    def __str__(self):
        return self.email
