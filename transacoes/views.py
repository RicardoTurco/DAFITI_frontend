import os
import requests
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'transacoes/index.html', {'user': None})


def tp_contas(request):
    url_tp_contas = os.getenv('URL_API') + 'tipo-contas'
    response = requests.get(url_tp_contas)
    tp_contas = response.json()
    return render(request, 'transacoes/tipo_contas.html', {'tp_contas': tp_contas, 'status_tp_contas': response.status_code})


def tp_conta_new(request):
    return render(request, 'transacoes/tipo_conta_new.html')


def criar_tp_conta(request):
    url_criar_tp_conta = os.getenv('URL_API') + 'tipo-contas'

    tipo_conta = {
        'tipoconta': request.POST.get('tipoconta')
    }
    response = requests.post(url_criar_tp_conta, json=tipo_conta)
    return redirect('tipo_contas')


def deletar_tp_conta(request, idtipoconta=None):
    url_tp_conta = os.getenv('URL_API') + 'tipo-contas/id/' + idtipoconta

    response_tp_conta = requests.delete(url_tp_conta)
    return redirect('tipo_contas')
