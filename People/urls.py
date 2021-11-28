from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("info/<int:pID>", views.info, name="info")
]