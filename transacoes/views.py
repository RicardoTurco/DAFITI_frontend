import os
import requests
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'transacoes/index.html', {'user': None})


def pessoas(request):
    url_pessoas = os.getenv('URL_API') + 'pessoas'
    response = requests.get(url_pessoas)
    pessoas = response.json()
    return render(request, 'transacoes/pessoas.html', {'pessoas': pessoas, 'status_pessoas': response.status_code})


def pessoa_v(request, idpessoa=None):
    url_pessoa = os.getenv('URL_API') + 'pessoas/id/' + idpessoa
    response_pessoa = requests.get(url_pessoa)
    pessoa = response_pessoa.json()
    return render(request, 'transacoes/pessoa_v.html', {'pessoa': pessoa})


def pessoa_new(request):
    return render(request, 'transacoes/pessoa_new.html')


def criar_pessoa(request):
    url_criar_pessoa = os.getenv('URL_API') + 'pessoas'

    pessoa = {
        'nome': request.POST.get('nome'),
        'cpf': request.POST.get('cpf'),
        'datanascimento': request.POST.get('datanascimento'),
        'username': request.POST.get('username'),
        'email': request.POST.get('email'),
        'password': request.POST.get('password')
    }
    response = requests.post(url_criar_pessoa, json=pessoa)
    return redirect('pessoas')


def deletar_pessoa(request, idpessoa=None):
    url_pessoa = os.getenv('URL_API') + 'pessoas/id/' + idpessoa

    response_pessoa = requests.delete(url_pessoa)
    return redirect('pessoas')


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


def contas(request):
    url_api = os.getenv('URL_API') + 'contas'
    response = requests.get(url_api)
    contas = response.json()
    return render(request, 'transacoes/contas.html', {'contas': contas, 'status_contas': response.status_code})


def conta_v(request, idconta=None):
    url_conta = os.getenv('URL_API') + 'contas/id/' + idconta
    url_transacoes_conta = os.getenv('URL_API') + 'transacoes/conta/' + idconta

    response_conta = requests.get(url_conta)
    response_transacoes_conta = requests.get(url_transacoes_conta)

    conta = response_conta.json()
    transacoes = response_transacoes_conta.json()
    return render(request, 'transacoes/conta_v.html', {'conta': conta, 'transacoes': transacoes, 'status_transacoes': response_transacoes_conta.status_code})


def conta_new(request):
    url_pessoas = os.getenv('URL_API') + 'pessoas'
    url_tp_contas = os.getenv('URL_API') + 'tipo-contas'

    response_pessoas = requests.get(url_pessoas)
    response_tp_contas = requests.get(url_tp_contas)

    pessoas = response_pessoas.json()
    tp_contas = response_tp_contas.json()
    return render(request, 'transacoes/conta_new.html', {'pessoas': pessoas, 'tp_contas': tp_contas})


def criar_conta(request):
    url_criar_conta = os.getenv('URL_API') + 'contas'

    conta = {
        'idpessoa': request.POST.get('idpessoa'),
        'limitesaquediario': float(request.POST.get('limitesaquediario')),
        'idtipoconta': request.POST.get('idtipoconta')
    }
    response = requests.post(url_criar_conta, json=conta)
    return redirect('contas')


def inativar_conta(request, idconta=None):
    url_conta = os.getenv('URL_API') + 'contas/id/' + idconta + '/inactivate'

    response = requests.patch(url_conta)
    return redirect('conta_v', idconta)


def ativar_conta(request, idconta=None):
    url_conta = os.getenv('URL_API') + 'contas/id/' + idconta + '/activate'

    response = requests.patch(url_conta)
    return redirect('conta_v', idconta)


def deletar_conta(request, idconta=None):
    url_transacoes_conta = os.getenv('URL_API') + 'transacoes/conta/' + idconta
    url_conta = os.getenv('URL_API') + 'contas/id/' + idconta

    response_transacoes = requests.delete(url_transacoes_conta)
    response_conta = requests.delete(url_conta)
    return redirect('contas')


def tp_transacoes(request):
    url_tp_transacoes = os.getenv('URL_API') + 'tipo-transacoes'
    response = requests.get(url_tp_transacoes)
    tp_transacoes = response.json()
    return render(request, 'transacoes/tipo_transacoes.html', {'tp_transacoes': tp_transacoes, 'status_tp_transacoes': response.status_code})


def tp_transacao_new(request):
    return render(request, 'transacoes/tipo_transacao_new.html')


def criar_tp_transacao(request):
    url_criar_tp_transacao = os.getenv('URL_API') + 'tipo-transacoes'

    tipo_transacao = {
        'tipotransacao': request.POST.get('tipotransacao'),
        'operacao': request.POST.get('operacao')
    }
    response = requests.post(url_criar_tp_transacao, json=tipo_transacao)
    return redirect('tipo_transacoes')


def deletar_tp_transacao(request, idtipotransacao=None):
    url_tp_transacao = os.getenv('URL_API') + 'tipo-transacoes/id/' + idtipotransacao

    response_tp_transacao = requests.delete(url_tp_transacao)
    return redirect('tipo_transacoes')


def transacao_new(request, idconta=None):
    url_conta = os.getenv('URL_API') + 'contas/id/' + idconta
    url_tp_transacoes = os.getenv('URL_API') + 'tipo-transacoes'

    response_conta = requests.get(url_conta)
    response_tp_transacoes = requests.get(url_tp_transacoes)

    conta = response_conta.json()
    tp_transacoes = response_tp_transacoes.json()
    return render(request, 'transacoes/transacao.html', {'conta': conta, 'tipo_transacoes': tp_transacoes})


def confirm_transacao(request):
    url_transacao = os.getenv('URL_API') + 'transacoes'

    transacao = {
        'idconta': request.POST.get('idconta'),
        'idtipotransacao': request.POST.get('idtipotransacao'),
        'valor': float(request.POST.get('valor'))
    }
    response = requests.post(url_transacao, json=transacao)
    return redirect('conta_v', request.POST.get('idconta'))


def delete_transacao(request, idconta=None, idtransacao=None):
    url_transacao = os.getenv('URL_API') + 'transacoes/id/' + idtransacao

    response = requests.delete(url_transacao)
    return redirect('conta_v', idconta)
