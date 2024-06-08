from django.contrib import admin
from .models import ContactUs

# Register your models here.


class Contact(admin.ModelAdmin):
    list_display = ("name", "email", "message")

    ordering = ("name",)


admin.site.register(ContactUs)
