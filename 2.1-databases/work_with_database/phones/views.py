from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    # phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        products = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        products = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        products = Phone.objects.all().order_by('-price')
    else:
        products = Phone.objects.all()

    context = {'phones': products,
               'sort': sort,
               }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
