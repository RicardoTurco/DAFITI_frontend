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
    tp_transacao_new, criar_tp_transacao, deletar_tp_transacao


urlpatterns = [
    path('', index, name='index'),
    path('tipo-contas/', tp_contas, name='tipo_contas'),
    path('tipo-conta-new/', tp_conta_new, name='tipo_conta_new'),
    path('criar-tp-conta/', criar_tp_conta, name='criar_tp_conta'),
    path('deletar-tp-conta/<str:idtipoconta>', deletar_tp_conta, name='deletar_tp_conta'),
    path('tipo-transacoes/', tp_transacoes, name='tipo_transacoes'),
    path('tipo-transacao-new/', tp_transacao_new, name='tipo_transacao_new'),
    path('criar-tp-transacao/', criar_tp_transacao, name='criar_tp_transacao'),
    path('deletar-tp-transacao/<str:idtipotransacao>', deletar_tp_transacao, name='deletar_tp_transacao'),
    path('admin/', admin.site.urls),
]
