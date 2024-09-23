from rest_framework import generics
from .models import Operacoes, UserOperacao, Sequencia, Tickets
from .serializers import (
    OperacoesSerializers, UserOperacaoSerializer,
    SequenciaSerializer, TicketSerializers
)

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions

#============OPERACAO===========
class OperacoesListCreateView(generics.ListCreateAPIView):
    queryset = Operacoes.objects.all()
    serializer_class = OperacoesSerializers


class OperacoesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Operacoes.objects.all()
    serializer_class = OperacoesSerializers


#=============USER==============
class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserOperacao.objects.all()
    serializer_class = UserOperacaoSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserOperacao.objects.all()
    serializer_class = UserOperacaoSerializer


#============Tickets=============
class TicketsListCreateView(generics.ListCreateAPIView):
    
    serializer_class = TicketSerializers

    def get_queryset(self):
        queryset = Tickets.objects.all()

        operacao = self.request.query_params.get('operacao')
        sequencia = self.request.query_params.get('sequencia')
        criacao = self.request.query_params.get('criacao')
    
        if operacao:
            queryset = queryset.filter(operacao__nome__icontains=operacao)
        if sequencia:
            queryset = queryset.filter(sequencia=sequencia)
        if criacao:
            queryset = queryset.filter(criacao=criacao)

        return queryset


class TicketsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializers


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
