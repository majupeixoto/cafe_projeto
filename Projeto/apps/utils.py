# utils.py
from django.utils.dateparse import parse_date

def filtrar_ordens(request, ordens_queryset):
    # Filtro por status
    status = request.GET.get('status')
    if status:
        ordens_queryset = ordens_queryset.filter(status=status)

    # Filtro por data de criação
    data_criacao = request.GET.get('data_criacao')
    if data_criacao:
        try:
            date_obj = parse_date(data_criacao)
            if date_obj:
                ordens_queryset = ordens_queryset.filter(created_at__date=date_obj)
        except ValueError:
            pass  # Ignorar valores inválidos

    return ordens_queryset, status, data_criacao
