from rest_framework import generics
from .models import Operacoes, UserOperacao, Sequencia, Tickets
from .serializers import (
    OperacoesSerializers, UserOperacaoSerializer,
    TicketSerializers
)
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Adicione campos personalizados ao token
        token['user_id'] = user.id
        token['username'] = user.username
        # token['empresa'] = [empresa.id for empresa in user.empresa.all()]

        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.user
        user_operacao = UserOperacao.objects.get(user=user)
        empresas = user_operacao.empresas.all()

        response_data = {
            'access': serializer.validated_data['access'],
            'refresh': serializer.validated_data['refresh'],
            'user_id': user.id,
            'username': user.username,
            'empresas': [operacao.id for operacao in empresas],  # Adicione as empresas aqui
        }
        
        return Response(response_data)

