from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('saludar/<str:nombre>', views.saludar, name='saludar'),
    re_path('alumnos_por_anio/(?P<year>[0-9]{4})/$', views.alumnos_por_año, name='alumnos_por_anio')

]