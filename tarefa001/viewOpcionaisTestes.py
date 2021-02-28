#coding: utf-8

from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from service.views.viewEmpresa import atualiza_dados_magento
try:
	from django.utils import simplejson as json
except:
	import simplejson as json
from django.views.decorators.gzip import gzip_page
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from service.utilitarios import pesquisa, funcoes, sequenciador, gerar_relatorio, requisicoes
from service.gerador_planilha import gerador_planilha_opcionaisTestes
from service.dao import gravarDados
from service.dao.models import tabela_opcionais_testes

from service.utilitarios.gerador_relatorio_opcionaisTestes_pdf import gerar_relatorio as relfin
from decimal import Decimal
import xlrd, requests
from datetime import datetime


def opcional(request):
	try:
		codregistro, chave, staff, configs = funcoes.validaLoginSessao(request)
		if codregistro == None:
			return HttpResponseRedirect('/login')
		elif codregistro == 'EXPIRADO':
			return HttpResponseRedirect('/pagina_licenca_vencida')
		else:
			if funcoes.verificarPermissaoUsuario(request, codregistro, "opcional", None):
				context = Context({
					'configs': configs,
					'codregistro': codregistro,
					'modulo': funcoes.verificarOpcoesModulo(codregistro),
					'permissoes': funcoes.verificarOpcoesMenu(request),
					'staff': staff
				})
				return render(request, 'opcionais_de_testes.html', context)
	except:
		pass
	return HttpResponseRedirect('/pagina_erro')

campos = [
	['nome', 'Nome', 'string'], 
	['sigla', 'Sigla', 'string'], 
	['unidade', 'Unidade', 'decimal'], 
	['ativo', 'Status', 'status'],
	['observacao', 'Observação', 'string']
]

@gzip_page
@require_http_methods(['GET'])
def pesquisar_opcionaisTestes(request):
	try:
		codregistro, chave, staff, configs = funcoes.validaLoginSessao(request)
		if codregistro == None:
			return HttpResponseRedirect('/login')
		elif codregistro == 'EXPIRADO':
			return HttpResponseRedirect('/pagina_licenca_vencida')
		else:
			(valor, multi_valor, lista_campos_pesquisa, padraoPesquisa, campo_ordenacao, 
				tipo_ordenacao, tipo, tamanho_pagina, inicial) = pesquisa.getDados(request)

			sql  = 'SELECT o.nome, o.sigla, o.unidade, '
			sql += '(CASE o.ativo '
			sql += '    WHEN \'1\' THEN \'Ativo\' '
			sql += '    WHEN \'0\' THEN \'Inativo\' '
			sql += 'END)AS ativo, o.observacao '
			
			sql += 'FROM tabela_opcionais_testes o '
			sql += 'WHERE o.codregistro LIKE \'%s\' ' % codregistro

			if tipo == 'ativos':
				sql += 'AND o.ativo = 1 '
			elif tipo == 'inativos':
				sql += 'AND o.ativo = 0 '

			if lista_campos_pesquisa != '' and (valor != '' or multi_valor != ''):
				sql += pesquisa.montarFiltros(valor, multi_valor, lista_campos_pesquisa, padraoPesquisa)

			if campo_ordenacao != '':
				sql += 'ORDER BY %s ' % campo_ordenacao
				sql += 'ASC ' if (tipo_ordenacao == 0) else 'DESC '

			if tamanho_pagina != -1:
				sql += 'LIMIT %d, %d' % (inicial, (tamanho_pagina + 1))

			db = funcoes.connectMySql()
			db.query(sql)
			lista = db.use_result().fetch_row(0)
			db.close()

			lista = pesquisa.padronizar(lista)

			return pesquisa.padronizaRetorno(lista, 200, tamanho_pagina, sql=sql)
	except:
		pass
	return HttpResponseRedirect('/pagina_erro')

@gzip_page
@require_http_methods(['GET'])
def obter_campos_opcionaisTestes(request):
	try:
		codregistro, chave, staff, configs = funcoes.validaLoginSessao(request)
		if codregistro == None:
			return HttpResponseRedirect('/login')
		elif codregistro == 'EXPIRADO':
			return HttpResponseRedirect('/pagina_licenca_vencida')
		else:
			jsonResposta = campos
			resposta = HttpResponse(
				json.dumps(jsonResposta), content_type='application/json; charset=utf-8')
			resposta.status_code = 200
			resposta["Access-Control-Allow-Origin"] = "*"
			return resposta
	except:
		pass
	return HttpResponseRedirect('/pagina_erro')

campos2 = [
	['o.nome', u'Nome', 'string', 10000],
	['o.sigla', u'Sigla', 'string', 2000],
	['o.unidade', u'Unidade', 'int', 5000],
	['o.ativo', u'Status', 'status', 5000],
	['o.observacao', u'Observação', 'string', 10000],
]

@gzip_page
@require_http_methods(['GET'])
def filtrar_relatorio_opcionaisTestes(request):
	try:
		codregistro, chave, staff, configs = funcoes.validaLoginSessao(request)
		if codregistro == None:
			return HttpResponseRedirect('/login')
		elif codregistro == 'EXPIRADO':
			return HttpResponseRedirect('/pagina_licenca_vencida')
		else:
			imprimir = request.GET['imprimir']

			# Prepara Lista de Retorno
			listaMaster = []
			listaDetalhe = []
			listaDados = []

			codigo_status = 200  # OK

			# Instancia Conector do Banco.
			db = funcoes.connectMySql()

			sql = 'SELECT nome, sigla, unidade, ativo, observacao '
			
			sql += 'FROM tabela_opcionais_testes WHERE codregistro=\'%s\' ' % codregistro

			sql += 'order by nome asc'

			db.query(sql)
			listaDetalhe = db.use_result().fetch_row(0)

			for d in listaDetalhe:
				listaDados.append([[], [], [], [], 
				funcoes.decodeUtf8(d[0].decode('utf8')) if (d[0] != '' and d[0] != None) else '', 
				funcoes.decodeUtf8(d[1].decode('utf8')) if (d[1] != '' and d[1] != None) else '', 
				d[2], d[3], 
				funcoes.decodeUtf8(d[4].decode('utf8')) if (d[4] != '' and d[4] != None) else ''])

			db.close()
			if imprimir == 'S':
				if listaDados != []:
					formato = int(request.GET['formato'])
					for subdados in listaDados:
						nome = subdados[4]
						novo_nome = (nome[:40] + '..') if len(nome) > 42 else nome
						subdados[4] = novo_nome

					if formato != 1:
						# gerar pdf
						dados = relfin(codregistro, listaDados)
						if dados != None:
							# mimetype, encoding = mimetypes.guess_type(dados)
							nome_arquivo = 'relatorio_opcionaisdetestes_%s.pdf' % codregistro
							resposta = HttpResponse(mimetype='application/pdf')

							resposta['Content-Disposition'] = 'inline; filename=\'%s\'' % nome_arquivo
							resposta.write(dados)
							resposta.status_code = 200
					else:
						# gerar arquivo xls
						dados = gerador_planilha_opcionaisTestes.gerarPlanilha(codregistro, campos2, listaDados)

						if dados:
							return dados
				else:
					return render(request, 'nao_ha_dados.html', Context({'tempo': '5'}))
			else:
				resposta = HttpResponse(json.dumps(listaDados, separators=(',', ':')),
										content_type='application/json; charset=utf-8')

			resposta["Access-Control-Allow-Origin"] = "*"
			return resposta
	except:
	   pass
	return HttpResponseRedirect('/pagina_erro')