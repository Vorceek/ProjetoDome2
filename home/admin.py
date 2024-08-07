from django.contrib import admin
from .models import TabelaPessoa

class TabelaPessoaAdmin(admin.ModelAdmin):
    list_display = ('data', 'atividade', 'horaInicio', 'horaFim', 'duracao')
    readonly_fields = ('duracao',)  # Somente leitura para o campo duracao

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Se for edição
            return self.readonly_fields + ('duracao',)  # Adiciona duracao como readonly
        return self.readonly_fields

admin.site.register(TabelaPessoa, TabelaPessoaAdmin)
