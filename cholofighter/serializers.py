from rest_framework import serializers
from .models import Personaje


class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = ('nombre', 'icono')
