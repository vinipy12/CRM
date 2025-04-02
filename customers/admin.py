from django.contrib import admin
from .models import Empresa, Endereco, Representante
from files.models import Arquivo

class ArquivoInline(admin.TabularInline):
    model = Arquivo
    extra = 0
    fields = ('nome', 'ano', 'endereco')
    readonly_fields = ('ano', 'endereco')

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'cnpj', 'telefone')
    search_fields = ('nome_fantasia', 'cnpj')
    inlines = [ArquivoInline]
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('files')

class EmpresaInline(admin.TabularInline):
    model = Arquivo
    extra = 0
    fields = ('nome_fantasia', 'cnpj', 'endereco')
    readonly_fields = ('nome_fantasia', 'cnpj', 'endereco')

@admin.register(Representante)
class RepresentanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa', 'email')
    search_fields = ('nome', 'empresa', 'email')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('customers')

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('rua', 'bairro', 'cep', 'cidade', 'estado', 'pais')
    search_fields = ('rua', 'bairro', 'cep', 'cidade', 'estado', 'pais')
    