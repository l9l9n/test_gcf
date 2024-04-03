from django.contrib import admin
from .models import Collect, Payment


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'choice_occasion',
        'description',
        'target_amount',
        'collected_amount',
        'contributors_count_donations',
        'image_cover',
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
