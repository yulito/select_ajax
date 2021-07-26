import json
from django.db.models.fields import AutoField
from django.http.response import HttpResponse, HttpResponseServerError, JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from core.models import *
from django.core import serializers

# Create your views here.

def index(request):
    print('Estoy en index')
    cat = Categoria.objects.all()
    data = {'cat':cat}
    return render(request,'core/index.html' , data)

#DEVUELVE DATOS EN FORMA DE ARREGLO POR OBJETO
@csrf_exempt
def filtro(request):
    print('Estoy en filtro DJANGO')
    _cat = request.POST['cat']
    prod = list(Producto.objects.filter(categoriaa = _cat).values_list())
    return HttpResponse(json.dumps(prod))

#ESTE TAMBIEN FUNCIONA. Devuelve datos en forma de TUPLA O ARREGLO POR LISTAS
'''@csrf_exempt
def filtro(request):
    print('Estoy en filtro DJANGO')
    _cat = request.POST['cat']
    _prod = list(Producto.objects.filter(categoriaa = _cat).values_list())
    data = {'prod':_prod}
    return JsonResponse(data)'''

#ESTE NO FUNCIONA NI POR SI ACASO XD... NAAA, DICE QUE EL GET DEVUELVE MAS DE UN PRODUCTO, CONCRETAMENTE 3
'''@csrf_exempt
def filtro(request):
    print('Estoy en filtro DJANGO')
    _cat = request.POST['cat']
    for i in Producto.objects.get(categoriaa = _cat):
        prod=[i.idProducto, i.nomProducto, i.categoriaa.idCategoria]
    print(prod)
    data = {'prod':prod}
    return JsonResponse(data)'''
