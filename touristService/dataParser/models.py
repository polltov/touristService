from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Tags(models.Model):
    title = models.CharField(verbose_name="Название тега", max_length=50)

    def __str__(self):
        return self.title


class Region(models.Model):
    title = models.CharField(max_length=50, null=False)
    additional_information_for_parsing = models.CharField(max_length=100, null=False)
    rating = models.IntegerField(null=False, validators=[MinValueValidator(Decimal('1'))])
    short_definition = models.CharField(verbose_name="Короткое описание", max_length=200)
    long_definition = models.TextField(verbose_name="Длинное описание")
    image = models.ImageField(verbose_name='Изображение региона', blank=True, null=True, upload_to='images')
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.CharField(max_length=50, null=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    text = models.TextField()

    class RatingChoices(models.IntegerChoices):
        FIRST_CHOICE = 5, 'Отлично'
        SECOND_CHOICE = 4, 'Хорошо'
        THIRD_CHOICE = 3, 'Удовлетворительно'
        FORTH_CHOICE = 2, 'Плохо'
        FIFTH_CHOICE = 1, 'Ужасно'

    rating = models.IntegerField(choices=RatingChoices.choices)

    def __str__(self):
        return self.author


class RegionStatistics(models.Model):
    max_digits = 100
    decimal_places = 2

    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    beauty_master_services = models.DecimalField(verbose_name="Средняя цена услуги мастера в салоне красоты",
                                                 max_digits=max_digits, decimal_places=decimal_places, blank=True,
                                                 null=True, validators=[MinValueValidator(Decimal('0.01'))])
    going_to_the_bath = models.DecimalField(verbose_name="Поход в баню", max_digits=max_digits,
                                            decimal_places=decimal_places,
                                            blank=True, null=True, validators=[MinValueValidator(Decimal('0.01'))])
    medical_examination = models.DecimalField(verbose_name="Поход к врачу", max_digits=max_digits,
                                              decimal_places=decimal_places, blank=True, null=True,
                                              validators=[MinValueValidator(Decimal('0.01'))])
    lunch_at_restaurant = models.DecimalField(verbose_name="Средний чек в заведениях премиум класса",
                                              max_digits=max_digits,
                                              decimal_places=decimal_places, blank=True, null=True,
                                              validators=[MinValueValidator(Decimal('0.01'))])
    lunch_at_catering = models.DecimalField(verbose_name="Средний чек в заведениях общепита", max_digits=max_digits,
                                            decimal_places=decimal_places, blank=True, null=True,
                                            validators=[MinValueValidator(Decimal('0.01'))])
    safe_rental = models.DecimalField(verbose_name="Аренда сейфа", max_digits=max_digits, decimal_places=decimal_places,
                                      blank=True, null=True, validators=[MinValueValidator(Decimal('0.01'))])
    tram_thoroughfare = models.DecimalField(verbose_name="Проезд в трамвае", max_digits=max_digits,
                                            decimal_places=decimal_places, blank=True, null=True,
                                            validators=[MinValueValidator(Decimal('0.01'))])
    trolley_bus_thoroughfare = models.DecimalField(verbose_name="Проезд в троллейбусе", max_digits=max_digits,
                                                   decimal_places=decimal_places, blank=True, null=True,
                                                   validators=[MinValueValidator(Decimal('0.01'))])
    taxi_thoroughfare = models.DecimalField(verbose_name="Проезд в такси", max_digits=max_digits,
                                            decimal_places=decimal_places,
                                            blank=True, null=True, validators=[MinValueValidator(Decimal('0.01'))])
    bus_thoroughfare = models.DecimalField(verbose_name="Проезд в городском автобусе", max_digits=max_digits,
                                           decimal_places=decimal_places, blank=True, null=True,
                                           validators=[MinValueValidator(Decimal('0.01'))])
    local_train_thoroughfare = models.DecimalField(verbose_name="Проезд в пригородном поезде", max_digits=max_digits,
                                                   decimal_places=decimal_places, blank=True, null=True,
                                                   validators=[MinValueValidator(Decimal('0.01'))])
    car_rental_services = models.DecimalField(verbose_name="Услуги аренды автомобилей, час", max_digits=max_digits,
                                              decimal_places=decimal_places, blank=True, null=True,
                                              validators=[MinValueValidator(Decimal('0.01'))])
    going_to_the_cinema = models.DecimalField(verbose_name="Поход в кинотеатр", max_digits=max_digits,
                                              decimal_places=decimal_places, blank=True, null=True,
                                              validators=[MinValueValidator(Decimal('0.01'))])
    going_to_the_theater = models.DecimalField(verbose_name="Поход в театр", max_digits=max_digits,
                                               decimal_places=decimal_places, blank=True, null=True,
                                               validators=[MinValueValidator(Decimal('0.01'))])
    going_to_the_museum = models.DecimalField(verbose_name="Поход в музей", max_digits=max_digits,
                                              decimal_places=decimal_places, blank=True, null=True,
                                              validators=[MinValueValidator(Decimal('0.01'))])
    bus_tour = models.DecimalField(verbose_name="Автобусная экскурсия", max_digits=max_digits,
                                   decimal_places=decimal_places,
                                   blank=True, null=True, validators=[MinValueValidator(Decimal('0.01'))])
    sanatorium_day = models.DecimalField(verbose_name="Посещение санатория (день)", max_digits=max_digits,
                                         decimal_places=decimal_places, blank=True, null=True,
                                         validators=[MinValueValidator(Decimal('0.01'))])
    event_organizer_services = models.DecimalField(verbose_name="Услуги организатора проведения торжеств",
                                                   max_digits=max_digits, decimal_places=decimal_places, blank=True,
                                                   null=True, validators=[MinValueValidator(Decimal('0.01'))])
    excursion_tours = models.DecimalField(verbose_name="Экскурсионные туры по России", max_digits=max_digits,
                                          decimal_places=decimal_places, blank=True, null=True,
                                          validators=[MinValueValidator(Decimal('0.01'))])
    liter_of_alcohol = models.DecimalField(verbose_name="Алкоголь (литр)", max_digits=max_digits,
                                           decimal_places=decimal_places,
                                           blank=True, null=True, validators=[MinValueValidator(Decimal('0.01'))])
    liter_of_water = models.DecimalField(verbose_name="Вода (литр)", max_digits=max_digits,
                                         decimal_places=decimal_places,
                                         blank=True, null=True, validators=[MinValueValidator(Decimal('0.01'))])
    liter_of_soda = models.DecimalField(verbose_name="Напитки газированные (литр)", max_digits=max_digits,
                                        decimal_places=decimal_places, blank=True, null=True,
                                        validators=[MinValueValidator(Decimal('0.01'))])
    icecream = models.DecimalField(verbose_name="Мороженное (килограмм)", max_digits=max_digits,
                                   decimal_places=decimal_places,
                                   blank=True, null=True, validators=[MinValueValidator(Decimal('0.01'))])
    coffee = models.DecimalField(verbose_name="Кофе (килограмм)", max_digits=max_digits, decimal_places=decimal_places,
                                 blank=True, null=True, validators=[MinValueValidator(Decimal('0.01'))])
    tea_bags = models.DecimalField(verbose_name="Чай в пакетика (25 пакетиков)", max_digits=max_digits,
                                   decimal_places=decimal_places, blank=True, null=True,
                                   validators=[MinValueValidator(Decimal('0.01'))])
    premises_for_rent = models.DecimalField(verbose_name="Аренда помещения", max_digits=max_digits,
                                            decimal_places=decimal_places, blank=True, null=True,
                                            validators=[MinValueValidator(Decimal('0.01'))])
    hostel_accommodation = models.DecimalField(verbose_name="Проживание в хостеле", max_digits=max_digits,
                                               decimal_places=decimal_places, blank=True, null=True,
                                               validators=[MinValueValidator(Decimal('0.01'))])
    hotel_accommodation_economy = models.DecimalField(verbose_name="Проживание в гостинице (эконом)",
                                                      max_digits=max_digits,
                                                      decimal_places=decimal_places, blank=True, null=True,
                                                      validators=[MinValueValidator(Decimal('0.01'))])
    hotel_accommodation_comfort = models.DecimalField(verbose_name="Проживание в гостинице (комфорт)",
                                                      max_digits=max_digits,
                                                      decimal_places=decimal_places, blank=True, null=True,
                                                      validators=[MinValueValidator(Decimal('0.01'))])
    hotel_accommodation_lux = models.DecimalField(verbose_name="Проживание в гостинице (Люкс)", max_digits=max_digits,
                                                  decimal_places=decimal_places, blank=True, null=True,
                                                  validators=[MinValueValidator(Decimal('0.01'))])
    liter_of_gasoline = models.DecimalField(verbose_name="Бензин (литр)", max_digits=max_digits,
                                            decimal_places=decimal_places,
                                            blank=True, null=True, validators=[MinValueValidator(Decimal('0.01'))])
    utility_bills = models.DecimalField(verbose_name="Коммунальные услуги", max_digits=max_digits,
                                        decimal_places=decimal_places, blank=True, null=True,
                                        validators=[MinValueValidator(Decimal('0.01'))])
    book_price = models.DecimalField(verbose_name="Стоимость книги", max_digits=max_digits,
                                     decimal_places=decimal_places,
                                     blank=True, null=True, validators=[MinValueValidator(Decimal('0.01'))])
    gym = models.DecimalField(verbose_name="Клубная карта в фитнес-клуб, месяц", max_digits=max_digits,
                              decimal_places=decimal_places, blank=True, null=True,
                              validators=[MinValueValidator(Decimal('0.01'))])
    min_apartment_price = models.DecimalField(verbose_name="Минимальная плата за аппартаменты", max_digits=max_digits,
                                              decimal_places=decimal_places, blank=True, null=True,
                                              validators=[MinValueValidator(Decimal('0.01'))])

    max_apartment_price = models.DecimalField(verbose_name="Максимальная плата за аппартаменты", max_digits=max_digits,
                                              decimal_places=decimal_places, blank=True, null=True,
                                              validators=[MinValueValidator(Decimal('0.01'))])

    def __str__(self):
        # TODO MAYBE WE NEED TO RETURN region_title
        return f"{self.region.title}. Статистика."
