from rest_framework import serializers
from .models import Operacoes, Sequencia, Tickets, UserOperacao


class OperacoesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Operacoes
        fields = '__all__'
    
class SequenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequencia
        fields = '__all__'

class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ['id', 'sequencia', 'criacao', 'placa', 'transportadora', 'motorista', 'cliente', 
                  'peso_entrada', 'peso_saida', 'peso_liquido', 'lote_leira', 'ticket_cancelado',
                  'usuario','operacao']
        read_only_fields = ['sequencia', 'criacao']

class UserOperacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOperacao
        fields = '__all__'

