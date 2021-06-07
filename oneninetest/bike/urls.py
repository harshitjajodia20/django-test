from django.urls import path
from . import views

urlpatterns = [
    path('bike', views.bike,name="bike"),
]
