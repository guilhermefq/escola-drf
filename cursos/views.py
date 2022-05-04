"""Uso da generics views do Django Rest Framework"""
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

from rest_framework import viewsets
# para adicionar um método customizado, alterando ações padrão do Django Rest Framework
from rest_framework.decorators import action
from rest_framework.response import Response

"""
API V1
"""


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # Sobrescrevendo o método get_object para retornar o objeto
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                     curso=self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
API V2
"""


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # Criando a rota avaliacoes para acessar as avaliações do curso
    # Detail=Cria a rota para acessar o curso; methods=['get']=Apenas GET
    @action(methods=['get'], detail=True)
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        avaliacoes = curso.avaliacoes.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
