from django.urls import path

from . import views


urlpatterns = [path("voltage", views.voltage, name="voltage")]
