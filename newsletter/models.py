from django.db import models


class NewsletterSignup(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    gdpr = models.BooleanField(default=False)

    def __str__(self):
        return self.email
