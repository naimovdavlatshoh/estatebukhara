

from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Category(models.Model):
    title = models.CharField('Загаловок', max_length=256)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return str(self.title)

class Estate(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category', related_name='category_detail')
    title = models.CharField('Загаловок', max_length=256)
    image = models.FileField('Фото', blank=True, null=True)
    content = models.TextField('Описание', blank=True)
    price_usd = models.IntegerField('Цена в долларах', default=0)
    address = models.TextField('Адрес', blank=True)
    square = models.IntegerField('Площадь',blank=True, default=0)
    rooms = models.IntegerField('Кол-во комнат', blank=True, default=0)
    floor_number = models.IntegerField('Этаж дома', blank=True, default=0)
    floor = models.IntegerField('Этажность', blank=True, default=0)
    ceiling = models.IntegerField('Высота потолка', blank=True, default=0)
    bathroom = models.BooleanField('Санузел', blank=True, default=False)
    furniture = models.BooleanField('Мебилирован', blank=True, default=False)
    total_square = models.IntegerField('Общая Площадь', blank=True, default=0)
    house_square = models.IntegerField('Жилая Площадь', blank=True, default=0)
    electricity = models.BooleanField('Электричество', blank=True, default=False)
    gas = models.BooleanField('Газ', blank=True, default=False)
    heating = models.BooleanField('Отопление', blank=True, default=False)
    water = models.BooleanField('Вода', blank=True, default=False)
    sewerage = models.BooleanField('Канализация', blank=True, default=False)

    REPAIR = (
            ('V1', ('Евроремонт')), 
            ('V2', ('Средний')),
            ('V3', ('Старый')),
            ('V4', ('Требует ремонта')),
            ('V5', ('Коробка')),
        )
    repair = models.CharField('Ремонт', blank=True, max_length=300, choices = REPAIR, null=True)

    BUILDING_TYPE = (
        ('V1', ('Панельная')),
        ('V2', ('Кирпичная')),
        ('V3', ('Древесная')),
    )
    building_type = models.CharField('Тип строения', blank=True, max_length=300, choices = BUILDING_TYPE, null=True)


    PLAN = (
        ('V1', ('Раздельная')),
        ('V2', ('Смежная')),
        ('V3', ('Раздельно-смежная')),
    )
    plan = models.CharField('Планировка', blank=True, max_length=300, choices = PLAN, null=True)

    availibility = models.BooleanField('Availibility', default=False)
    parking = models.BooleanField('Парковка', default=False)
    is_favourite = models.BooleanField(default=False)





class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favourites', verbose_name='User')
    flat = models.ForeignKey(Estate, null=True, on_delete=models.CASCADE, related_name='product_favourites', verbose_name='Пост')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


    def __str__(self):
        return str(self.user.username)


class View(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user")
    product = models.ForeignKey(Estate, on_delete=models.CASCADE, verbose_name="recomendations")

    

    class Meta:
        verbose_name = 'Recomendation'
        verbose_name_plural = 'Recomendations'


    def __str__(self):
        return str(self.product)





class Gallery(models.Model):
    images = models.ForeignKey(Estate, on_delete=models.CASCADE, related_name='user_favourites', verbose_name='Flat')
    gallery = models.FileField('Галерея', blank=True, null=True)

    

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'