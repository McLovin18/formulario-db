# formulario/urls.py
from django.urls import path
from .views import formulario_view, exito_view

urlpatterns = [
    path('', formulario_view, name='formulario'),
    path('exito/', exito_view, name='exito'),
]