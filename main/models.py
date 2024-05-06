from django.db import models

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
