from django.urls import path
from .views import CollectListAPIView, PaymentListAPIView

urlpatterns = [
    path("collects/", CollectListAPIView.as_view()),
    path("payments/", PaymentListAPIView.as_view()),
]
