
from django.contrib import admin
from .models import Customer, Meal, Subscription


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'available')
    search_fields = ('name',)
    list_filter = ('available',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'customer', 'plan_name',
        'start_date', 'end_date', 'amount'
    )
    search_fields = ('customer__name', 'plan_name')
