from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Region, RegionStatistics
from .utils import parser_of_data


@receiver(post_save, sender=Region)
def post_save_region_statistics(sender, instance, **kwargs):
    region_statistics = RegionStatistics.objects.filter(region=instance)

    if len(region_statistics) == 0:
        services_statistic = parser_of_data.parse_data(instance.additional_information_for_parsing)

        RegionStatistics.objects.create(
            region=instance,
            beauty_master_services=services_statistic[
                ('Стрижка модельная в женском зале, стрижка', 'Стрижка модельная в мужском зале, стрижка',
                 'Химическая завивка волос, услуга', 'Маникюр,услуга')].average_price,
            going_to_the_bath=services_statistic[('Помывка в бане в общем отделении, билет')].average_price,
            medical_examination=services_statistic[('Первичный консультативный прием у врача специалиста, посещение',
                                                    'Ультразвуковое исследование брюшной полости, исследование',
                                                    'Физиотерапевтическое лечение, процедура',
                                                    'Общий анализ крови, анализ',
                                                    'Пребывание пациента в круглосуточном стационаре,койко день',
                                                    'Первичный консультативный осмотр больного у стоматолога, посещение',
                                                    'Удаление зуба под местным обезболиванием, удаление',
                                                    'Лечение кариеса, пломба')].average_price,
            lunch_at_restaurant=services_statistic[('Ужин в ресторане, на 1 человека')].average_price,
            lunch_at_catering=services_statistic[
                ('Обед в ресторане, на 1 человека', 'Кофе в организациях быстрого обслуживания, 200 г',
                 'Обед в столовой, кафе, закусочной (кроме столовой в организации), на 1 человека',
                 'Продукция предприятий общественного питания быстрого обслуживания (сэндвич типа "Гамбургер"), шт.')].average_price,
            safe_rental=services_statistic[
                ('Аренда индивидуального банковского сейфа, в расчете на месяц')].average_price,
            tram_thoroughfare=services_statistic[('Проезд в трамвае, поездка')].average_price,
            trolley_bus_thoroughfare=services_statistic[('Проезд в троллейбусе, поездка')].average_price,
            taxi_thoroughfare=services_statistic[('Проезд в такси, в расчете на 1 км пути')].average_price,
            bus_thoroughfare=services_statistic[('Проезд в городском автобусе,поездка')].average_price,
            local_train_thoroughfare=services_statistic[('Проезд в пригородном поезде, поездка',
                                                         'Проезд в купейном вагоне скорого нефирменного поезда дальнего следования, в расчете на 100 км пути',
                                                         'Проезд в купейном вагоне скорого фирменного поезда дальнего следования, в расчете на 100 км пути',
                                                         'Проезд в плацкартном вагоне скорого нефирменного поезда дальнего следования, в расчете на 100 км пути')].average_price,
            car_rental_services=services_statistic[('Услуги аренды автомобилей, час')].average_price,
            going_to_the_cinema=services_statistic[('Кинотеатры, билет')].average_price,
            going_to_the_theater=services_statistic[('Театры, билет')].average_price,
            going_to_the_museum=services_statistic[('Музеи и выставки, билет')].average_price,
            bus_tour=services_statistic[('Экскурсия автобусная, час')].average_price,
            sanatorium_day=services_statistic[('Санаторий, день')].average_price,
            event_organizer_services=services_statistic[
                ('Услуги организатора проведения торжеств, услуга')].average_price,
            excursion_tours=services_statistic[('Экскурсионные туры по России, поездка')].average_price,
            liter_of_alcohol=services_statistic[
                ('Водка крепостью 40% об. спирта и выше, л', 'Вино виноградное крепленое крепостью до 20% об.спирта, л',
                 'Вино виноградное столовое (сухое, полусухое, полусладкое) крепостью до 14% об.спирта и содержанием до 8% сахара, л',
                 'Коньяк ординарный отечественный, л', 'Вино игристое отечественное, л',
                 'Вино виноградное крепленое, л',
                 'Вино виноградное столовое, л', 'Пиво, л', 'Водка, л')].average_price,
            liter_of_water=services_statistic[('Вода минеральная и питьевая, л')].average_price,
            liter_of_soda=services_statistic[('Напитки газированные, л')].average_price,
            icecream=services_statistic[('Мороженое сливочное, кг', 'Мороженое сливочное отечественное, кг',
                                         'Мороженое сливочное импортное, 1000 мл')].average_price,
            coffee=services_statistic[
                ('Кофе натуральный растворимый, кг', 'Кофе натуральный в зернах и молотый, кг')].average_price,
            tea_bags=services_statistic[('Чай черный байховый пакетированный, 25 пакетиков')].average_price,
            premises_for_rent=services_statistic[('Аренда однокомнатной квартиры у частных лиц, месяц',
                                                  'Аренда двухкомнатной квартиры у частных лиц, месяц')].average_price,
            hostel_accommodation=services_statistic[('Проживание в хостеле, сутки с человека')].average_price,
            hotel_accommodation_economy=services_statistic[
                ('Проживание в гостинице 1* или в мотеле, сутки с человека')].average_price,
            hotel_accommodation_comfort=services_statistic[(
                'Проживание в гостинице 2*, сутки с человека',
                'Проживание в гостинице 3*, сутки с человека')].average_price,
            hotel_accommodation_lux=services_statistic[
                ('Проживание в гостинице 4*-5*, сутки с человека', 'Дом отдыха, пансионат, день')].average_price,
            liter_of_gasoline=services_statistic[
                ('Бензин автомобильный марки АИ-92, л', 'Бензин автомобильный марки АИ-95, л', 'Дизельное топливо, л',
                 'Бензин автомобильной марки,АИ-98,л', 'Бензин автомобильный')].average_price,
            utility_bills=services_statistic[
                ('Водоснабжение холодное и водоотведение, месяц с человека', 'Газ сетевой, месяц с человека',
                 'Газ сжиженный, месяц с человека', 'Услуги по снабжению электроэнергией',
                 'Водоснабжение холодное, месяц с человека', 'Водоотведение, месяц с человека',
                 'Услуги по воспитанию детей, предоставляемые наемным персоналом,час',
                 'Услуги сиделок, час')].average_price,
            book_price=services_statistic[
                ('Книга детективно-приключенческого жанра, шт.', 'Книга художественная, шт.')].average_price,
            gym=services_statistic[('Клубная карта в фитнес-клуб, месяц')].average_price,
            min_apartment_price=services_statistic[('Минимальная цена аппартаментов')].average_price,
            max_apartment_price=services_statistic[('Максимальная цена аппартаментов')].average_price
        )
