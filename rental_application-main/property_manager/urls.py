from django.urls import path
from .models import Property
from property_manager import views


urlpatterns = [
    path("property_manager/", views.propertypost.as_view(), name="property deatils"),
]
