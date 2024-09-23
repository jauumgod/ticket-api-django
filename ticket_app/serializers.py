from rest_framework import serializers
from .models import Operacoes, Sequencia, Tickets, UserOperacao, User



class OperacoesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Operacoes
        fields = '__all__'
    
class SequenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequencia
        fields = '__all__'


class TicketSerializers(serializers.ModelSerializer):
    operacao = OperacoesSerializers(read_only=True)
    class Meta:
        model = Tickets
        fields = ['id', 'sequencia', 'criacao', 'placa','produto', 'transportadora', 'motorista','operador', 'cliente', 
                  'peso_entrada', 'peso_saida', 'peso_liquido', 'lote_leira', 'ticket_cancelado',
                  'usuario','operacao']
        read_only_fields = ['sequencia', 'criacao', 'operacao','usuario']

class UserOperacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOperacao
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    tickets = TicketSerializers(many=True, read_only=True)
    empresas = OperacoesSerializers(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'tickets', 'empresas']

