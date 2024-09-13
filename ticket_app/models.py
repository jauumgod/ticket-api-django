from django.db import models
from django.contrib.auth.models import User


class Operacoes(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    criacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome
    

class UserOperacao(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresas = models.ManyToManyField(Operacoes, related_name='usuarios')
    

class Sequencia(models.Model):
    operacao = models.OneToOneField(Operacoes, on_delete=models.CASCADE, related_name='sequencia')
    proximo_numero = models.IntegerField(default=1)

    def gerar_sequencia(self):
        numero_atual = self.proximo_numero
        self.proximo_numero +=1
        self.save()
        return numero_atual
    
    def __str__(self):
        return f'Sequencia para {self.operacao.nome}'


class Tickets(models.Model):
    sequencia = models.IntegerField(null=True, blank=True)
    criacao = models.DateField(auto_now_add=True)
    placa = models.CharField(max_length=100)
    transportadora = models.CharField(max_length=255)
    motorista = models.CharField(max_length=255)
    cliente = models.CharField(max_length=255)
    peso_entrada = models.FloatField()
    peso_saida = models.FloatField()
    peso_liquido = models.FloatField()
    lote_leira = models.CharField(max_length=100)
    ticket_cancelado = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    operacao = models.ForeignKey(Operacoes, on_delete=models.CASCADE, related_name='tickets')

    def save(self, *args, **kwargs):
        if self.pk is None:  # Somente gerar para um novo ticket
            sequencia_obj, created = Sequencia.objects.get_or_create(operacao=self.operacao)
            self.sequencia = sequencia_obj.gerar_sequencia()
        
        # Chama o método save do modelo pai corretamente
        super().save(*args, **kwargs)




#JK0125242 LOTE EXEMPLO

