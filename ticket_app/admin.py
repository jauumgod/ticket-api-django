from django.contrib import admin
from .models import UserEmpresa, Empresas

class UserEmpresaAdmin(admin.ModelAdmin):
    list_display = ('user',)  # Adicione outros campos que deseja visualizar
    search_fields = ('user__username',)

admin.site.register(UserEmpresa, UserEmpresaAdmin)
admin.site.register(Empresas)
