from rest_framework import serializers
from django.db.models import Avg
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:  # Meta é um dicionário que define as configurações do serializer
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = ('__all__')

    # Seguir o padrão: validate_nomedocampo
    def validate_avaliacao(self, valor):
        if valor in range(0, 6):
            return valor
        return serializers.ValidationError('A avaliação deve estar entre 1 e 5')


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # Hyperlinked Related Field
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name='avaliacao-detail')

    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # Criando o campo media_avaliacoes
    # SerializerMethodField indica que o campo é alimentado por uma função
    media_avaliacoes = serializers.SerializerMethodField()

    # Criando a função para calculo da média, para alimentar o campo media_avaliacoes
    # Deve-se manter o padrão get_nomedocampo
    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(
            Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2

    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'url', 'criacao',
                  'ativo', 'avaliacoes', 'media_avaliacoes')
