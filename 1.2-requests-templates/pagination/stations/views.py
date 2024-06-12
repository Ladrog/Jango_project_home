from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    bus_stations_list = []
    with open('data-398-2018-08-30.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, fieldnames=['Name', 'Street', 'District'])
        for row in reader:
            bus_stations_list.append({
                'name': row['Name'],
                'street': row['Street'],
                'district': row['District'],
            })

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    paginator = Paginator(bus_stations_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
         'page': page_obj,
    }
    return render(request, 'stations/index.html', context)
