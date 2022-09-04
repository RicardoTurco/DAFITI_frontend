"""dafiti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from transacoes.views import index, tp_contas, tp_conta_new, criar_tp_conta, deletar_tp_conta, tp_transacoes, \
    tp_transacao_new, criar_tp_transacao, deletar_tp_transacao, pessoas, pessoa_v, pessoa_new, criar_pessoa, \
    deletar_pessoa, contas, conta_v, conta_new, criar_conta, inativar_conta, ativar_conta, deletar_conta, \
    transacao_new, confirm_transacao, delete_transacao


urlpatterns = [
    path('', index, name='index'),
    path('pessoas/', pessoas, name='pessoas'),
    path('pessoa-v/<str:idpessoa>', pessoa_v, name='pessoa_v'),
    path('pessoa-new/', pessoa_new, name='pessoa_new'),
    path('criar-pessoa/', criar_pessoa, name='criar_pessoa'),
    path('deletar-pessoa/<str:idpessoa>', deletar_pessoa, name='deletar_pessoa'),
    path('tipo-contas/', tp_contas, name='tipo_contas'),
    path('tipo-conta-new/', tp_conta_new, name='tipo_conta_new'),
    path('criar-tp-conta/', criar_tp_conta, name='criar_tp_conta'),
    path('deletar-tp-conta/<str:idtipoconta>', deletar_tp_conta, name='deletar_tp_conta'),
    path('contas/', contas, name='contas'),
    path('contas-v/<str:idconta>', conta_v, name='conta_v'),
    path('conta-new/', conta_new, name='conta_new'),
    path('criar-conta/', criar_conta, name='criar_conta'),
    path('inativar-conta/<str:idconta>', inativar_conta, name='inativar_conta'),
    path('ativar-conta/<str:idconta>', ativar_conta, name='ativar_conta'),
    path('deletar-conta/<str:idconta>', deletar_conta, name='deletar_conta'),
    path('tipo-transacoes/', tp_transacoes, name='tipo_transacoes'),
    path('tipo-transacao-new/', tp_transacao_new, name='tipo_transacao_new'),
    path('criar-tp-transacao/', criar_tp_transacao, name='criar_tp_transacao'),
    path('deletar-tp-transacao/<str:idtipotransacao>', deletar_tp_transacao, name='deletar_tp_transacao'),
    path('transacao-new/<str:idconta>', transacao_new, name='transacao_new'),
    path('confirm-transacao/', confirm_transacao, name='confirm_transacao'),
    path('delete-transacao/<str:idconta>/<str:idtransacao>', delete_transacao, name='delete_transacao'),
    path('admin/', admin.site.urls),
]
