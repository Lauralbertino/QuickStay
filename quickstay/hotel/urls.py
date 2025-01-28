from django.urls import path
from .hotel import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hospedes/", views.listar_hospedes, name="listar_hospedes"),
    path("hospedes/novo/", views.criar_hospede, name="criar_hospede"),
    path("reservas/", views.listar_reservas, name="listar_reservas"),
    path("reservas/novo/", views.criar_reserva, name="criar_reserva"),
]
