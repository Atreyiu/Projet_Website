from django.shortcuts import render


def blog(request):
    return render(request, 'blog/portfolio.html')

def blog_detail(request):
    return render(request, 'blog/blog_detail.html')

