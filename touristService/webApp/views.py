from django.shortcuts import render
from django.apps import apps
from django.db.models import Q
from django.db.models.functions import Lower


def remove_all_zero_values(data):
    new_data = {}
    for key, value in data.items():
        if value != 0:
            new_data[key] = value
    return new_data


def get_min_in_dict(data):
    minimum = 1000000000
    for m in data.values():
        minimum = min(minimum, m)
    return minimum


def get_max_in_dict(data):
    maximum = 0
    for m in data.values():
        maximum = max(maximum, m)
    return maximum


def set_min_and_max_price(data):
    return get_min_in_dict(data), get_max_in_dict(data)


def region(request, number_of_region: int):
    region_from_db = apps.get_model('dataParser', 'Region').objects.get(rating=number_of_region)
    model_info_about_region = apps.get_model('dataParser', 'RegionStatistics').objects.get(region=region_from_db)

    info_from_fields = model_info_about_region._meta.get_fields()
    info_about_region = {}

    for i in range(2, len(info_from_fields)):
        value_of_region = info_from_fields[i].value_from_object(model_info_about_region)
        info_about_region[info_from_fields[i].verbose_name] = value_of_region

    apartment = {
        'Аренда помещения': info_about_region['Аренда помещения'],
        'Проживание в хостеле': info_about_region['Проживание в хостеле'],
        'Проживание в гостинице (эконом)': info_about_region['Проживание в гостинице (эконом)'],
        'Проживание в гостинице (комфорт)': info_about_region['Проживание в гостинице (комфорт)'],
        'Проживание в гостинице (Люкс)': info_about_region['Проживание в гостинице (Люкс)'],
    }

    beauty_service = {
        'Средняя цена услуги мастера в салоне красоты': info_about_region[
            'Средняя цена услуги мастера в салоне красоты'],
        'Поход в баню': info_about_region['Поход в баню'],
        'Поход к врачу': info_about_region['Поход к врачу'],
    }

    dinner = {
        'Средний чек в заведениях премиум класса': info_about_region['Средний чек в заведениях премиум класса'],
        'Средний чек в заведениях общепита': info_about_region['Средний чек в заведениях общепита'],
    }

    bank_services = {
        'Аренда сейфа': info_about_region['Аренда сейфа'],
    }

    thoroughfare = {
        'Проезд в трамвае': info_about_region['Проезд в трамвае'],
        'Проезд в троллейбусе': info_about_region['Проезд в троллейбусе'],
        'Проезд в такси': info_about_region['Проезд в такси'],
        'Проезд в городском автобусе': info_about_region['Проезд в городском автобусе'],
        'Проезд в пригородном поезде': info_about_region['Проезд в пригородном поезде'],
        'Услуги аренды автомобилей, час': info_about_region['Услуги аренды автомобилей, час'],
    }

    entertainments = {
        'Поход в кинотеатр': info_about_region['Поход в кинотеатр'],
        'Поход в театр': info_about_region['Поход в театр'],
        'Поход в музей': info_about_region['Поход в музей'],
        'Автобусная экскурсия': info_about_region['Автобусная экскурсия'],
        'Посещение санатория (день)': info_about_region['Посещение санатория (день)'],
        'Услуги организатора проведения торжеств': info_about_region['Услуги организатора проведения торжеств'],
        'Экскурсионные туры по России': info_about_region['Экскурсионные туры по России']
    }

    check_in_shop = {
        'Алкоголь (литр)': info_about_region['Алкоголь (литр)'],
        'Вода (литр)': info_about_region['Вода (литр)'],
        'Напитки газированные (литр)': info_about_region['Напитки газированные (литр)'],
        'Мороженное (килограмм)': info_about_region['Мороженное (килограмм)'],
        'Кофе (килограмм)': info_about_region['Кофе (килограмм)'],
        'Чай в пакетика (25 пакетиков)': info_about_region['Чай в пакетика (25 пакетиков)'],
    }

    liter_of_gasoline = {
        'Бензин (литр)': info_about_region['Бензин (литр)']
    }

    utility_bills = {
        'Коммунальные услуги': info_about_region['Коммунальные услуги']
    }

    book_price = {
        'Стоимость книги': info_about_region['Стоимость книги']
    }

    gym = {
        'Клубная карта в фитнес-клуб, месяц': info_about_region['Клубная карта в фитнес-клуб, месяц']
    }

    dict_with_statistic = {
        'Услуги проживания': apartment,
        'Услуги красоты': beauty_service,
        'Питание': dinner,
        'Банковские услуги': bank_services,
        'Поездка на общественном транспорте': thoroughfare,
        'Развлечения': entertainments,
        'Цены в магазине': check_in_shop,
        'Цена бензина': liter_of_gasoline,
        'Коммунальные услуги': utility_bills,
        'Цена за книги': book_price,
        'Посещение спортзала': gym,
    }

    names_with_zero_value = []
    for header, dict_ in dict_with_statistic.items():
        dict_with_statistic[header] = remove_all_zero_values(dict_)
        if len(dict_with_statistic[header]) == 0:
            names_with_zero_value.append(header)

    for name in names_with_zero_value:
        dict_with_statistic.pop(name)

    range_of_price = {}
    for names, dict_with_info in dict_with_statistic.items():
        range_of_price[names] = set_min_and_max_price(dict_with_info)

    comments = apps.get_model('dataParser', 'Comments').objects.filter(Q(region=region_from_db))

    return render(request, 'webApp/about_region.html', {'region': region_from_db,
                                                        'info_about_region': dict_with_statistic,
                                                        'prices': range_of_price,
                                                        'comments': comments})


def index(request):
    search_query = request.GET.get("q")
    tags_query = request.GET.get("tags")
    print(search_query)
    tags = apps.get_model('dataParser', 'Tags').objects.all()
    if search_query is None and tags_query is None:
        regions = apps.get_model('dataParser', 'Region').objects.prefetch_related('tags').all().order_by('rating')
    elif tags_query is None:
        regions = apps.get_model('dataParser', 'Region').objects.filter(Q(title__icontains=search_query) |
                                                                        Q(title__icontains=search_query.capitalize()) |
                                                                        Q(long_definition__icontains=search_query) |
                                                                        Q(long_definition__icontains=search_query.capitalize())
                                                                        )
    elif search_query is None:
        tags_query = tags_query.split(",")
        regions = apps.get_model('dataParser', 'Region').objects.filter(tags__in=tags_query)
    else:
        tags_query = tags_query.split(",")
        regions = apps.get_model('dataParser', 'Region').objects.filter(Q(title__icontains=search_query) |
                                                                Q(title__icontains=search_query.capitalize()) |
                                                                Q(long_definition__icontains=search_query) |
                                                                Q(long_definition__icontains=search_query.capitalize()) |
                                                                Q(tags__in=tags_query)
                                                                )

    state_of_header = "Топ туристических регионов по популярности"

    if len(regions) == 0:
        state_of_header = "Ничего не найдено"
    model_with_info_about_region = apps.get_model('dataParser', 'RegionStatistics')
    regions_statistic = {}

    for region in regions:
        i = model_with_info_about_region.objects.get(region=region)
        regions_statistic[region.rating] = {
            'min_apartment_price': i.min_apartment_price,
            'max_apartment_price': i.max_apartment_price,
            'image': region.image,
            'rating': region.rating,
            'title': region.title,
            'short_definition': region.short_definition,
            'tags': region.tags
        }

    return render(request, 'webApp/index.html', {
        'regions': regions_statistic,
        'tags': tags,
        'state_of_header': state_of_header
    })
