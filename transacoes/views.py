from django.shortcuts import render


def index(request):
    return render(request, 'transacoes/index.html', {'user': None})
