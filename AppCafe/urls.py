from django.urls import path
from AppCafe import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('variedad-cafe', views.variedadcafe, name="Variedad Cafe"),
    path('variedad-te', views.variedadte, name="Variedad Te"),
    path('variedad-gaseosa', views.variedadgaseosa, name="Variedad Gaseosa"),
    path('formscafe', views.formscafe, name="Formulario"),
]
