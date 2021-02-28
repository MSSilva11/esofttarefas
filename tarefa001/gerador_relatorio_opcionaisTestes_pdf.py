# coding: utf-8

from django.conf import settings
from service import fpdf
from service.utilitarios import funcoes
from datetime import datetime
import os, os.path

# Método que gera um relatório de opcionais de testes em pdf
def gerar_relatorio(codregistro, lista_opcionaisdetestes):
	try:
		data_relatorio = datetime.today() # Data da geração do relatório
		pdf = fpdf.FPDF()				  # Objeto da classe FPDF
		limite_tamanho_pagina = 260		  # Tamanho da página (altura)
		altura = 25						  # Altura do cabeçalho de dados da tabela
		pagina_atual = 1				  # Página atual do arquivo pdf
		valorTotalTabela = 0;			  # Total de valores em aberto ou liquidados das finanças selecionadas
		cont = 0
		pdf.alias_nb_pages()

		# Cria uma nova página do arquivo pdf
		novaPagina(pdf, data_relatorio)
		pagina_atual = pagina_atual + 1

		# Cria Subtitulos.
		pdf = criaSubtitulo(pdf, altura)
		altura = altura + 6

		i = 0
		while i < len(lista_opcionaisdetestes):
			pdf.set_font('Arial', '', 10)
			pdf.text(x=10,y=altura, txt=u'%s' % funcoes.removerAcentos(lista_opcionaisdetestes[i][4]))
			pdf.text(x=82,y=altura, txt=u'%s' % funcoes.removerAcentos(lista_opcionaisdetestes[i][5]))
			pdf.text(x=99,y=altura, txt=u'%s' % lista_opcionaisdetestes[i][6])
			if lista_opcionaisdetestes[i][7] == '1':
				pdf.text(x=121,y=altura, txt=u'Ativo')
			else:
				pdf.text(x=121,y=altura, txt=u'Inativo')
			pdf.text(x=143,y=altura, txt=u'%s' % funcoes.removerAcentos(lista_opcionaisdetestes[i][8]))

			i = i+1
			altura += 6
			if altura >= 275:
				pdf.set_font('times', '', 10)
				pdf.set_text_color(0, 0, 0)
				# Cria Nova Paigna.
				novaPagina(pdf, data_relatorio)
				pagina_atual = pagina_atual + 1
				# Cria Subtitulos.
				altura = 45
				pdf = criaSubtitulo(pdf, altura)
				altura = altura + 5
		
			
		# salva no arquivo no diretório de arquivos de extratos
		path = settings.MEDIA_PDF
		if not os.path.exists(path):
			os.makedirs(path)

		nome_arquivo = path + str(codregistro) + ".pdf"
		pdf.alias_nb_pages()
		pdf.output(r"" + nome_arquivo, "F")
		pdf.close()

		return file(nome_arquivo, 'rb').read()
	except:
		return None


#Cria Nova Pagina.
def novaPagina(pdf, data_relatorio):
	# cria a página (ou uma nova página, caso esta função seja chamada novamente)
	# comprimento total: 210
	pdf.add_page()
	#if pagina_atual == 1:
	titulo = u"Relatório da Tabela Opcionais de Testes"
	# Título página
	pdf.set_font('Arial', 'B', 18)
	# Define o texto, a codificação e o posicionamento (margem superior, margem superior)
	pdf.set_x(0)
	pdf.set_y(12)
	# Título página
	pdf.text(x=10, y=12, txt=titulo)
	
	criaRodape(pdf, data_relatorio)
	return pdf

# Cria Subtitulos.
def criaSubtitulo(pdf, altura):
	pdf.set_font('Arial', 'B', 12)
	pdf.set_line_width(0.3)
	pdf.text(x=10, y=altura, txt=u'Nome') # width=23
	pdf.line(10  , altura+1, 80 , altura+1)
	pdf.text(x=82, y=altura, txt=u'Sigla') # width=38
	pdf.line(82 , altura+1, 97 , altura+1)
	pdf.text(x=99, y=altura, txt=u'Unidade') # width= 28
	pdf.line(99 , altura+1, 119, altura+1)
	pdf.text(x=121, y=altura, txt=u'Status') # width= 27
	pdf.line(121, altura+1, 141, altura+1)
	pdf.text(x=143, y=altura, txt=u'Observação') # width= 48
	pdf.line(143, altura+1, 202, altura+1)

	return pdf

# Cria Rodapé
def criaRodape(pdf, data_relatorio):
	# Linha rodapé
	pdf.line(5, 288, 205, 288)
	# Texto rodapé
	pdf.set_font('Arial', '', 10)
	pdf.text(x=9, y=293, txt=u'Modo Teste')
	# Texto data geração de relatórios
	texto = u'Gerado em %02d/%02d/%d às %02d:%02d' % (data_relatorio.day, data_relatorio.month, 
		data_relatorio.year, data_relatorio.hour, data_relatorio.minute)
	pdf.text(x=79, y=293, txt=texto)
	# Texto número da página no rodapé
	texto = u'Pág. %d de {nb}' % (pdf.page_no())
	pdf.text(x=180, y=293, txt=texto)
	return pdf