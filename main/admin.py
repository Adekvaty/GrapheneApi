from django.contrib import admin
from main.models import Brand, Clothes, Person, Car

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'has_license', 'license_category')  # Отображаемые поля
    search_fields = ('first_name', 'last_name')  # Поля для поиска
    list_filter = ('has_license', 'license_category')  # Фильтры для быстрой сортировки


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'registration_number', 'owner')  # Отображаемые поля
    search_fields = ('brand', 'model', 'registration_number')  # Поля для поиска
    list_filter = ('year', 'brand', 'owner')  # Фильтры для быстрой сортировки


admin.site.register(Brand)
admin.site.register(Clothes)