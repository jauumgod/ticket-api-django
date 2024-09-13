from rest_framework import generics
from .models import Operacoes, UserOperacao, Sequencia, Tickets
from .serializers import (
    OperacoesSerializers, UserOperacaoSerializer,
    SequenciaSerializer, TicketSerializers
)

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
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializers

class TicketsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializers
