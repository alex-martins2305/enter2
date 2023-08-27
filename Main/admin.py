from django.contrib import admin
from .models import Aposentados

class ListandoAposentados(admin.ModelAdmin):
    list_display =('mci','beneficio', 'conta','idade', 'analfabeto','limite_vigente', 'ultimo_atendimento')
    list_display_links=('mci','beneficio', 'conta','idade', 'analfabeto','limite_vigente', 'ultimo_atendimento')
    search_fields=('mci','beneficio', 'conta','idade', 'ultimo_atendimento')
    list_filter=('mci','beneficio', 'conta','idade', 'ultimo_atendimento')
    list_per_page=50

admin.site.register(Aposentados, ListandoAposentados)
