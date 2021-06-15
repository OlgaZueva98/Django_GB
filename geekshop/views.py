from django.shortcuts import render
from mainapp.models import Product


def index(request):

    title = 'geekshop'
    products = Product.objects.all()[:4]

    context = {
        'products': products,
        'some_name': 'hello',
        'title': title,
    }
    return render(request, 'index.html', context=context)


def contacts(request):
    return render(request, 'contact.html')
