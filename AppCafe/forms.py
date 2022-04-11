from django import forms

class Pedido(forms.Form):
    nombre = forms.CharField()
    marca  = forms.CharField()
    precio = forms.IntegerField()