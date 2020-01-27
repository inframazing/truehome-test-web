from django.urls import path
from . import views

urlpatterns = [
    path("", views.propiedad_index, name="propiedad_index"),
    path("<int:pk>/", views.propiedad_detail, name="propiedad_detail"),
]
