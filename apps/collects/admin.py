from django.contrib import admin
from .models import Collect, Payment


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'occasion',
        'target_amount',
        'current_amount',
        'contributors_count',
        'end_date'
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'collect',
        'contributor',
        'amount',
        'timestamp'
    )
