from django.contrib import admin
from apps.stores.models import Store, Visit


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('store_and_employee', 'visit_date', 'longitude', 'latitude')
    search_fields = ('employee__name', 'store__title')