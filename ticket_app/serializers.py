from rest_framework import serializers
from .models import Empresas, Sequencia, Tickets, UserEmpresa, User, Imagens



class EmpresaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'
    
class SequenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequencia
        fields = '__all__'


class TicketSerializers(serializers.ModelSerializer):
    empresa = EmpresaSerializers(read_only=True)
    class Meta:
        model = Tickets
        fields = ['id', 'sequencia', 'criacao', 'placa','produto', 'transportadora', 'motorista','operador', 'cliente', 
                  'peso_entrada', 'peso_saida', 'peso_liquido', 'lote_leira', 'ticket_cancelado',
                  'usuario','empresa']
        read_only_fields = ['sequencia', 'criacao', 'empresa','usuario']

class UserOperacaoSerializer(serializers.ModelSerializer):
    empresas = serializers.PrimaryKeyRelatedField(queryset=Empresas.objects.all(), many=True)  # Permite selecionar múltiplas empresas
    username = serializers.CharField(source='user.username')  # Campo para username
    password = serializers.CharField(write_only=True)  # Campo para password

    class Meta:
        model = UserEmpresa
        fields = ['id', 'username', 'password', 'empresas']

    def create(self, validated_data):
        empresas = validated_data.pop('empresas', [])  # Remove empresas do validated_data
        user_data = validated_data.pop('user')  # Obtém os dados do usuário

        # Criação do usuário
        user = User.objects.create_user(username=user_data['username'], password=validated_data['password'])

        # Criação da instância UserEmpresa e associação das empresas
        user_empresa = UserEmpresa.objects.create(user=user)
        user_empresa.empresas.set(empresas)  # Associa as empresas ao usuário
        return user_empresa



class UserSerializers(serializers.ModelSerializer):
    tickets = TicketSerializers(many=True, read_only=True)
    empresas = serializers.SerializerMethodField()  # Usar SerializerMethodField para obter as empresas

    class Meta:
        model = User
        fields = ['username', 'tickets', 'empresas', 'permissions']

    def get_permissions(self, obj):
        return obj.get_all_permissions()
    
    def get_empresas(self, obj):
        # Obter a instância de UserOperacao associada ao usuário
        user_empresa = UserEmpresa.objects.filter(user=obj).first()
        if user_empresa:
            # Retorna as empresas associadas ao UserOperacao
            return EmpresaSerializers(user_empresa.empresas.all(), many=True).data
        return []


class ImagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagens
        fields = ['id', 'nome', 'imagem', 'ticket']