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
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # Hyperlinked Related Field
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name='avaliacao-detail')

    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = ('__all__')
