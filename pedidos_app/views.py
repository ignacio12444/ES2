from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pedidos_app.serializers import cuentaSerializer


# 1) Crear una cuenta
@api_view(['POST','PUT'])
def crear_cuenta(request):
    datos_cuenta_deserializado = cuentaSerializer(data=request.data)

    if datos_cuenta_deserializado.is_valid(): # Validar 
        datos_cuenta_deserializado.save() # Guardar
        return Response(datos_cuenta_deserializado.data, status=status.HTTP_201_CREATED)
    else:
        return Response(datos_cuenta_deserializado.errors, status=status.HTTP_400_BAD_REQUEST)
    

# 2) Crear dos personajes para esa cuenta



#3) Modificar el correo electro nico de la cuenta creada

@api_view(['PATCH'])
def modificar_cliente(request):
    datos_cuenta_deserializado = cuentaSerializer(data=request.data)

    if datos_cuenta_deserializado.is_valid():
        datos_cuenta_deserializado.save()
        return repo
    pass