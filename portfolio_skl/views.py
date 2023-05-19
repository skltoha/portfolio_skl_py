from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'request': request})


def services(request):
    return render(request, 'services.html', {'request': request})


def work(request):
    return render(request, 'work.html', {'request': request})


def worksingle(request):
    return render(request, 'work-single.html', {'request': request})


def blog(request):
    return render(request, 'blog.html', {'request': request})


def about(request):
    return render(request, 'about.html', {'request': request})


def contact(request):
    return render(request, 'contact.html', {'request': request})

