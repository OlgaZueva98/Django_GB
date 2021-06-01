from django.shortcuts import render


def products(request):
    title = 'каталог/продукты'

    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'mainapp:index', 'name': 'офис'},
        {'href': 'mainapp:index', 'name': 'модерн'},
        {'href': 'mainapp:index', 'name': 'классика'},
    ]

    context = {
        'links_menu': links_menu,
        'title': title,
    }

    return render(request, 'mainapp/products.html', context=context)
