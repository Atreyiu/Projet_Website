from django.shortcuts import render
from django.shortcuts import render, redirect

def contact(request):
    return render(request, 'contact/contact.html')

