#coding: utf-8

from django.conf import settings
from django.http import HttpResponse
from service.utilitarios import funcoes
from service.dao.models import tabela_opcionais_testes
from service.dao.models import Grupo
from service.dao.models import Cliente
from service.dao.models import ClassificacaoFiscal

import re, os, xlwt

def gerarPlanilha(codregistro, campos, listaDados):
	try:
		# Definindo planilha
		wb = xlwt.Workbook()
		ws = wb.add_sheet(u'Relatório Opcionais de Testes')

		# Cria a fonte
		font = xlwt.Font()
		# Noma da fonte
		font.name = 'Tahoma'
		# Tamanho da fonte
		font.height = 320
		# Define o status de negrito da fonte
		font.bold = True
		# Define o status do sublinhado da fonte
		font.underline = True

		# Cria o estilo da fonte
		style = xlwt.XFStyle()

		# Aplica a fonte no estilo
		style.font = font

		# Define o alinhamento do texto
		alignment = xlwt.Alignment()
		alignment.horz = xlwt.Alignment.HORZ_CENTER
		style.alignment = alignment

		# Define as bordas das células
		borders = xlwt.Borders()
		borders.bottom = xlwt.Borders.MEDIUM
		borders.top = xlwt.Borders.MEDIUM
		borders.left = xlwt.Borders.MEDIUM
		borders.right = xlwt.Borders.MEDIUM
		style.borders = borders
		
		titulos = []

		for c in campos:
			if c[0] == 'id_classificacao_fiscal':
				titulos.append([u"NCM", c[3]])
			else:
				titulos.append([u"%s" % funcoes.decodeUtf8(c[1]), c[3]])
			
		
		titulo_tabela = u'Relatório da Tabela Opcionais de Testes'

		ws.write_merge(0, 0, 0, len(titulos)-1, titulo_tabela, style=style)
		ws.row(0).height = 600

		font = xlwt.Font()
		font.name = 'Tahoma'
		font.height = 200
		font.bold = True
		style = xlwt.XFStyle()
		style.font = font
		style.borders = borders
		
		# Escrevendo títulos na primeira linha do arquivo
		i = 0
		for t in titulos:
			ws.write(1, i, t[0], style=style)

			# Definindo largura das células das sequência
			ws.col(i).width = t[1]
			i += 1

		ws.row(1).height = 400

		font = xlwt.Font()
		font.name = 'Tahoma'
		font.height = 170
		font.bold = False

		style = xlwt.XFStyle()
		styleLeft = xlwt.XFStyle()
		styleRight = xlwt.XFStyle()

		style.font = font
		styleLeft.font = font
		styleRight.font = font

		borders = xlwt.Borders()
		borders.bottom = xlwt.Borders.THIN
		borders.top = xlwt.Borders.THIN
		borders.left = xlwt.Borders.THIN
		borders.right = xlwt.Borders.THIN
		style.borders = borders
		styleLeft.borders = borders
		styleRight.borders = borders

		alignment = xlwt.Alignment()
		alignment.horz = xlwt.Alignment.HORZ_LEFT
		styleLeft.alignment = alignment

		alignment = xlwt.Alignment()
		alignment.horz = xlwt.Alignment.HORZ_RIGHT
		styleRight.alignment = alignment

		linha = 2
		valor_total = 0
		estoque_total = 0
		visualizar_valor_total = False
		visualizar_estoque_total = False

		controle = 0
		for l in listaDados:
			l = l[4: len(l)]
			opcional = tabela_opcionais_testes.objects.filter(codregistro=codregistro)[controle]
			
			coluna = 0
			if opcional.nome != None and opcional.nome != '':		
				ws.write(linha, coluna, funcoes.removerAcentos(opcional.nome), style=styleLeft)			
			else:
				ws.write(linha, coluna, u'', style=styleLeft)
			
			coluna += 1
			if opcional.sigla != None and opcional.sigla != '':		
				ws.write(linha, coluna, funcoes.removerAcentos(opcional.sigla), style=styleLeft)			
			else:
				ws.write(linha, coluna, u'', style=styleLeft)
			
			coluna += 1
			if opcional.unidade != None:
				ws.write(linha, coluna, u'%d' % int(opcional.unidade), style=styleLeft)
			else:
				ws.write(linha, coluna, u'0', style=styleLeft)

			coluna += 1
			ws.write(linha, coluna, u'%s' % ('Ativo' if (opcional.ativo == 1) else 'Inativo'), style=styleLeft)

			coluna += 1
			if opcional.observacao != None and opcional.observacao != '':
				ws.write(linha, coluna, funcoes.removerAcentos(opcional.observacao), style=styleLeft)
			else:
				ws.write(linha, coluna, u'', style=styleLeft)
				
			linha += 1
			controle +=1
		
		print("uhu10")
		font = xlwt.Font()
		font.name = 'Tahoma'
		font.height = 200
		font.bold = True
		style = xlwt.XFStyle()
		style.font = font
		style.borders = borders
		coluna = 0
			
		# Salva a planilha na requisição HTTP de retorno
		response = HttpResponse(mimetype = "application/ms-excel")
		response['Content-Disposition'] = 'attachment; filename=relatorio_opcionaisdetestes.xls'
		wb.save(response)
		return response
	except:
		return None

