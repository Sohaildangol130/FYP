from django.urls import path
from checkout.api.views import api_detail_checkout_view

app_name = "checkout"

urlpatterns = [
    path('<slug>', api_detail_checkout_view)
]