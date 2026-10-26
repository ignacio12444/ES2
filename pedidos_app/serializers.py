from rest_framework import serializers
from pedidos_app.models import cuenta


class cuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = cuenta
        fields = '__all__'

class CuentaPersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaPersonaje
        fields = '__all__'

class CuentaPersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaPersonaje
        fields = '__all__'

class Item (serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'