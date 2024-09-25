from rest_framework import serializers
from .models import Empresas, Sequencia, Tickets, UserEmpresa, User



class EmpreasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'
    
class SequenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequencia
        fields = '__all__'


class TicketSerializers(serializers.ModelSerializer):
    empresa = EmpreasSerializers(read_only=True)
    class Meta:
        model = Tickets
        fields = ['id', 'sequencia', 'criacao', 'placa','produto', 'transportadora', 'motorista','operador', 'cliente', 
                  'peso_entrada', 'peso_saida', 'peso_liquido', 'lote_leira', 'ticket_cancelado',
                  'usuario','empresa']
        read_only_fields = ['sequencia', 'criacao', 'empresa','usuario']

class UserOperacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmpresa
        fields = '__all__'


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
            return EmpreasSerializers(user_empresa.empresas.all(), many=True).data
        return []


