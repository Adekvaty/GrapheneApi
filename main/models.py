from django.db import models

from django.db import models

class Person(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя',
        help_text='Укажите ваше имя (максимум 50 символов).'
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия',
        help_text='Укажите вашу фамилию (максимум 50 символов).'
    )
    has_license = models.BooleanField(
        default=False,
        verbose_name='Наличие водительских прав',
        help_text='Укажите, есть ли у вас водительские права.'
    )
    license_category = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        verbose_name='Категория прав',
        help_text='Укажите категорию водительских прав (например, B, C, A). Оставьте пустым, если нет прав.'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class Car(models.Model):
    owner = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='cars',
        verbose_name='Владелец',
        help_text='Укажите владельца автомобиля.'
    )
    model = models.CharField(
        max_length=50,
        verbose_name='Модель',
        help_text='Укажите модель автомобиля (максимум 50 символов).'
    )
    brand = models.CharField(
        max_length=50,
        verbose_name='Марка',
        help_text='Укажите марку автомобиля (максимум 50 символов).'
    )
    year = models.PositiveIntegerField(
        verbose_name='Год выпуска',
        help_text='Укажите год выпуска автомобиля.'
    )
    registration_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Регистрационный номер',
        help_text='Укажите уникальный регистрационный номер автомобиля.'
    )

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Brand(models.Model):
    name = models.CharField(
        max_length=144,
        verbose_name="Название бренда",
        help_text="Укажите имя бренда"
    )
    country = models.CharField(
        max_length=144,
        verbose_name="Страна происхождения",
        help_text="Страна, в которой основан бренд"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class Clothes(models.Model):
    type = models.CharField(
        max_length=255,
        verbose_name="Тип одежды",
        help_text="Укажите тип одежды, например, футболка, брюки, куртка и т.д."
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Название одежды",
        help_text="Укажите название одежды"
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name="Бренд",
        help_text="Выберите бренд для этой одежды"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        help_text="Укажите цену одежды"
    )
    material = models.CharField(
        max_length=255,
        verbose_name="Материал",
        help_text="Укажите материал, из которого сделана одежда"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return f"{self.name} ({self.brand.name})"
    
    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежда"
