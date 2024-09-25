from rest_framework import generics
from .models import Empresas, UserEmpresa, Tickets
from .serializers import (
    EmpreasSerializers, UserOperacaoSerializer,
    TicketSerializers
)
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated



#============OPERACAO===========
class EmpresasListCreateView(generics.ListCreateAPIView):
    queryset = Empresas.objects.all()
    serializer_class = EmpreasSerializers


class EmpresasRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresas.objects.all()
    serializer_class = EmpreasSerializers


#=============USER==============
class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserEmpresa.objects.all()
    serializer_class = UserOperacaoSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserEmpresa.objects.all()
    serializer_class = UserOperacaoSerializer


#============Tickets=============
# class TicketsListCreateView(generics.ListCreateAPIView):
    
#     serializer_class = TicketSerializers

#     def get_queryset(self):
#         queryset = Tickets.objects.all()

#         operacao = self.request.query_params.get('operacao')
#         sequencia = self.request.query_params.get('sequencia')
#         criacao = self.request.query_params.get('criacao')
    
#         if operacao:
#             queryset = queryset.filter(operacao__nome__icontains=operacao)
#         if sequencia:
#             queryset = queryset.filter(sequencia=sequencia)
#         if criacao:
#             queryset = queryset.filter(criacao=criacao)

#         return queryset

#===========================TICKETS V2 - CREATE TICKET BASED ON TOKEN =========================


class TicketsListCreateView(generics.ListCreateAPIView):
    serializer_class = TicketSerializers
    permission_classes = [IsAuthenticated]  # Garante que o usuário esteja autenticado

    def get_queryset(self):
        queryset = Tickets.objects.all()

        # Obtendo os parâmetros da query
        empresa = self.request.query_params.get('empresa')
        sequencia = self.request.query_params.get('sequencia')
        criacao = self.request.query_params.get('criacao')

        # Filtrando com base nos parâmetros, se estiverem presentes
        if empresa:
            queryset = queryset.filter(empresa__nome__icontains=empresa)  # Corrigido: ajuste o campo para corresponder ao seu modelo
        if sequencia:
            queryset = queryset.filter(sequencia=sequencia)
        if criacao:
            queryset = queryset.filter(criacao=criacao)

        return queryset

    def perform_create(self, serializer):
        user = self.request.user  # Obtém o usuário autenticado a partir do token
        
        # Tenta obter a UserOperacao associada ao usuário
        user_empresa = UserEmpresa.objects.filter(user=user).first()  # Verifique se o nome do modelo está correto
        print(f'User: {user}, UserOperacao: {user_empresa}')

        if user_empresa is None:
            return Response(
                {'error': 'Usuário não está associado a nenhuma operação.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        empresa = user_empresa.empresas.first()  # Pega a primeira empresa associada
        print(f'Empresa: {empresa}')
        
        if empresa is None:
            return Response(
                {'error': 'Usuário não tem empresas associadas.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # Salva o ticket com o usuário e a operação automaticamente preenchidos
        serializer.save(usuario=user, empresa=empresa)




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
        
        # Verifica se existe o UserOperacao para o usuário
        try:
            user_empresa = UserEmpresa.objects.get(user=user)  # Corrigido para UserOperacao
            empresas = user_empresa.empresas.all()
        except UserEmpresa.DoesNotExist:
            empresas = []  # Se não existir, retorna uma lista vazia

        response_data = {
            'access': serializer.validated_data['access'],
            'refresh': serializer.validated_data['refresh'],
            'user_id': user.id,
            'username': user.username,
            'empresas': [empresa.id for empresa in empresas],  # Correção aqui
        }
        
        return Response(response_data)


