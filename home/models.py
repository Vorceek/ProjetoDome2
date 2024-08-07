from django.db import models
from datetime import datetime, timedelta

class TabelaPessoa(models.Model):
    data = models.DateField(null=False, blank=False)
    atividade = models.CharField(null=False, max_length=200, blank=False)
    horaInicio = models.TimeField(null=False, blank=False)
    horaFim = models.TimeField(null=False, blank=False)
    duracao = models.DurationField(null=True, blank=True)  # Opcional, calculado automaticamente

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        ordering = ['data']

    def save(self, *args, **kwargs):
        # Calcula a duração antes de salvar
        if self.horaInicio and self.horaFim:
            dt_inicio = datetime.combine(self.data, self.horaInicio)
            dt_fim = datetime.combine(self.data, self.horaFim)
            
            if dt_fim < dt_inicio:
                dt_fim += timedelta(days=1)  # Adiciona um dia se a hora de fim for antes da hora de início
            
            self.duracao = dt_fim - dt_inicio
        
        super(TabelaPessoa, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.atividade} ({self.data})"
