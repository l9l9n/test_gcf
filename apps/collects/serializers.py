from rest_framework import serializers

from group_cash_fees.apps.collects.models import Collect, Payment


class CollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collect
        fields = (
            'author_fees',
            'title',
            'choice_occasion',
            'description',
            'target_amount',
            'collected_amount',
            'contributors_count_donations',
            'image_cover',
            'end_date',
        )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'collect',
            'contributor',
            'amount',
            'timestamp',
        )
