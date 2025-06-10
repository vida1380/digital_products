from django.urls import path

from digital_products.urls import urlpatterns
from .views import PackageView, SubscriptionView


urlpatterns = [

    path('packages/', PackageView.as_view()),
    path('subscriptions/', SubscriptionView.as_view())
]