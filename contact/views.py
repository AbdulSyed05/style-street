# views.py
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactUsForm


def view_contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # form.save()
            messages.success(request, "Message successfully send!")
            return redirect("contact_success")
    else:
        form = ContactUsForm()
    return render(request, "contact/contact.html", {"form": form})


def contact_success(request):
    return render(request, "contact/success.html")
