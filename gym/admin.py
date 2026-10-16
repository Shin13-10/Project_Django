
from django.contrib import admin
from .models import Member, Trainer


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'phone', 'email',
        'membership_type', 'start_date', 'end_date', 'fee'
    )
    search_fields = ('name', 'email', 'phone')
    list_filter = ('membership_type',)


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'phone', 'salary')
    search_fields = ('name', 'specialization', 'phone')
