import requests
import json
import re


class Service:
    names_of_services: tuple
    average_price: int = 0
    counter: int = 0

    def __init__(self, names_of_services):
        self.names_of_services = names_of_services


class Value:
    count = 0
    average_price = 0


def count_average_price_for_region(region_services, services_statistic: dict):
    pattern = re.compile(r"[0-9,.]+")
    for info_about_region in region_services['results']:
        price: int = 0
        for value in info_about_region:
            if pattern.match(info_about_region[value]):
                category = info_about_region[value]
                category = category.replace(',', '.')
                price += float(category)

        for key, value in services_statistic.items():
            if info_about_region['dim58273'] in key:
                value.average_price += price
                value.count += 1

    for key, value in services_statistic.items():
        if value.count != 0:
            value.average_price = round(value.average_price / value.count, 2)

    return services_statistic


def parse_data(region_id_parsing: str):
    url = "https://fedstat.ru/indicator/dataGrid.do?id=31448"

    payload = f"lineObjectIds=0&lineObjectIds=30611&lineObjectIds=57831&lineObjectIds=58273&columnObjectIds=3&columnObjectIds=33560&selectedFilterIds=0_31448&selectedFilterIds=3_2022&selectedFilterIds=30611_950351&selectedFilterIds=33560_1540283&selectedFilterIds={region_id_parsing}&selectedFilterIds=58273_1709730&selectedFilterIds=58273_1709750&selectedFilterIds=58273_1709752&selectedFilterIds=58273_1754705&selectedFilterIds=58273_1754706&selectedFilterIds=58273_1754720&selectedFilterIds=58273_1754721&selectedFilterIds=58273_1754722&selectedFilterIds=58273_1754724&selectedFilterIds=58273_1754752&selectedFilterIds=58273_1754760&selectedFilterIds=58273_1754761&selectedFilterIds=58273_1754773&selectedFilterIds=58273_1754777&selectedFilterIds=58273_1754795&selectedFilterIds=58273_1754796&selectedFilterIds=58273_1754797&selectedFilterIds=58273_1754809&selectedFilterIds=58273_1754812&selectedFilterIds=58273_1754921&selectedFilterIds=58273_1754960&selectedFilterIds=58273_1754981&selectedFilterIds=58273_1755035&selectedFilterIds=58273_1755037&selectedFilterIds=58273_1755041&selectedFilterIds=58273_1755045&selectedFilterIds=58273_1755049&selectedFilterIds=58273_1755060&selectedFilterIds=58273_1755063&selectedFilterIds=58273_1755066&selectedFilterIds=58273_1755077&selectedFilterIds=58273_1755078&selectedFilterIds=58273_1755087&selectedFilterIds=58273_1755088&selectedFilterIds=58273_1755089&selectedFilterIds=58273_1755094&selectedFilterIds=58273_1755098&selectedFilterIds=58273_1755116&selectedFilterIds=58273_1755119&selectedFilterIds=58273_1755125&selectedFilterIds=58273_1755128&selectedFilterIds=58273_1755129&selectedFilterIds=58273_1755132&selectedFilterIds=58273_1755133&selectedFilterIds=58273_1755136&selectedFilterIds=58273_1755138&selectedFilterIds=58273_1755150&selectedFilterIds=58273_1755156&selectedFilterIds=58273_1755157&selectedFilterIds=58273_1755175&selectedFilterIds=58273_1755184&selectedFilterIds=58273_1755186&selectedFilterIds=58273_1755189&selectedFilterIds=58273_1755191&selectedFilterIds=58273_1755193&selectedFilterIds=58273_1755196&selectedFilterIds=58273_1755205&selectedFilterIds=58273_1755209&selectedFilterIds=58273_1755210&selectedFilterIds=58273_1759589&selectedFilterIds=58273_1785650&selectedFilterIds=58273_1785688&selectedFilterIds=58273_1785695&selectedFilterIds=58273_1785737&selectedFilterIds=58273_1785738&selectedFilterIds=58273_1785755&selectedFilterIds=58273_1785759&selectedFilterIds=58273_1785766&selectedFilterIds=58273_1785776&selectedFilterIds=58273_1836520&selectedFilterIds=58273_1836522&selectedFilterIds=58273_1836524&selectedFilterIds=58273_1836582&selectedFilterIds=58273_1836583&selectedFilterIds=58273_1836584&selectedFilterIds=58273_1836585&selectedFilterIds=58273_1836586&selectedFilterIds=58273_1848512"

    headers = {
        'Cookie': 'JSESSIONID=98EDA976FC3A897C5FA8FDCDA5A57180',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    request_result = json.loads(requests.request("POST", url, headers=headers, data=payload).text)
    services = {
        ('Стрижка модельная в женском зале, стрижка', 'Стрижка модельная в мужском зале, стрижка',
         'Химическая завивка волос, услуга', 'Маникюр,услуга'): Value(),
        ('Помывка в бане в общем отделении, билет'): Value(),
        ('Первичный консультативный прием у врача специалиста, посещение',
         'Ультразвуковое исследование брюшной полости, исследование',
         'Физиотерапевтическое лечение, процедура', 'Общий анализ крови, анализ',
         'Пребывание пациента в круглосуточном стационаре,койко день',
         'Первичный консультативный осмотр больного у стоматолога, посещение',
         'Удаление зуба под местным обезболиванием, удаление',
         'Лечение кариеса, пломба'): Value(),
        ('Ужин в ресторане, на 1 человека'): Value(),
        ('Обед в ресторане, на 1 человека', 'Кофе в организациях быстрого обслуживания, 200 г',
         'Обед в столовой, кафе, закусочной (кроме столовой в организации), на 1 человека',
         'Продукция предприятий общественного питания быстрого обслуживания (сэндвич типа "Гамбургер"), шт.'): Value(),
        ('Аренда индивидуального банковского сейфа, в расчете на месяц'): Value(),
        ('Проезд в трамвае, поездка'): Value(),
        ('Проезд в троллейбусе, поездка'): Value(),
        ('Проезд в такси, в расчете на 1 км пути'): Value(),
        ('Проезд в городском автобусе,поездка'): Value(),
        ('Проезд в пригородном поезде, поездка',
         'Проезд в купейном вагоне скорого нефирменного поезда дальнего следования, в расчете на 100 км пути',
         'Проезд в купейном вагоне скорого фирменного поезда дальнего следования, в расчете на 100 км пути',
         'Проезд в плацкартном вагоне скорого нефирменного поезда дальнего следования, в расчете на 100 км пути'): Value(),
        ('Услуги аренды автомобилей, час'): Value(),
        ('Кинотеатры, билет'): Value(),
        ('Театры, билет'): Value(),
        ('Музеи и выставки, билет'): Value(),
        ('Экскурсия автобусная, час'): Value(),
        ('Санаторий, день'): Value(),
        ('Услуги организатора проведения торжеств, услуга'): Value(),
        ('Экскурсионные туры по России, поездка'): Value(),
        ('Водка крепостью 40% об. спирта и выше, л', 'Вино виноградное крепленое крепостью до 20% об.спирта, л',
         'Вино виноградное столовое (сухое, полусухое, полусладкое) крепостью до 14% об.спирта и содержанием до 8% сахара, л',
         'Коньяк ординарный отечественный, л', 'Вино игристое отечественное, л', 'Вино виноградное крепленое, л',
         'Вино виноградное столовое, л', 'Пиво, л', 'Водка, л'): Value(),
        ('Вода минеральная и питьевая, л'): Value(),
        ('Напитки газированные, л'): Value(),
        ('Мороженое сливочное, кг', 'Мороженое сливочное отечественное, кг',
         'Мороженое сливочное импортное, 1000 мл'): Value(),
        ('Кофе натуральный растворимый, кг', 'Кофе натуральный в зернах и молотый, кг'): Value(),
        ('Чай черный байховый пакетированный, 25 пакетиков'): Value(),
        ('Аренда однокомнатной квартиры у частных лиц, месяц',
         'Аренда двухкомнатной квартиры у частных лиц, месяц')
        : Value(),
        ('Проживание в хостеле, сутки с человека'): Value(),
        ('Проживание в гостинице 1* или в мотеле, сутки с человека'): Value(),
        ('Проживание в гостинице 2*, сутки с человека', 'Проживание в гостинице 3*, сутки с человека'): Value(),
        ('Проживание в гостинице 4*-5*, сутки с человека', 'Дом отдыха, пансионат, день'): Value(),
        ('Бензин автомобильный марки АИ-92, л', 'Бензин автомобильный марки АИ-95, л', 'Дизельное топливо, л',
         'Бензин автомобильной марки,АИ-98,л', 'Бензин автомобильный'): Value(),
        ('Водоснабжение холодное и водоотведение, месяц с человека', 'Газ сетевой, месяц с человека',
         'Газ сжиженный, месяц с человека', 'Услуги по снабжению электроэнергией',
         'Водоснабжение холодное, месяц с человека', 'Водоотведение, месяц с человека',
         'Услуги по воспитанию детей, предоставляемые наемным персоналом,час', 'Услуги сиделок, час'): Value(),
        ('Книга детективно-приключенческого жанра, шт.', 'Книга художественная, шт.'): Value(),
        ('Клубная карта в фитнес-клуб, месяц'): Value(),
    }

    count_average_price_for_region(request_result, services)

    services[('Минимальная цена аппартаментов')] = Value()
    services[('Минимальная цена аппартаментов')].average_price = \
        min(services[('Проживание в гостинице 4*-5*, сутки с человека', 'Дом отдыха, пансионат, день')].average_price,
            services[('Аренда однокомнатной квартиры у частных лиц, месяц',
                      'Аренда двухкомнатной квартиры у частных лиц, месяц')].average_price,
            services[(('Проживание в хостеле, сутки с человека'))].average_price,
            services[('Проживание в гостинице 1* или в мотеле, сутки с человека')].average_price,
            services[(('Проживание в гостинице 2*, сутки с человека',
                       'Проживание в гостинице 3*, сутки с человека'))].average_price)

    services[('Максимальная цена аппартаментов')] = Value()
    services[('Максимальная цена аппартаментов')].average_price = \
        max(services[('Проживание в гостинице 4*-5*, сутки с человека', 'Дом отдыха, пансионат, день')].average_price,
            services[('Аренда однокомнатной квартиры у частных лиц, месяц',
                      'Аренда двухкомнатной квартиры у частных лиц, месяц')].average_price,
            services[(('Проживание в хостеле, сутки с человека'))].average_price,
            services[('Проживание в гостинице 1* или в мотеле, сутки с человека')].average_price,
            services[(('Проживание в гостинице 2*, сутки с человека',
                       'Проживание в гостинице 3*, сутки с человека'))].average_price)

    return services
