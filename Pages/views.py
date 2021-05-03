from django.shortcuts import render


def home(request):
    return render(request, 'Pages/index.html')


def blog(request):
    return render(request, 'blog/portfolio.html')
