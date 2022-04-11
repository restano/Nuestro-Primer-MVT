from django.http import HttpResponse
from django.shortcuts import render
from AppCafe.models import VariedadCafe,VariedadTe,VariedadGaseosa

def VariedadCafe(request):

    variedadcafe = VariedadCafe (nombre=" ", marca=" ", precio=" ")
    variedadcafe.save()
    pedido = f"VariedadCafe: {variedadcafe.nombre} VariedadCafe: {variedadcafe.marca} VariedadCafe: {variedadcafe.precio}"

    return HttpResponse(pedido)

def VariedadTe(request):

    variedadte = VariedadTe (nombre=" ", marca=" ", precio=" ")
    variedadte.save()
    pedido = f"VariedadTe: {variedadte.nombre} VariedadTe: {variedadte.marca} VariedadTe: {variedadte.precio}"

    return HttpResponse(pedido)

def VariedadGaseosa(request):

    variedadgaseosa = VariedadGaseosa (nombre=" ", marca=" ", precio=" ")
    variedadgaseosa.save()
    pedido = f"VariedadGaseosa: {variedadgaseosa.nombre} VariedadGaseosa: {variedadgaseosa.marca} VariedadGaseosa: {variedadgaseosa.precio}"

    return HttpResponse(pedido)



def inicio(request):

    return render(request, "inicio.html")

def variedadcafe(request):

    return render(request, "variedadcafe.html")

def variedadte(request):

    return render(request, "variedadte.html")

def variedadgaseosa(request):

    return render(request, "variedadgaseosa.html")

def formscafe(request):

    return render(request, "formscafe.html")

# def buscar(request):

#     if request.GET['pedido']:

#         pedido = request.GET['pedido']
#         variedad = request.GET['Variedad']


from AppCafe.forms import Pedido