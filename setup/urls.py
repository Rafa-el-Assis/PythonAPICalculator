from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from calculadoraVetorial.views import SomaView, AritimeticaView
from rest_framework import routers


router = DefaultRouter()
router.register('soma', SomaView, basename='Soma Vetorial')
router.register('aritimetica', AritimeticaView, basename='Media Aritimetica do Vetor')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
