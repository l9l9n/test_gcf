from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import generics

from models import Collect, Payment
from serializers import CollectSerializer, PaymentSerializer


class CollectListAPIView(generics.ListAPIView):
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


