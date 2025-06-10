from django.urls import path

from digital_products.urls import urlpatterns
from .views import GatewayView, PaymentView

urlpatterns = [

    path('gateways/', GatewayView.as_view()),
    path('pay/', PaymentView.as_view())
]