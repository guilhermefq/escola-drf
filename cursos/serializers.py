from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:  # Meta é um dicionário que define as configurações do serializer
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = ('__all__')


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('__all__')
