
from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'roll_number',
        'email',
        'age',
        'course',
    )
    search_fields = ('name', 'roll_number', 'email')
    list_filter = ('course',)
