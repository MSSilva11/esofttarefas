# coding: utf-8
'''
 *
 * AddMob Integradora de Soluções LTDA (c) - 2015
 *
 * Arquivo que define o mapeamento das tabelas do banco de dadoos
 *
 * PortalERP
 *
 * models.py
 *
 * Desenvolvido por:
 * - Diego Oliveira
 * - Flávio Lucio De Paula G.JR
 * - José Eduardo Ferreira
 * - Paulo Vitor Francisco
 *
'''
from django.db import models


'''
    Classe Empresa
        Define o mapeamento da tabela de empresa do sistema PortalERP
'''
class Empresa(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Nome da empresa
    nome_empresa = models.CharField(max_length=300)
    # Razao social da empresa
    razaosocial = models.CharField(max_length=300)
    # CPF/CNPJ da empresa
    cnpj = models.CharField(max_length=18)
    # Inscrição estadual da empresa
    inscricao_estadual = models.CharField(max_length=50)
    # Numero de telefone da empresa
    telefone = models.CharField(max_length=16)
    # Email da empresa
    email = models.CharField(max_length=56)
    # Email para envio de NF-e
    email_emissao_nfe = models.CharField(max_length=56)
    # Website da empresa
    site = models.CharField(max_length=56)
    # Endereço da empresa
    cep = models.CharField(max_length=9)
    # CEP do endereço da empresa
    endereco = models.CharField(max_length=90)
    # Número do endereço da empresa
    numeroendereco = models.CharField(max_length=10)
    # Complemento do endereço da empresa
    complemento = models.CharField(max_length=90, default=None)
    # Bairro do endereço da empresa
    bairro = models.CharField(max_length=90)
    # Cidade do endereço da empresa
    cidade = models.IntegerField()
    # Estado do endereço da empresa
    estado = models.IntegerField()
    # Nome da imagem de logomarca da empresa
    logoempresa = models.CharField(max_length=255)
    # Rede Social 1
    rede_social_1 = models.CharField(max_length=200)
    # Rede Social 2
    rede_social_2 = models.CharField(max_length=200)
    # Quantidade de dispositivos referentes a esta empresa
    quantidade_dispositivos = models.IntegerField()
    # Nome da imagem de fundo da tela de menu (caso ela exista)
    imagem_menu = models.CharField(max_length=40)
    # Texto descritivo sobre a empresa
    descricao = models.TextField()
    # Valor da latitude das coordenadas de localização da empresa
    latitude = models.CharField(max_length=30)
    # Valor da longitude das coordenadas de localização da empresa
    longitude = models.CharField(max_length=30)
    # Data de inalguração da empresa
    data_criacao = models.DateTimeField(auto_now_add=True)
    # Status de empresa com playground (padrão: "S" ou "N")
    playground = models.CharField(max_length=1)
    # Status de empresa com estacionamento (padrão: "S" ou "N")
    estacionamento = models.CharField(max_length=1)
    # Status de empresa com manobrista (padrão: "S" ou "N")
    manobrista = models.CharField(max_length=1)
    # status de empresa que possui cardápio cadastrado no sistema (padrao: "S" ou "N")
    temcardapio = models.CharField(max_length=1)
    # define a quantidade de acessos da empresa
    quantidade_acessos = models.IntegerField()
    # define o tipo de empresa (padrão: "R": restaurante e "E": empresa comum)
    tipo_empresa = models.CharField(max_length=1)
    # data da última atualização
    data_ultima_atualizacao = models.DateTimeField()
    # ativo
    ativo = models.IntegerField(max_length=1)
    # id_circuito que ele pertence
    id_circuito = models.IntegerField()
    # Endereço do perfil da empresa no Facebook
    facebook = models.CharField(max_length=255, default='')
    # Endereço do perfil da empresa no Instagram
    instagram = models.CharField(max_length=255, default='')
    # Endereço do perfil da empresa no Twitter
    twitter = models.CharField(max_length=255, default='')
    # Código da Sub-Empresa
    codempresa = models.IntegerField(primary_key=True, max_length=2)

    class Meta:
        db_table = u'nempresa'


'''
    Classe Usuario
        Define o mapeamento da tabela de usuário do sistema PortalERP
'''
class Usuario(models.Model):
    # Identificador do usuário
    id = models.IntegerField()
    # Código de registro da empresa deste usuário
    codregistro = models.IntegerField(max_length=25)
    # Status de usuário ativo
    is_active = models.IntegerField(max_length=1)
    # Data de criação da conta de usuário
    date_joined = models.DateTimeField()
    # Data de expiração da conta de usuário
    dt_expiracao = models.DateTimeField()
    # Nome de usuário para login
    username = models.CharField(max_length=100, primary_key=True)
    # Hash da senha do usuário
    password = models.TextField()
    # Número de telefone do usuário
    telefone = models.CharField(max_length=15)
    # Tipo do plano do usuário
    tipo_plano = models.IntegerField()
    # Tipo de usuário
    tipo_usuario = models.IntegerField()
    # Nome do usuário
    first_name = models.CharField(max_length=100)
    # Sobrenome do usuário
    last_name = models.CharField(max_length=100)
    # Email do usuário
    email = models.CharField(max_length=100)
    # Data do último login
    last_login = models.DateTimeField()
    # Define o grupo que este usuário pertence 
    groups = models.CharField(max_length=100)
    # Define as permissões deste usuário
    user_permissions = models.CharField(max_length=100)
    # Define o status de administrador para acesso ao site deste usuário
    is_staff = models.IntegerField(max_length=1)
    # Define o status de super usuário deste usuário
    is_superuser = models.IntegerField(max_length=1)
    # Nome da imagem do usuário
    imagem = models.CharField(max_length=255)
    # Identificador do cliente
    id_cliente = models.IntegerField()
    # Nome do perfil deste usuário
    perfil = models.CharField(max_length=100)
    # CNPJ da empresa (usuário do cliente)
    cnpj_empresa = models.CharField(max_length=14)
    # CPF/CNPJ do usuário do cliente
    cpf_cnpj = models.CharField(max_length=14)
    # Define o setor de trabalho do usuário
    id_setor = models.IntegerField(max_length=11, default=0)

    class Meta:
        db_table = u'auth_user'


'''
    Classe Configs
        Define o os campos da tabela de configuraçẽos de uma empresa
'''
class Configs(models.Model):
    # Identificador de configs
    id_configs = models.IntegerField()
    # Código de registro da empresa deste usuário
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    #
    mostra_clientes = models.CharField(max_length=255, default=None)
    #
    mostra_produtos = models.CharField(max_length=255, default=None)
    #
    tamanhos_clientes = models.CharField(max_length=255, default=None)
    #
    tamanhos_produtos = models.CharField(max_length=255, default=None)
    #
    titulos_clientes = models.CharField(max_length=255, default=None)
    #
    titulos_produtos = models.CharField(max_length=255, default=None)
    #
    contfinancadocumentopagar = models.IntegerField(default=0)
    #
    contfinancadocumentoreceber = models.IntegerField(default=0)
    #
    mascarapreco = models.CharField(max_length=30, default=None)
    #
    mascaraquantidade = models.CharField(max_length=30, default=None)
    #
    mostra_financa = models.CharField(max_length=255, default=None)
    #
    tamanhos_financa = models.CharField(max_length=255, default=None)
    #
    titulos_financa = models.CharField(max_length=255, default=None)
    #
    cont_numdocumentomovliq = models.IntegerField(default=0)
    # Status de empresa que trabalha com emissão de nota fiscal eletrônica (NF-e)
    trabalha_nfe = models.IntegerField(max_length=1, default=0)
    # Tipo de Ambiente da NF-e. "Produção = 1", "Homologação = 2"
    tipo_ambiente = models.IntegerField(max_length=1, default=2)
    # CRT da empresa
    crt = models.IntegerField(default=1)
    # Inscrição Municipal do Prestador de serviço
    inscricao_municipal = models.CharField(max_length=20, default=None)
    # CNAE fiscal
    cnae = models.CharField(max_length=20, default=None)
    # Nome do arquivo com o certificado do cliente
    nome_certificado = models.CharField(max_length=30, default=None)
    # senha do certificado
    senha_certificado = models.TextField(default=None)
    # Define a série padrão da empresa para emissão de nf-e
    serie_padrao = models.CharField(max_length=20, default=None)
    # Define a espécie padrão da empresa para emissão de nf-e
    especie_padrao = models.CharField(max_length=3, default=None)
    # Mensagem de acréscimo no email de envio de nf-e para cliente
    mensagem_email_nfe = models.TextField(default=None)
    # Identificador do módulo utilizadoi pela empresa
    id_modulo = models.IntegerField(default=0)
    # Email do contador da empresa
    email_contador = models.CharField(max_length=100, default=None)
    # Data de expiração da conta
    data_expiracao_conta = models.DateField(default=None)
    # Status de empresa que emite nfc-e
    emite_nfce = models.IntegerField(default=0)
    # Código CSC (homologação)
    codigo_csc_homologacao = models.CharField(max_length=32, default=None)
    # Código CSC (Produção)
    codigo_csc_producao = models.CharField(max_length=32, default=None)
    # Código status abertura
    codstatusabertura = models.CharField(max_length=2)
    # Termos de uso da empresa
    termos_uso = models.TextField(default=None)
    # Identificador do usuário de acesso a API
    id_usuario_api = models.IntegerField(default=None)
    # Url api esoft
    url_api_esoft = models.TextField(default=None)
    # Número de dias úteis ate o novo contato
    #num_dias_uteis_novo_contato = models.IntegerField(default=5)
    # Campo que recebe a chave da criptografia
    #chave_criptografia = None
    # Status de empresa que trabalha com a API SkyHub
    trabalha_api_skyhub = models.IntegerField(default=0)
    # Login API Skyhub
    login_api_skyhub = models.CharField(max_length=255, default=None)
    # Senha API Skyhub
    senha_api_skyhub = models.TextField(default=None)
    # Token API Skyhub
    token_api_skyhub = models.CharField(max_length=255, default=None)
    # Status de empresa que trabalha com a API MadeiraMadeira
    trabalha_api_madeira = models.IntegerField(default=0)
    # Login API MadeiraMadeira
    login_api_madeira = models.CharField(max_length=255, default=None)
    # Senha API MadeiraMadeira
    senha_api_madeira = models.TextField(default=None)
    # Token API MadeiraMadeira
    token_api_madeira = models.CharField(max_length=255, default=None)
    # Status de empresa que trabalha com a API Leroy Merlin
    trabalha_api_leroy = models.IntegerField(default=0)
    # Login API Leroy Merlin
    login_api_leroy = models.CharField(max_length=255, default=None)
    # Senha API Leroy Merlin
    senha_api_leroy = models.TextField(default=None)
    # Token API Leroy Merlin
    token_api_leroy = models.CharField(max_length=255, default=None)
    # Número de dias para o próximo agendamento (MegaZap)
    dias_agendamento_megazap = models.IntegerField(default=0)
    # Mensagem padrão de boas vindas (MegaZap)
    msg_boas_vindas_megazap = models.TextField(default=None)
    # Mensagem padrão de encaminhamento (MegaZap)
    msg_encaminhamento_megazap = models.TextField(default=None)
    # Mensagem padrão de encerramento (MegaZap)
    msg_encerramento_megazap = models.TextField(default=None)
    #Parâmetro de verificação se trabalha com log de usuário
    trabalha_log_mov_usu = models.IntegerField(default=0)
    #Nome do usuário integrador de transportadoras
    usu_integrador_transp = models.TextField(default=None)
    #Senha do usuário integrador de transportadoras
    senha_integrador_transp = models.TextField(default=None)
    #Token do usuário integrador de transportadoras
    token_integrador_transp = models.TextField(default=None)
    #Nome do usuário integrador de cartão de crédito loja virtual
    usu_integrador_cartao_loja_virtual = models.TextField(default=None)
    #Senha do usuário integrador de cartão de crédito loja virtual
    senha_integrador_cartao_loja_virtual = models.TextField(default=None)
    #Token do usuário integrador de cartão de crédito loja virtual
    token_integrador_cartao_loja_virtual = models.TextField(default=None)
    #Nome do usuário integrador de cartão de crédito aplicativo
    usu_integrador_cartao_app = models.TextField(default=None)
    #Senha do usuário integrador de cartão de crédito aplicativo
    senha_integrador_cartao_app = models.TextField(default=None)
    #Token do usuário integrador de cartão de crédito aplicativo
    token_integrador_cartao_app = models.TextField(default=None)
    # url API Magento
    url_api_magento = models.TextField(default=None)
    # usuario API Magento
    usuario_api_magento = models.TextField(default=None)
    # senha API Magento
    senha_api_magento = models.TextField(default=None)
    # Status de empresa que trabalha com a API Magento
    trabalha_api_magento = models.IntegerField(default=0)
    # Código da Sub-Empresa
    codempresa = models.IntegerField(primary_key=True, max_length=2)

    class Meta:
        db_table = u'nconfigs'


'''
    Classe Grupo
        Define os atributos de um grupo ou subgrupo de produtos.
'''
class Grupo(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do grupo
    id_grupo = models.IntegerField(primary_key=True)
    # Identificador do grupo pai (caso exista) para possibilitar o
    # encadeamento de grupos por niveis
    id_pai = models.IntegerField()
    # Nome do grupo
    nome_grupo = models.CharField(max_length=60)
    # Status de grupo ativo ou nao (padrao: "S" ou "N")
    ativo = models.IntegerField(max_length=1)
    # Poosicao de exibicao deste grupo na lista de grupos
    posicao = models.IntegerField()
    # Status de existencioa de subgrupos relacionados a este grupo (padrao:
    # "S" ou "N")
    possui_subgrupo = models.CharField(max_length=1)
    # Nome da imagem ilustrativa deste grupo (padrao:
    # <id_grupo>.<extensao_imagem>. Ex: 1.jpg)
    imagem = models.CharField(max_length=255)
    # Caminho deste grupo ate o topo da hierarquia de grupos, caso esta
    # hierarquia exista
    path = models.TextField()
    # Código do grupo original, vindo do esoft
    cod_grupo_original = models.CharField(max_length=3, default=None)
    # Código do subgrupo original, vindo do esoft
    cod_subgrupo_original = models.CharField(max_length=3, default=None)

    class Meta:
        db_table = u'ngrupo'


'''
    Classe Produtos
        Define os atributos de um produto.
'''
class Produtos(models.Model):
    # Identificador do grupo na qual este produto pertence (ultimo grupo da
    # hierarquia de grupos, caso exista)
    id_grupo = models.IntegerField(default=0)
    # Idebtificador do produto
    id_produto = models.IntegerField(primary_key=True)
    # Nome do produto, em portugues
    nome_produto_1 = models.CharField(max_length=255)
    # Nome do produto, em espanhol
    nome_produto_2 = models.CharField(max_length=255)
    # Nome do produto, em ingles
    nome_produto_3 = models.CharField(max_length=255)
    # Codigo de barras do produto
    codbarra = models.CharField(max_length=20, primary_key=True)
    # Descricao do produto, em portugues
    descricao_produto_1 = models.TextField(null=True)
    # Descricao do produto, em espanhol
    descricao_produto_2 = models.TextField(null=True)
    # Descricao do produto, em ingles
    descricao_produto_3 = models.TextField(null=True)
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Status de produto ativo (padrao: "S" ou "N")
    ativo = models.IntegerField(max_length=1)
    # Preco de Venda do Produto
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    # Preco de Custo do Produto
    precocusto = models.DecimalField(max_digits=12, decimal_places=2)
    # Preço normal de venda do produto
    #preco_normal = models.DecimalField(max_digits=12, decimal_places=2)
    # Preço promocional de venda do produto
    #preco_promocional = models.DecimalField(max_digits=12, decimal_places=2)
    # Data de início do preço promocional
    #inicio_preco_promocional = models.DateField()
    # Data final do preço promocional
    #fim_preco_promocional = models.DateField()
    # Estoque do produto
    estoque = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Unidade de Medida.(Ex: 'Kg', 'Ml', 'L', 'BD', 'PC')
    unidademedida = models.CharField(max_length=6)
    # Peso bruto do produto
    peso_bruto = models.DecimalField(max_digits=12, decimal_places=3)
    # Peso líquido do produto
    peso_liquido = models.DecimalField(max_digits=12, decimal_places=3)
    # Posicao deste produto na lista de exibicao de produtos
    posicao = models.IntegerField()
    # Nome da imagem ilustrativa deste produto (padrao:
    # <id_grupo>_<id_produto>.<extensao_imagem>. Ex: 1_1.jpg)
    imagem = models.CharField(max_length=255)
    # Identificador da impressora na qual este produto tera seus dados
    # impressos
    impProd = models.IntegerField(max_length=1, default=0)
    # Caminho deste produto ate o topo da hierarquia de grupos, caso esta
    # hierarquia exista
    path = models.TextField()
    # Identificador da classificação fiscal
    id_classificacao_fiscal = models.CharField(max_length=8)
    # Identificador do fornecedor deste produto
    id_fornecedor = models.IntegerField(default=None)
    # Margem de lucro do produto
    margem_lucro = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Estoque mínimo do produto
    estoque_minimo = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Estoque máximo do produto
    estoque_maximo = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Sugestão
    sugestao = models.CharField(max_length=1)
    # Promocao
    promocao = models.CharField(max_length=1)
    # Status de desconto de icms desonerado
    descontar_icms_deson = models.IntegerField(default=0)
    # Tipo de Produto ('V' = Venda, 'R' = Revenda, 'S' = Serviço).
    tipo_produto = models.CharField(max_length=1)
    # status de produto que será enviado para a loja virtual
    envia_loja_virtual = models.IntegerField(default=0)
    # status de produto que será enviado para o App de vendas
    envia_app_vendas = models.IntegerField(default=0)
    # Largura do produto
    largura = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    # Comprimento do produto
    comprimento = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    # Altura do produto
    altura = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    # Número de dias para a produção, quando o estoque for zero
    prazo_producao = models.IntegerField(default=0)
    # Código do fabricante do produto
    cod_fabricante = models.CharField(max_length=20, default=None)
    # Código do produto original, vindo do esoft
    cod_original = models.CharField(max_length=15, default=None)
    # última data de atualização
    ultima_data_atualizacao = models.DateTimeField()
    # Nome da imagem ilustrativa deste produto (padrao:
    # <id_grupo>_<id_produto>.<extensao_imagem>. Ex: 1_1.jpg)
    imagem2 = models.CharField(max_length=255)
    # Nome da imagem ilustrativa deste produto (padrao:
    # <id_grupo>_<id_produto>.<extensao_imagem>. Ex: 1_1.jpg)
    imagem3 = models.CharField(max_length=255)
    # envia produto para api magento
    envia_magento = models.IntegerField(max_length=11, default=0)
    # envia produto para api magento
    id_categoria_magento = models.IntegerField(max_length=11, default=None)
    # envia produto para api magento
    id_grupo_magento = models.IntegerField(max_length=11, default=None)


    class Meta:
        db_table = u'nproduto'


'''
    Classe ProdutoFornecedor
        Define os atributos de um relacionamento de fornecedores com um produto.
'''
class ProdutoFornecedor(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código de barras do produto no cadastro do fornecedor (NF de entrada)
    codbarra = models.CharField(primary_key=True, max_length=12)
    # Identificador do produto no PortalERP
    id_produto = models.IntegerField()
    # Identificador do fornecedor
    id_fornecedor = models.CharField(primary_key=True, max_length=60)

    class Meta:
        db_table = u'nproduto_fornecedor'


'''
    Classe Parametro
        Define os parâmetros do sistema.
'''
class Parametro(models.Model):
    # Identificador do parâmetro
    id_parametro = models.IntegerField()
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Nome do parâmetro
    nome_parametro = models.CharField(primary_key=True, max_length=100)
    # Preço do parâmetro
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    # Quantidade do Parâmetro
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    # Status de parâmetro ativo
    ativo = models.IntegerField(max_length=1)

    class Meta:
        db_table = u'nparametro'


'''
    Classe Opcional
        Define os dados referentes ao opcional de um produto.
'''
class Opcional(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do opcional do produto
    id_opcional = models.IntegerField(primary_key=True)
    # Nome do opcional
    nome_opcional = models.CharField(max_length=60)
    # Preco do opcional
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    # Status de opcional ativo (padrao: "S" ou "N")
    ativo = models.IntegerField(max_length=1)

    class Meta:
        db_table = u'nopcional'


'''
    Classe CadAtendente
        Define os dados referentes a um atendente do sistema.
'''
class CadAtendente(models.Model):
    # Identificador do atendente
    id_atendente = models.IntegerField()
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Nome do atendente
    nome_atendente = models.CharField(primary_key=True, max_length=100)
    # Tipo de OS
    id_os = models.IntegerField()
    # Status de atendente ativo
    ativo = models.IntegerField(max_length=1)

    class Meta:
        db_table = u'ncadatendente'


'''
    Classe AtendimentoCliente
        Define os dados referentes a uma ocorrência do sistema lançada pelo cliente.
'''
class AtendimentoCliente(models.Model):
    # Identificador do atendimento ao cliente
    id_atendimentocliente = models.IntegerField(primary_key=True)
    # Descrição do atendimento ao cliente
    descricao = models.CharField(max_length=255)
    # Data da solicitação do atendimento ao cliente
    data_solicitacao = models.DateField()
    # Módulo do atendimento ao cliente
    modulo = models.CharField(max_length=50)
    # Motivo do atendimento ao cliente
    motivo = models.CharField(max_length=150)
    # Tipo de OS do atendimento ao cliente
    tipo_os = models.CharField(max_length=1)
    # Identificador do Cliente do atendimento ao cliente
    id_cliente = models.IntegerField()
    # Identificador do atendente do atendimento ao cliente
    id_atendente = models.IntegerField()
    # Identificador do contato do atendimento ao cliente
    id_contato = models.IntegerField()
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código de status do atendimento ao cliente
    codstatus = models.IntegerField()
    # Observação do atendimento da ocorrência (modo administrativo)
    observacao = models.TextField(default=None)
    # Usuário que realizou o fechamento do atendimento da ocorrẽncia
    usuario = models.CharField(max_length=100, default=None)
    # Data e hora da resolução da ocorrência
    data_resolucao_ocorrencia = models.DateTimeField(default=None)

    class Meta:
        db_table = u'natendimentocliente'


'''
    Classe CadContato
        Define os dados referentes a um contato de um cliente.
'''
class CadContato(models.Model):
    # Identificador do contato
    id_contato = models.IntegerField()
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Nome do contato
    nome_contato = models.CharField(primary_key=True, max_length=100)
    # Identificador do cliente
    id_cliente = models.IntegerField()
    # Status de contato ativo
    ativo = models.IntegerField(max_length=1)

    class Meta:
        db_table = u'ncadcontato'


'''
    Classe Transacao
        Define os dados referentes a uma transação.
'''
class Transacao(models.Model):
    # Identificador da transação
    id_transacao = models.IntegerField()
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Nome da transação
    nome_transacao = models.CharField(primary_key=True, max_length=50)
    # Tipo de movimentação ('E' - entrada e 'S' = saída)
    movimentacao = models.CharField(max_length=1)
    # Status de transação ativa
    ativo = models.IntegerField(max_length=1)
    # Transação Padrão para Recebimento.
    trans_padrao_rec = models.IntegerField(max_length=1)
    # Transação Padrão para Pagamento.
    trans_padrao_pag = models.IntegerField(max_length=1)

    class Meta:
        db_table = u'ntransacao'


'''
    Classe ContaBancaria
        Define os dados referentes a uma conta bancária.
'''
class ContaBancaria(models.Model):
    # Identificador da conta bancária
    id_conta = models.IntegerField()
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código da agência
    agencia = models.CharField(primary_key=True, max_length=6)
    # Código do banco
    banco = models.CharField(primary_key=True, max_length=3)
    # Número da conta
    conta = models.CharField(primary_key=True, max_length=15)
    # Conta Padrão para Recebimento?
    cont_padrao_rec = models.IntegerField(max_length=1)
    # Conta Padrão para Pagamento?
    cont_padrao_pag = models.IntegerField(max_length=1)
    # Status de conta interna
    interno = models.IntegerField(max_length=1)
    # Status de conta ativa
    ativo = models.IntegerField(max_length=1)
    # Banco gera nosso numero 
    gera_nosso_numero = models.IntegerField(max_length=1, default=0)
    # Campo inicial para geração do nosso número
    campo_inicial_nosso_numero = models.CharField(max_length=20)
    # Campo final para geração do nosso número
    campo_final_nosso_numero = models.CharField(max_length=20)

    class Meta:
        db_table = u'ncontabancaria'


'''
    Classe Financa
        Define os dados referentes a uma finança.
'''
class Financa(models.Model):
    # Identificador da finança
    id_financa = models.IntegerField(primary_key=True)
    # Codregistro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Status do sistema da finança
    tipo_financa = models.CharField(max_length=1)
    # Status de finança original
    original = models.CharField(max_length=1)
    # Documento da finança
    documento = models.CharField(max_length=15)
    # Estado do documento da finança
    estadodoc = models.CharField(max_length=2)
    # Valor da finança
    valor = models.DecimalField(max_digits=18, decimal_places=4)
    # Valor em aberto da finança
    valor_aberto = models.DecimalField(max_digits=18, decimal_places=4)
    # Valor recebido da finança
    valor_recebido = models.DecimalField(max_digits=18, decimal_places=4)
    # Define o valor de desconto da finança
    desconto = models.DecimalField(max_digits=18, decimal_places=4)
    # Valor de juros da finança
    juros = models.DecimalField(max_digits=18, decimal_places=4)
    # Valor de acréscimo da finança
    acrescimos = models.DecimalField(max_digits=18, decimal_places=4)
    # Valor da multa da finança
    multa = models.DecimalField(max_digits=18, decimal_places=4)
    # Identificador do cliente
    id_cliente = models.IntegerField()
    # Identificador do tipo
    id_tipo = models.IntegerField()
    # Status de finança ativa
    ativo = models.IntegerField(max_length=1)
    # Número do sistema da finança
    numero_sis = models.IntegerField()
    # Número de Liquidação do Sistema
    numero_sisliq = models.IntegerField()
    # Define o borderô (Borderô é o documento onde são relacionados os cheques pré-datados e/ou duplicatas 
    # que foram negociados com a empresa) da finança
    bordero = models.CharField(max_length=10)
    # Status de documento cancelado da finança
    doc_cancelado = models.IntegerField(max_length=1)
    # Data da emissão da finança
    data_emissao = models.DateField()
    # Data de vencimento da finança
    data_vencimento = models.DateField()
    # Status de protesto da finança
    em_protesto = models.IntegerField(max_length=1)
    # Status de enviar a contabilidade da finança
    enviar_contab = models.IntegerField(max_length=1)
    # Status judicial da finança
    judicial = models.IntegerField(max_length=1)
    # Status de lançamento da finança
    lancamento = models.CharField(max_length=1)
    # Número da apólice da finança
    numero_ap = models.CharField(max_length=15)
    # Número da boleta da finança
    numero_boleta = models.CharField(max_length=20)
    # Número de duplicata da finança
    numero_duplicata = models.CharField(max_length=20)
    # Observação da finança
    observacao = models.TextField()    
    # Valor de desconto do pagamento da finança
    descontopagamento = models.DecimalField(max_digits=18, decimal_places=4)
    # Data de recebimento da finança
    data_recebimento = models.DateField()
    # Valor de juros do pagamento da finança
    jurospagamento = models.DecimalField(max_digits=18, decimal_places=4)
    # Data de criação da finança
    data_criacao = models.DateField()
    # Data de liquidação da finança
    data_liquidacao = models.DateField()
    # Identificador da conta
    id_conta = models.IntegerField(default=None)
    # Identificador da carteira boleta
    id_carteira_boleta = models.IntegerField(default=None)
    # Tip ode boleto
    tipo_boleto = models.CharField(max_length=1, default=None)
    # Status de boleto gerado (0: não gerado, 1: boleto gerado)
    boleto_gerado = models.IntegerField(default=0)
    # Status de remessa gerada (0: não gerada, 1: remessa gerada)
    remessa_gerada = models.IntegerField(default=0)
    # Define o número da remessa (arquivo de remessa)
    numero_remessa = models.CharField(max_length=30, default=None)
    # Define o número da remessa (arquivo de remessa)
    nome_arquivo_remessa = models.CharField(max_length=50, default=None)
    # Código da Sub-Empresa
    codempresa = models.IntegerField(primary_key=True, max_length=2)

    class Meta:
        db_table = u'nfinanca'


'''
    Classe RecuperarSenha
        Define os dados referentes a chave de recuperação de senha.
'''
class RecuperarSenha(models.Model):
    # Identificador da chave de recuperação de senha
    id_senha_recuperacao = models.IntegerField(primary_key=True)
    # Chave de recuperação de senha
    senha_recuperacao = models.CharField(max_length=6)
    # Email do cliente
    email = models.CharField(max_length=90)
    
    class Meta:
        db_table = u'nrecuperar_senha'


'''
    Classe Cliente
        Define os atributos de um cliente.
'''
class Cliente(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do cliente
    id_cliente = models.IntegerField(primary_key=True)
    # Nome do cliente
    nome_cliente = models.CharField(max_length=100)
    # CPF/CNPJ do cliente
    cpf_cnpj = models.CharField(primary_key=True, max_length=14, default=0)
    # Telefone do cliente
    telefone = models.CharField(max_length=14)
    # Fax do cliente
    fax = models.CharField(max_length=14)
    # Celular do cliente
    celular = models.CharField(max_length=14)
    # E-mail do cliente
    email = models.CharField(max_length=50)
    # E-mail para recebimento de NF-e do cliente
    email_nfe = models.CharField(max_length=50)
    # Observacao do cliente
    observacao = models.TextField()
    # Site do cliente
    site = models.CharField(max_length=50)
    # senha de acesso do cliente
    senha = models.TextField()
    # gênero do cliente
    sexo = models.CharField(max_length=1)
    # data de nascimento do cliente
    data_nascimento = models.DateField(default=None)
    # estado civil do cliente
    estado_civil = models.CharField(max_length=20)
    
    # cep do endereco principal do cliente
    cep_endereco_principal = models.CharField(max_length=9)
    # endereço principal do cliente
    endereco_principal = models.CharField(max_length=90)
    # número do endereço principal do cliente
    numero_endereco_principal = models.IntegerField()
    # complemento do endereço principal do cliente
    complemento_endereco_principal = models.CharField(max_length=90, default=None)
    # bairro do endereço principal do cliente
    bairro_endereco_principal = models.CharField(max_length=90)
    # código da cidade do endereço principal do cliente
    cidade_endereco_principal = models.IntegerField()
    # código do uf do endereço principal do cliente
    estado_endereco_principal = models.IntegerField()

    # cep do endereco entrega do cliente
    cep_endereco_entrega = models.CharField(max_length=9, default=None)
    # endereço entrega do cliente
    endereco_entrega = models.CharField(max_length=90, default=None)
    # número do endereço entrega do cliente
    numero_endereco_entrega = models.IntegerField(default=None)
    # complemento do endereço entrega do cliente
    complemento_endereco_entrega = models.CharField(max_length=90, default=None)
    # bairro do endereço entrega do cliente
    bairro_endereco_entrega = models.CharField(max_length=90, default=None)
    # código da cidade do endereço entrega do cliente
    cidade_endereco_entrega = models.IntegerField(default=None)
    # código do uf do endereço entrega do cliente
    estado_endereco_entrega = models.IntegerField(default=None)

    # cep do endereco cobranca do cliente
    cep_endereco_cobranca = models.CharField(max_length=9, default=None)
    # endereço cobranca do cliente
    endereco_cobranca = models.CharField(max_length=90, default=None)
    # número do endereço cobranca do cliente
    numero_endereco_cobranca = models.IntegerField(default=None)
    # complemento do endereço cobranca do cliente
    complemento_endereco_cobranca = models.CharField(max_length=90, default=None)
    # bairro do endereço cobranca do cliente
    bairro_endereco_cobranca = models.CharField(max_length=90, default=None)
    # código da cidade do endereço cobranca do cliente
    cidade_endereco_cobranca = models.IntegerField(default=None)
    # código do uf do endereço cobranca do cliente
    estado_endereco_cobranca = models.IntegerField(default=None)
    
    # ponto de referẽncia do endereço do cliente
    ponto_referencia = models.CharField(max_length=60)
    # imagem do cliente
    imagem = models.CharField(max_length=255)
    # número da Incrição Estadual do cliente
    inscricao_estadual = models.CharField(max_length=20)
    # Nome Fantasia da Empresa do cliente
    nome_fantasia = models.CharField(max_length=100)
    # Razão Social da Empresa do cliente
    razao_social = models.CharField(max_length=100)
    # Cliente Está Ativo?
    ativo = models.IntegerField(max_length=1)
    # Status de considerar cliente
    considerar_cliente = models.CharField(max_length=1, default="S")
    # Cliente Pode Ser Usado Como Transportadora?
    considerar_transportadora = models.CharField(max_length=1, default="N")
    # Cliente Pode Ser Usado Como Fornecedor?
    considerar_fornecedor = models.CharField(max_length=1, default="N")
    # Cliente Pode Ser Usado Como Vendedor?
    considerar_vendedor = models.CharField(max_length=1, default="N")
    # Comissao do Vendedor
    comissao_vendedor = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Status de consumidor final
    consumidor_final = models.CharField(max_length=1, default='N')
    # Status de cliente contributinte de ICMS
    contribuinte_icms = models.IntegerField(max_length=1, default=0)
    # id do cliente cadaastrado como Matriz
    id_matriz = models.IntegerField(default=None, null=True)
    # E-mail para recebimento de boletos
    email_boleto = models.CharField(max_length=50)
    # Endereço do perfil do Instagran
    instagram = models.TextField(default=None)
    # Endereço do perfil do Facebook
    facebook = models.TextField(default=None)
    # Total de pontos do cliente
    total_pontos = models.DecimalField(max_digits=15, decimal_places=2, default=None)
    # Categoria do cliente
    categoria = models.IntegerField(default=None)
    # Nome principal do vendedor 
    nome_principal_vendedor = models.CharField(max_length=255, default=None)
    # Nome principal do atendente
    nome_principal_atendente = models.CharField(max_length=255, default=None)
    # Status de cliente que aceita envio de mensagens de marketing
    aceita_mkt = models.IntegerField(default=0)
    # Nome do responsável
    nome_responsavel = models.CharField(max_length=100, default=None)
    # CPF do responsável
    cpf_responsavel = models.CharField(max_length=14, default=None)
    # Código do cliente original, vindo do esoft
    cod_clie_original = models.CharField(max_length=15, default=None)
    # Código do fornecedor original, vindo do esoft
    cod_forn_original = models.CharField(max_length=15, default=None)
    # Código da transportadora original, vindo do esoft
    cod_tran_original = models.CharField(max_length=15, default=None)
    # Código do vendedor original, vindo do esoft
    cod_vend_original = models.CharField(max_length=15, default=None)
    # Cliente Pode Ser Usado Como Cartão de crédito?
    considerar_cartao_credito = models.CharField(max_length=1, default="N")
    # Taxa Administradora (%)
    taxa_administradora = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    # cartão de crédito
    checkbox_cartao_credito = models.IntegerField(max_length=11, default=0)
    # cartão de débito
    checkbox_cartao_debito = models.IntegerField(max_length=11, default=0)

    class Meta:
        db_table = u'ncliente'


'''
    Classe Paises
        Define os dados referentes aos Países.
'''
class Paises(models.Model):
    # ID do Pais.
    id_pais = models.IntegerField(primary_key=True)
    # Sigla do Pais.
    sigla = models.CharField(max_length=2)
    # Nome do País.
    nome = models.CharField(max_length=64)
    # Status de país ativo
    ativo = models.IntegerField(max_length=1, default=1)

    class Meta:
        db_table = u'npais'


'''
    Classe Regioes
        Define os dados referentes as Regiões.
'''
class Regioes(models.Model):
    # ID da Região.
    id_regiao = models.IntegerField(primary_key=True)
    # Nome da Região.
    nome = models.CharField(max_length=80)
    # Status de região ativo
    ativo = models.IntegerField(max_length=1, default=1)

    class Meta:
        db_table = u'nregiao'        


'''
    Classe Estados
        Define os dados referentes aos Estados.
'''
class Estados(models.Model):
    # ID do Pais.
    id_pais = models.IntegerField(primary_key=True)
    # ID da Região.
    id_regiao = models.IntegerField(primary_key=True)
    # ID do Estado.
    id_estado = models.IntegerField(primary_key=True)
    # Nome do Estado.
    nome = models.CharField(max_length=35)
    # Sigla do Estado.
    sigla = models.CharField(max_length=2)
    # Código do Estado - IBGE
    cod_estado = models.IntegerField()
    # Alíquota FCP (Fundo Contra Probreza)
    aliquota_fcp = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    # Alíquota de ICMS de entrada (Emissão de NF-e envolvendo emissor e cliente de estados diferentes)
    aliquota_entrada = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    # Alíquota de ICMS de saída (Emissão de NF-e envolvendo emissor e cliente de estados diferentes)
    aliquota_saida = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    # Alíquota de ICMS interna do estado (Emissão de NF-e envolvendo emissor e cliente de estados diferentes)
    aliquota_interna_icms = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    # Status de estado ativo
    ativo = models.IntegerField(max_length=1, default=1)

    class Meta:
        db_table = u'nestado'        


'''
    Classe DifalEstado
        Define os dados de relacionamento de um estado e as alíquotas de saída para outros estados
'''
class DifalEstado(models.Model):
    # Identificador do estado de origem
    id_estado_origem = models.IntegerField(primary_key=True)
    # Identificador do estado de destino
    id_estado_destino = models.IntegerField(primary_key=True)
    # Alíquota de saída
    aliquota_saida = models.DecimalField(max_digits=14, decimal_places=4)
    # Alíquota de st
    aliquota_st = models.DecimalField(max_digits=14, decimal_places=4)

    class Meta:
        db_table = u'ndifal_estado'


'''
    Classe Areas
        Define os dados referentes as Cidades.
'''
class Areas(models.Model):
    # ID da Área.
    id_area = models.IntegerField(primary_key=True)
    # ID do Estado.
    id_estado = models.IntegerField(primary_key=True)
    # nome da Área.
    area = models.CharField(max_length=80)
    # Código de Área para Ligações (DDD).
    cod_area = models.CharField(max_length=6)
    # Status de área ativo
    ativo = models.IntegerField(max_length=1, default=1)
    

    class Meta:
        db_table = u'narea'


'''
    Classe Cidades
        Define os dados referentes as Cidades.
'''
class Cidades(models.Model):
    # ID do Pais.
    id_pais = models.IntegerField(primary_key=True)
    # ID da Região.
    id_regiao = models.IntegerField(primary_key=True)
    # ID do Estado.
    id_estado = models.IntegerField(primary_key=True)
    # ID da Cidade.
    id_cidade = models.IntegerField(primary_key=True)
    # Nome da Cidade.
    nome = models.CharField(max_length=50)
    # Código da Cidade - IBGE
    cod_cidade = models.IntegerField()
    # Código de Área para Ligações (DDD)
    cod_area = models.CharField(max_length=6)
    # Status de cidade ativo
    ativo = models.IntegerField(max_length=1, default=1)
    

    class Meta:
        db_table = u'ncidade'


'''
    Classe MovimentoLiquidacao
        Define os dados referentes ao moviemnto de liquidação.
'''
class MovimentoLiquidacao(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador de moviemnto de liquidação
    id_mov_liq = models.IntegerField(primary_key=True)
    # Identificador da conta do moviemnto de liquidação
    id_conta = models.IntegerField() 
    # Identificador da transação do moviemnto de liquidação
    id_transacao = models.IntegerField()
    # Documento do moviemnto de liquidação
    documento = models.CharField(max_length=15)
    # Status do moviemnto de liquidação
    movimentacao = models.CharField(max_length=1)
    # Valor da moviemntação
    valor = models.DecimalField(max_digits=18, decimal_places=4)
    # Data da movimentação
    data_movimento = models.DateField()
    # Descrição
    descricao = models.TextField()
    # NúmeroSis de Liquidação Gerado Em "funcoes.NumeroSisLiq".
    numero_sisliq = models.IntegerField()
    # Tipo de moviemnto (E = Estorno, L = Liquidação)
    estorno_liquidacao = models.CharField(max_length=1)
    # Origem do moviemnto de liquidação(P = Pagar, R = Receber, M = Manual)
    origem = models.CharField(max_length=1)
    # codempresa
    codempresa = models.IntegerField(max_length=2)

    class Meta:
        db_table = u'nmovimento_liquidacao'


'''
    Classe HistoricoMovimento
        Define os dados referentes ao histórico de moviemntação.
'''
class HistoricoMovimento(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador da finança do histórico de movimentação
    id_financa = models.IntegerField(primary_key=True)
    # Tipo de Finaça (R = Receber, P = Pagar)
    tipo_financa = models.CharField(max_length=1)
    # Identificador do histórico de movimentação
    id_hist_mov = models.IntegerField(primary_key=True)  
    # Status do histórico de movimentação
    movimentacao = models.CharField(max_length=1)
    # Data do histórico de movimentação
    dt_movimento = models.DateField()
    # NúmeroSis de Liquidação Gerado Em "funcoes.NumeroSisLiq". 
    numero_sisliq = models.IntegerField()

    class Meta:
        db_table = u'nhistorico_movimento'


'''
    Classe Serie
        Define as Sries que Poderam ser Usadas nas Notas Fiscais.
'''
class Serie(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Id da serie.
    id_serie = models.IntegerField(primary_key=True)
    # Nome da Serie.
    nome_serie = models.CharField(max_length=20)
    # Sequencia da Numeração da Serie.
    sequencia = models.CharField(max_length=8)
    # Código do Documento Fiscal.
    cod_doc_fiscal = models.CharField(max_length=2)
    # Nota Fiscal de Produtos e Serviços?
    nf_prod_serv = models.IntegerField()
    # Tipo de Nota Fiscal Que Será Emitida Nesta Série.
    tipo_nf_emitida = models.CharField(max_length=1)
    # Indica se a Serie Esta Ativa.
    ativo = models.IntegerField()

    class Meta:
        db_table = u'nserie'


'''
    Classe Banco
        Define os dados referentes a um banco
'''
class Banco(models.Model):
    # Identificador do banco
    id_banco = models.IntegerField(primary_key=True)
    # Código de compensação do banco (Identificador)
    cod_compensacao = models.IntegerField()
    # Nome do banco
    nome_banco = models.CharField(max_length=100)
    # Status de banco ativo
    ativo = models.IntegerField(max_length=1, default=1)

    class Meta:
        db_table = u'nbanco'


'''
    Classe BancoEmpresa
        Define os dados referentes a um relacionamento de um banco com a empresa
'''
class BancoEmpresa(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do relacionamento de um banco com uma empresa
    id_banco_empresa = models.IntegerField()
    # Código de compensação do banco
    cod_compensacao = models.IntegerField(primary_key=True)
    # Nome do banco
    nome_banco = models.CharField(max_length=100, default=None)
    # Status de banco ativo
    ativo = models.IntegerField(max_length=1, default=1)

    class Meta:
        db_table = u'nbanco_empresa'


'''
    Classe NotaFiscalSaidaC
        Define os dados referentes aos cabeçalhos das notas fiscais de saída.
'''
class NotaFiscalSaidaC(models.Model):
    # Identificador do cabeçalho da nota fiscal de saída (código da venda)
    id_notafiscal_saida_c = models.IntegerField(primary_key=True)
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do cliente (No caso de inutilização, recebe o id do consumidor final - 0).
    id_cliente = models.IntegerField()
    # Identificador do vendedor.
    id_vendedor = models.IntegerField(default=0)
    # Número da nota fiscal de saída (Quando a nota for inutilizada este campo se refere a numeração inicial)
    numero_nf = models.CharField(max_length=8)
    # (Utilizado para inutilização) Número da nota fiscal de saída final da inutilização de numeração
    numero_nf_final = models.CharField(max_length=8)
    # Série da nota fiscal de saída.
    serie = models.CharField(primary_key=True, max_length=20)
    # Natureza da operação
    cfop = models.IntegerField()
    # Tipo de finalidade da nfe
    finalidade_nfe = models.IntegerField(default=1)
    # Data de Movimentação da Nota Fiscal de saída (No caso de inutilização, recebe a data que a numeração foi 
    # inutilizada).
    data_movimentacao = models.DateTimeField(default=None)
    # Data de saída da nota fiscal de saída (apenas nota fiscal de saída)
    data_saida = models.DateTimeField(default=None)
    # Data da venda
    data_venda = models.DateField(default=None)
    # Valor do desconto da nota fiscal de saída.
    desconto = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Encargos/despesas da nota fiscal de saída.
    encargos = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Valor total da nota fiscal de saída com descontos.
    total_nf = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Define a espécie da nota fiscal de saída.
    especie = models.CharField(max_length=2, default='55')
    # Identificador da condição de pagamento
    codigo_condicao_pagamento = models.IntegerField()
    # Indica se valor do Item (vProd) entra no valor total da nota fiscal de saída (vProd)
    ind_tot = models.IntegerField(max_length=1, default=1)
    # Origem da mercadoria
    origem = models.IntegerField(max_length=1, default=0)
    # Observações sobre a nota fiscal de saída
    observacao = models.TextField(default=None)    
    # Identificador da transportadora
    id_transportadora = models.CharField(max_length=25, default=None)
    # Modalidade do frete
    frete_por_conta = models.IntegerField(max_length=1, default=9)
    # Registro Nacional de Transportador de Carga (ANTT) (Transportadora)
    codigo_antt = models.CharField(max_length=8, default=None)
    # Placa do veículo (Transportadora)
    placa_veiculo = models.CharField(max_length=7, default=None)
    # UF do veículo (Transportadora)
    uf_veiculo = models.CharField(max_length=2, default=None)
    # Valor do frete (Transportadora)
    valor_frete = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # Valor do seguro (Transportadora)
    valor_seguro = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # Quantidade dos volumes transportados (Transportadora)
    quantidade_frete = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # Espécie (Transportadora)
    especie_transportadora = models.CharField(max_length=20, default=None)
    # Marca dos volumes transportados
    marca = models.CharField(max_length=60, default=None)
    # Peso líquido (Transportadora)
    peso_bruto = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Peso bruto (Transportadora)
    peso_liquido = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Data e horário de saída da nota (Transportadora)
    horario_saida = models.DateTimeField(default=None, null=True)
    # Status da nota fiscal de saída (0 - Pedido aberto, 1 - Pedido faturado, 2 - NF-e transmitida, 
    # 3 - NF-e cancelada, 4 - Numeração inutilizada, 5 - NF-e em processo, 6 - NF-e de devolução)
    status_nota = models.IntegerField(max_length=1, default=0)
    # Texto de justificativa de nota fiscal de saída (Utilizado apenas nos casos de cancelamento e inutilização)
    justificativa_nfe = models.TextField(default=None)
    # Chave de identificação da nota fiscal de saída
    chave_nfe = models.TextField(default=None)
    # Número do protocolo de recebimento da nota fiscal de saída
    protocolo_nfe = models.TextField(default=None)
    # Número do protocolo de cancelamento da nota fiscal de saída
    protocolo_cancelamento_nfe = models.TextField(default=None)
    # Número do sistema da nota fiscal de saída
    numero_sis = models.IntegerField()
    # Total do ICMS
    totalicms = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Total da BASE do ICMS
    totalbaseicms = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Total do IPI
    totalipi = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Total do Pis
    totalpis = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Total do COFINS
    totalcofins = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Total da ST
    totalst = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Total da Base ST
    totalbasest = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Total do ISS
    totaliss = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Total dos Produtos
    totalprodutos = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Total FCP
    valorfcp = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Total ICMS Destino
    valoricmsremet = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Total ICMS Remetente
    valoricmsdest = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Status de nfc-e
    nfce = models.IntegerField(default=0)
    # Status de NF-e de saída que foi devolvida
    nfe_devolvida = models.IntegerField(default=0)
    # Chave de identificação da nota fiscal de origem (modo devolução)
    chave_nfe_original_devolucao = models.TextField(default=None)
    #
    forma_pagamento = models.CharField(max_length=2)
    # Código da Venda no Sistema E-gestão.
    cod_venda = models.CharField(max_length=8)
    # Código do Tipo de Compra e Venda no Sistema E-gestão.
    cod_tp_venda = models.CharField(max_length=2)
    # Identificador da OS (apenas ordens de serviço)
    id_os = models.CharField(max_length=11)
    # Solicitante da OS (apenas ordens de serviço)
    nome_solicitante = models.CharField(max_length=30)
    # Código do Status da OS (apenas ordens de serviço)
    status_os = models.IntegerField(max_length=2, default=0)
    # Identificador do ponto de coleta (apenas ordens de serviço)
    id_ponto_coleta = models.IntegerField(default=0)
    # Data da coleta (apenas ordens de serviço)
    data_coleta = models.DateField(default=None)
    # Hora do início da coleta (apenas ordens de serviço)
    hora_inicial_coleta = models.TimeField(default=None)
    # Hora do fim da coleta (apenas ordens de serviço)
    hora_final_coleta = models.TimeField(default=None)
    # Identificador do ponto de entrega da coleta (apenas ordens de serviço)
    id_ponto_entrega = models.IntegerField(default=0)
    # Data da entrega da coleta (apenas ordens de serviço)
    data_entrega = models.DateField(default=None)
    # Hora do início da entrega da coleta (apenas ordens de serviço)
    hora_inicial_entrega = models.TimeField(default=None)
    # Hora do fim da entrega da coleta (apenas ordens de serviço)
    hora_final_entrega = models.TimeField(default=None)
    # Forma de Entrega (01 - Retira Loja, 02 - Entrega Loja, 03 - Correios, 04 - Transportadora)
    forma_entrega = models.CharField(max_length=2)
    # Identificador do motorista da (apenas ordens de serviço)
    id_motorista = models.IntegerField(default=0)
    # Nome do contato que irá receber a entrega (apenas ordens de serviço)
    nome_recebedor = models.CharField(max_length=100)
    # Data real que a coleta foi realizada (apenas ordens de serviço)
    data_real_col = models.DateField(default=None)
    # Hora real que a coleta foi realizada (apenas ordens de serviço)
    hora_real_col = models.TimeField(default=None)
    # ID do Usuario que registrou a coleta (apenas ordens de serviço)
    id_usuario_col = models.IntegerField(default=0)
    # Observacao sobre a coleta (apenas ordens de serviço)
    obs_col = models.TextField(default=None)    
    # Nome do funcionário que realizou a coleta (apenas ordens de serviço)
    nome_func_col = models.CharField(max_length=100)
    # Data real que a entrega foi realizada (apenas ordens de serviço)
    data_real_ent = models.DateField(default=None)
    # Hora real que a emtrega foi realizada (apenas ordens de serviço)
    hora_real_ent = models.TimeField(default=None)
    # ID do Usuario que registrou a entrega (apenas ordens de serviço)
    id_usuario_ent = models.IntegerField(default=0)
    # Observacao sobre a entrega (apenas ordens de serviço)
    obs_ent = models.TextField(default=None)    
    # Nome do funcionário que realizou a entrega (apenas ordens de serviço)
    nome_func_ent = models.CharField(max_length=100)
    #Quantidade de Volumes Impressos pelo usuário
    quantidade_volumes_impresso = models.IntegerField(default=0)
    # Código da Sub-Empresa
    codempresa = models.IntegerField(primary_key=True, max_length=2)

    class Meta:
        db_table = u'nnotafiscal_saida_c'  


'''
    Classe NotaFiscalI
        Define os dados referentes aos itens das notas fiscais de saída.
'''
class NotaFiscalSaidaI(models.Model):
    # Identificador do item da nota fiscal de saída
    id_notafiscal_saida_i = models.AutoField(primary_key=True)
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código da venda.
    id_notafiscal_saida_c = models.IntegerField(primary_key=True)
    # Identificador do produto da nota fiscal de saída.
    id_produto = models.IntegerField(primary_key=True)
    # Quantidade do produto da nota fiscal de saída.
    quantidade = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    # Valor unitário do oroduto da nota fiscal de saída.
    preco = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    # Número do item da nota fiscal de saída.
    num_item = models.IntegerField(primary_key=True)
    # Origem da mercadoria
    origem = models.IntegerField(max_length=1, default=0)
    # Valor do ICMS ST retido
    aliq_st = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    # Valor da BC do ICMS ST retido
    base_st = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    # Unidade de medida do priduto
    unidade = models.CharField(max_length=2)
    # Çódigo de situação tributária (CST)
    tributacao = models.CharField(max_length=3)
    # Çódigo de situação tributária (CST)
    tributacao_csosn = models.CharField(max_length=3)
    # Alíquota de IPI
    aliq_ipi = models.DecimalField(max_digits=15, decimal_places=4)
    # Alíquota de ISS
    aliq_iss = models.DecimalField(max_digits=15, decimal_places=4)
    # Alíquota de ICMS
    aliq_icms = models.DecimalField(max_digits=15, decimal_places=4)
    # Valor base de ICMS
    base_icms = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Alíquota de ICMS ST
    aliq_icmsst = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Alíquota de PIS
    pis = models.DecimalField(max_digits=15, decimal_places=4)
    # Alíquota de COFINS
    cofins = models.DecimalField(max_digits=15, decimal_places=4)
    # Valor da base de INSS
    base_inss = models.DecimalField(max_digits=15, decimal_places=4)
    # Çódigo de situação tributária de IPI
    cst_ipi = models.CharField(max_length=2)
    # Çódigo de situação tributária de PIS
    cst_pis = models.CharField(max_length=2)
    # Çódigo de situação tributária de COFINS
    cst_cofins = models.CharField(max_length=2)
    # Valor Imposto de Importação
    imposto_importacao = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor de despesas aduaneira
    despesas_aduaneira = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor de IOF
    #iof = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Peso bruto do produto
    peso_bruto = models.DecimalField(max_digits=15, decimal_places=4)
    # Peso líquido do produto
    peso_liquido = models.DecimalField(max_digits=15, decimal_places=4)
    # Valor de desconto do produto
    valor_desconto = models.DecimalField(max_digits=15, decimal_places=4)
    # Define se o item terá seu preço somado no total da nota fiscal de saída
    ind_tot = models.IntegerField(max_length=1)
    # Identificador da grade de produto
    grade = models.TextField(default=None)
    # Valor de desconto rateado
    desconto_rateado = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor de acréscimo rateado
    acrescimo_rateado = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor de frete rateado
    frete_rateado = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor de seguro rateado
    seguro_rateado = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor de total líquido considerando os campos rateados
    total_liquido = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor total de IPI
    valoripi = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor total de ICMS
    valoricms = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor total de St
    valorst = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor total de PIS
    valorpis = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor total de Cofins
    valorcofins = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor total de Base ST
    valorbasest = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor total de Base Icms
    valorbaseicms = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor total de Base Pis Cofins
    valorbasepiscofins = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # CFOP do item
    cfop_item = models.IntegerField(default=None)
    # Alíquota de FCP
    aliqfcp = models.DecimalField(max_digits=15, decimal_places=4)
    # ICMS Destino
    icmsdestino = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # ICMS Remetente
    icmsremetente = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Valor FCP
    valorfcp = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # ICMS Partilha
    icmspartilha = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Aliquota InterEstadual
    aliquotainterestadual = models.DecimalField(max_digits=15, decimal_places=4)
    # Aliquota Interna
    aliquotainterna = models.DecimalField(max_digits=15, decimal_places=4)
    # BASE da DIFAL
    basedifal = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    #
    cod_venda = models.CharField(max_length=8)
    #
    origem_venda = models.CharField(max_length=8)
    #
    seguro_rateado = models.DecimalField(max_digits=15, decimal_places=4)
    #
    tributacao_csosn = models.CharField(max_length=8)
    # Código do Status da OS (apenas ordens de serviço)
    id_os = models.CharField(max_length=11)
    # Identificador do ponto de coleta (apenas ordens de serviço)
    id_tipo_servico = models.IntegerField(default=0)
    # Código da Sub-Empresa
    codempresa = models.IntegerField(primary_key=True, max_length=2)
    
    class Meta:
        unique_together = ('id_notafiscal_saida_i')
        db_table = u'nnotafiscal_saida_i'


'''
    Classe NotaFiscalSaidaCP
        Define os Dados Referentes as condições de pagamento de uma nota fiscal de saída.
'''
class NotaFiscalSaidaCP(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador da condição de pagamento de uma nota fiscal de saída.
    id_notafiscal_saida_cp = models.IntegerField(primary_key=True)
    # Identificador do cabeçalho da nota fiscal
    id_notafiscal_saida_c = models.IntegerField()
    # Dias de prazo para pagamento da parcela
    dias_prazo = models.IntegerField()
    # Data de pagamento da parcela
    data_parcela = models.DateField()
    # Valor da parcela
    valor_parcela = models.DecimalField(max_digits=14, decimal_places=2)

    class Meta:
        db_table = u'nnotafiscal_saida_cp'


'''
    Classe NotaFiscalSaidaDadosCliente
        Define os Dados Referentes aos dados persinalizados de um cliente na NF de saída.
'''
class NotaFiscalSaidaDadosCliente(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do cabeçalho da nota fiscal
    id_notafiscal_saida_c = models.IntegerField(primary_key=True)
    # Identificador do cliente
    id_cliente = models.IntegerField(default=0)
    # Nome do cliente
    nome_cliente = models.CharField(max_length=100)
    # CPF/CNPJ do cliente
    cpf_cnpj = models.CharField(max_length=14, default=0)
    # Telefone do cliente
    telefone = models.CharField(max_length=14, default=None)
    # Email do cliente
    email = models.CharField(max_length=50, default=None)
    # cep do endereco principal do cliente
    cep_endereco_principal = models.CharField(max_length=9)
    # endereço principal do cliente
    endereco_principal = models.CharField(max_length=90)
    # número do endereço principal do cliente
    numero_endereco_principal = models.IntegerField()
    # complemento do endereço principal do cliente
    complemento_endereco_principal = models.CharField(max_length=90, default=None)
    # bairro do endereço principal do cliente
    bairro_endereco_principal = models.CharField(max_length=90)
    # código da cidade do endereço principal do cliente
    cidade_endereco_principal = models.IntegerField()
    # código do uf do endereço principal do cliente
    estado_endereco_principal = models.IntegerField()
    # Número da Incrição Estadual do cliente
    inscricao_estadual = models.CharField(max_length=20)
    # Status de consumidor final
    consumidor_final = models.CharField(max_length=1, default='S')
    # Status de cliente contributinte de ICMS
    contribuinte_icms = models.IntegerField(max_length=1, default=0)

    class Meta:
        db_table = u'nnotafiscal_saida_dados_cliente'


'''
    Classe NotaFiscalEntradaC
        Define os dados referentes aos cabeçalhos das notas fiscais de entrada.
'''
class NotaFiscalEntradaC(models.Model):
    # Identificador do cabeçalho da nota fiscal de entrada (código da venda)
    id_notafiscal_entrada_c = models.IntegerField()
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do cliente (No caso de inutilização, recebe o id do consumidor final - 0).
    id_fornecedor = models.IntegerField()
    # Número da nota fiscal de entrada (Quando a nota for inutilizada este campo se refere a numeração inicial)
    numero_nf = models.CharField(max_length=8, primary_key=True)
    # Série da nota fiscal de entrada.
    serie = models.CharField(primary_key=True, max_length=20)
    # Define a espécie da nota fiscal de entrada.
    especie = models.CharField(max_length=2, default='55')
    # Valor total da nota fiscal de entrada com descontos.
    total_nf = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Data de emissão da nota fiscal de entrada
    data_emissao = models.DateField(default=None)
    # Data da venda da nota fiscal de entrada
    data_entrada = models.DateField(default=None)
    # Valor GNRE da nota fiscal de entrada
    valor_gnre = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Identificador da condição de pagamento da nota fiscal de entrada
    codigo_condicao_pagamento = models.IntegerField()
    # Carteira da nota fiscal de entrada
    carteira = models.IntegerField()
    # Número do banco da nota fiscal de entrada
    banco = models.CharField(max_length=5)
    # Número da agência da nota fiscal de entrada
    agencia = models.CharField(max_length=5)
    # Número GNRE da nota fiscal de entrada
    numero_gnre = models.IntegerField(default=0)
    # Mês ano da nota fiscal de entrada
    mes_ano = models.CharField(max_length=7, default=None)
    # KWH cons da nota fiscal de entrada
    kwh_cons = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Código energ da nota fiscal de entrada
    cod_energ = models.IntegerField(default=0)
    # Situação do documento da nota fiscal de entrada
    situacao_documento = models.IntegerField()
    # Observações sobre a nota fiscal de entrada
    observacao = models.TextField(default=None)
    # Valor de cotação do dólar da nota fiscal de entrada
    valor_dolar = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Data da contação do dólar da nota fiscal de entrada
    data_dolar = models.DateField(default=None)
    # Tributação de outras da nota fiscal de entrada
    tributacao_outras = models.IntegerField()
    # Tipo de compra da nota fiscal de entrada
    tipo_compra = models.CharField(max_length=4)
    # Identificador da transportadora (transportadora)
    id_transportadora = models.CharField(max_length=25, default=None)
    # Modalidade do frete (transportadora)
    frete_por_conta = models.IntegerField(max_length=1, default=9)
    # Número conhecimento (transportadora)
    numero_conhecimento = models.CharField(max_length=8, default=None)
    # Série(transportadora)
    serie_transportadora = models.CharField(max_length=20)
    # Valor do frete (transportadora)
    valor_frete = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Valor base de ICMS de emissão (transportadora)
    valor_base_icms_emissao = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Valor de despesas (transportadora)
    despesas_ac = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Valor de aliquota ICMS do frete
    aliquota_icms_transportadora = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Peso do produto (Transportadora)
    peso = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Tipo de frete (transportadora)
    tipo_frete = models.IntegerField(default=None)
    # Tributação de frete (transportadora)
    tributacao_frete = models.IntegerField(default=None)    
    # Chave de identificação da nota fiscal de entrada
    chave_nfe = models.TextField(default=None)
    # Número do protocolo de recebimento da nota fiscal de entrada
    protocolo_nfe = models.TextField(default=None)
    # Número do sistema da nota fiscal de entrada
    numero_sis = models.IntegerField()
    # Número da conta da nota fiscal de entrada
    conta = models.CharField(max_length=20)
    # Status de nota fiscal de entrada ativa
    ativo = models.IntegerField(max_length=1, default=1)
    # Status de NF-e de saída que foi devolvida
    nfe_devolvida = models.IntegerField(default=0)
    # Id da nota fiscal de entrada (CT-e)
    id_notafiscal_entrada_c_origem = models.IntegerField(default=None)
    # Série da nota fiscal de entrada (CT-e)
    serie_nf_origem = models.CharField(max_length=20, default=None)
    # Número da nota fiscal de entrada (CT-e)
    numero_nf_origem = models.CharField(max_length=8, default=None)
    # Id do fornecedor a nota fiscal de entrada (CT-e)
    id_fornecedor_origem = models.IntegerField(default=None)
    # Valor da mercadoria (CT-e)
    valor_mercadoria = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Data de emissão (CT-e)
    data_emissao_cte = models.DateField(default=None)
    # Base ICMS (CT-e)
    base_icms_transportadora = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    # Valor ICMS (CT-e)
    valor_icms_transportadora = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # CST (CT-e)
    cst_transportadora = models.CharField(max_length=2, default=None)
    # PIS (CT-e)
    pis_transportadora = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # COFINS (CT-e)
    cofins_transportadora = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Situação do documento (CT-e)
    situacao_documento_cte = models.IntegerField(default=None)
    # Valor do desconto (CT-e)
    valor_desconto_transporte = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Chave (CT-e)
    chave_cte = models.TextField(default=None)
    # Protocolo (CT-e)
    protocolo_cte = models.TextField(default=None)
    # 
    valor_base_gnre = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    valor_prod_g = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    base_icms = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    total_icms = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    base_st = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    valor_st = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    total_produto = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    e_financ = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    base_ipi = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    total_ipi = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    base_pis_cofins = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    valor_pis = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    valor_cofins = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    valor_ii = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    valor_aduaneiro = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    total_valor_desconto = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    outras = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 
    valor_iss = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    #
    data_gnre = models.DateField(default=None)
    #
    data_pagamento_gnre = models.DateField(default=None)
    #
    isentas = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Código da Sub-Empresa
    codempresa = models.IntegerField(primary_key=True, max_length=2)


    class Meta:
        db_table = u'nnotafiscal_entrada_c'  


'''
    Classe NotaFiscalEntradaI
        Define os dados referentes aos itens das notas fiscais de entrada.
'''
class NotaFiscalEntradaI(models.Model):
    # Identificador do item da nota fiscal de entrada
    id_notafiscal_entrada_i = models.AutoField(primary_key=True)
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código do cabeçalho da nota fiscal de entrada.
    id_notafiscal_entrada_c = models.IntegerField(primary_key=True)
    # Identificador do produto da nota fiscal de entrada.
    id_produto = models.IntegerField(primary_key=True)
    # Unidade de medida do produto da nota fiscal de entrada.
    unidade = models.CharField(max_length=2)
    # Valor unitário do oroduto da nota fiscal de entrada.
    preco = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Quantidade do produto da nota fiscal de entrada.
    quantidade = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Valor de desconto do produto da nota fiscal de entrada.
    desconto = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Alíquota de ICMS do produto da nota fiscal de entrada.
    aliq_icms = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Alíquota de ICMS do produto da nota fiscal de entrada.
    aliq_base_icms = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Alíquota de IPI do produto da nota fiscal de entrada.
    aliq_ipi = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Valor de ipi unitário do produto da nota fiscal de entrada.
    valor_ipi_unitario = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Çódigo de situação tributária de IPI do produto da nota fiscal de entrada.
    cst_ipi = models.CharField(max_length=2, default=None)
    # CST do produto da nota fiscal de entrada.
    cst = models.CharField(max_length=3, default=None)
    # CSOSN do produto da nota fiscal de entrada.
    csosn = models.CharField(max_length=3, default=None)
    # Alíquota de PIS do produto da nota fiscal de entrada.
    pis = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Alíquota de COFINS do produto da nota fiscal de entrada.
    cofins = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Valor do ICMS ST retido do produto da nota fiscal de entrada.
    aliq_st = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Valor do ICMS r ST retido do produto da nota fiscal de entrada.
    aliq_r_st = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Alíquota de ICMS ST do produto da nota fiscal de entrada.
    aliq_icms_st = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Classificação fiscal do produto da nota fiscal de entrada.
    classificacao_fiscal = models.IntegerField(default=0)
    # Tipo fiscal do produto da nota fiscal de entrada.
    tipo_fiscal = models.IntegerField(default=None)
    # Çódigo de situação tributária (CST) do produto da nota fiscal de entrada.
    tributacao = models.CharField(max_length=2, default=None)
    # Depósito do produto da nota fiscal de entrada.
    deposito = models.IntegerField(default=None)
    # Çódigo de situação tributária de PIS do produto da nota fiscal de entrada.
    cst_pis = models.CharField(max_length=2, default=None)
    # Çódigo de situação tributária de COFINS do produto da nota fiscal de entrada.
    cst_cofins = models.CharField(max_length=2, default=None)
    # Valor base de ICMS
    valor_base_icms = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Valor base de ICMS
    valor_icms = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Valor de base ST do produto da nota fiscal de entrada.
    valor_base_st = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Valor de ICMS ST do produto da nota fiscal de entrada.
    valor_icms_st = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Valor de base de IPI do produto da nota fiscal de entrada.
    valor_base_ipi = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Valor de IPI do produto da nota fiscal de entrada.
    valor_ipi = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Porcentagem de diferença de ICMS do produto da nota fiscal de entrada.
    diferenca_icms = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Número do do produto da nota fiscal de entrada.
    num_item = models.IntegerField(default=None)
    # Cert de qualidade do produto da nota fiscal de entrada.
    cert_qualidade = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # CFOP do item
    cfop_item = models.IntegerField(default=None)
    # U preço de custo
    u_preco_custo = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Código da Sub-Empresa
    codempresa = models.IntegerField(primary_key=True, max_length=2)

    class Meta:
        unique_together = ('nnotafiscal_entrada_i')
        db_table = u'nnotafiscal_entrada_i'


'''
    Classe NotaFiscalEntradaCP
        Define os Dados Referentes as condições de pagamento de uma nota fiscal de entrada.
'''
class NotaFiscalEntradaCP(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador da condição de pagamento de uma nota fiscal de entrada.
    id_notafiscal_entrada_cp = models.IntegerField(primary_key=True)
    # Identificador do cabeçalho da nota fiscal
    id_notafiscal_entrada_c = models.IntegerField()
    # Dias de prazo para pagamento da parcela
    dias_prazo = models.IntegerField()
    # Data de pagamento da parcela
    data_parcela = models.DateField()
    # Valor da parcela
    valor_parcela = models.DecimalField(max_digits=14, decimal_places=2)

    class Meta:
        db_table = u'nnotafiscal_entrada_cp'


'''
    Classe MensagemContato
        Define os Dados Referentes a uma mensagem de contato envidada da página inicial da aplicação.
'''
class MensagemContato(models.Model):
    # Identificador da mensagem de contato
    id_mensagem = models.IntegerField(primary_key=True)
    # Nome do remetente da mensagem de contato
    nome = models.CharField(max_length=90)
    # Telefone do remetente da mensagem de contato
    telefone = models.CharField(max_length=14)
    # Email do remetente da mensagem de contato
    email = models.CharField(max_length=50)
    # Mensagem do remetente da mensagem de contato
    mensagem = models.TextField()
    # Status de mensagem lida
    mensagem_lida = models.IntegerField(max_length=1)

    class Meta:
        db_table = u'nmensagem_contato'


'''
    Classe ClassificacaoFiscal
        Define os Dados Referentes a uma classificação fiscal (NCM) padrão da receita Federal
'''
class ClassificacaoFiscal(models.Model):
    # Identificador da classificação fiscal
    id_classificacao_fiscal = models.CharField(max_length=10, primary_key=True)
    # Identificador formatado da classificação fiscal
    codigo_formatado = models.CharField(max_length=15)
    # Nome da classificação fiscal
    nome_classificacao_fiscal = models.TextField()
    # Início da vigência STR
    inicio_vigencia_str = models.DateField()
    # Fim da vigência STR
    fim_vigencia_str = models.DateField()
    # Número CEST da classificação fiscal
    cest = models.CharField(max_length=7, default=None)
    # Porcentagem de impostos para movimentação interna
    impinterno = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Porcentagem de impostos para movimentação no exterior
    impexterno = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Data que o NCM foi atualizado
    data_ultima_atualizacao = models.DateTimeField()
    # Data que o NCM foi analisado (comparado)
    data_analisado = models.DateTimeField()
    # Status de classificação fiscal ativa
    ativo = models.IntegerField(max_length=1)

    class Meta:
        db_table = u'nclassificacao_fiscal'


'''
    Classe ClassificacaoFiscalEmpresa
        Define os Dados Referentes a uma classificação fiscal de uma empresa
'''
class ClassificacaoFiscalEmpresa(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador da classificação fiscal da empresa
    id_classificacao_fiscal_empresa = models.IntegerField()
    # Código da classificação fiscal padrão
    id_classificacao_fiscal = models.CharField(max_length=10, primary_key=True)
    # Validade desta classificação fiscal da empresa
    validade = models.DateField(default=None)
    # Status de classificação com tributação de pis e cofins
    pis_cofins = models.TextField(default=None)
    # Código de PIS de entrada
    cst_pis_entrada = models.CharField(max_length=2, default=None)
    # Alíquota de PIS de entrada
    aliquota_pis_entrada = models.DecimalField(max_digits=15, decimal_places=4, default=None)
    # Código de PIS de saída
    cst_pis_saida = models.CharField(max_length=2, default=None)
    # Alíquota de PIS de saída
    aliquota_pis = models.DecimalField(max_digits=15, decimal_places=4, default=None)
    # Alíquota de IPI
    aliquota_ipi = models.DecimalField(max_digits=15, decimal_places=4, default=None)
    # Alíquota de ICMS
    aliquota_icms = models.DecimalField(max_digits=15, decimal_places=4, default=None)
    # Alíquota de ICMS ST
    aliquota_icmsst = models.DecimalField(max_digits=15, decimal_places=4, default=None)
    # Valor de base de ICMS
    base_icms = models.DecimalField(max_digits=15, decimal_places=4, default=None)
    # Valor de base de ST
    base_st = models.DecimalField(max_digits=15, decimal_places=4, default=None)
    # Código da natureza da receita
    natureza_receita = models.CharField(max_length=3, default=None)
    # Código de COFINS de entrada
    cst_cofins_entrada = models.CharField(max_length=2, default=None)
    # Alíquota de COFINS de entrada
    aliquota_cofins_entrada = models.DecimalField(max_digits=15, decimal_places=4, default=None)
    # Alíquota de COFINS de saída
    cst_cofins_saida = models.CharField(max_length=2, default=None)
    # Código de COFINS de saída
    aliquota_cofins = models.CharField(max_length=2, default=None)
    # Cst de tributação de entrada
    cst_entrada = models.CharField(max_length=3, default=None)
    # Código de subistituição tributária
    cst = models.CharField(max_length=3, default=None)
    # Código de Situação da Operação no Simples Nacional 
    csosn = models.CharField(max_length=3, default=None)
    # Código de tributação de consumo
    cst_cons = models.CharField(max_length=3, default=None)
    # Código do gênero de serviço
    codigo_genero = models.CharField(max_length=4, default=None)
    # Porcentagem de impostos para movimentação interna
    impinterno = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Porcentagem de impostos para movimentação no exterior
    impexterno = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # tipo de tributação ("C" - ICMS, "S" - Sem tributação, "I": Isento e "N": Não incidente)
    tributacao = models.CharField(max_length=1, default=None)
    # Cfop de venda padrão
    cfop_venda_padrao = models.IntegerField(default=None)
    # Cfop de venda padrão do consumidor
    cfop_venda_padrao_consumidor = models.IntegerField(default=None)
    # Código de gênero do ítem
    cod_genero_item = models.CharField(max_length=2, default=None)

    cod_exp_conf_tipi = models.CharField(max_length=3, default=None)
    # Código de IPI
    cst_ipi = models.CharField(max_length=2, default=None)
    # Código de IPI
    cst_ipi_consumidor = models.CharField(max_length=2, default=None)
    # Porcentagem de impostos para movimentação estadual
    imp_estadual = models.DecimalField(max_digits=15, decimal_places=4)
    # Porcentagem de impostos para movimentação municipal
    imp_municipal = models.DecimalField(max_digits=15, decimal_places=4)
    # Código tributário
    cod_tributario = models.CharField(max_length=3, default=None, null=True)

    class Meta:
        db_table = u'nclassificacao_fiscal_empresa'


'''
    Classe ClassificacaoFiscalEstado
        Define os Dados Referentes a uma classificação fiscal (NCM) de cada estado
'''
class ClassificacaoFiscalEstado(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador da classificação fiscal
    id_classificacao_fiscal_empresa = models.IntegerField()
    # Identificador da classificação fiscal de estado
    id_classificacao_fiscal_estado = models.IntegerField(primary_key=True)
    # Identificador do estado
    id_estado = models.IntegerField()
    # Valor do ICMS
    valor_icms = models.DecimalField(max_digits=15, decimal_places=4)
    # Valor de base do ICMS
    base = models.DecimalField(max_digits=15, decimal_places=4)
    # Valor de base do ICMS 
    icms_st = models.DecimalField(max_digits=15, decimal_places=4)
    # Tipo de CFOP
    tipo_cfop = models.CharField(max_length=2)
    # Código de Situação da Operação no Simples Nacional 
    csosn = models.CharField(max_length=3)
    # Valor de base do ICMS 
    base_icms_st = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        db_table = u'nclassificacao_fiscal_estado'


'''
    Classe NaturezaOperacao
        Define os Dados Referentes a uma natureza de operação (CFOP)
'''
class NaturezaOperacao(models.Model):
    # Identificador da natureza de operação
    id_natureza_operacao = models.IntegerField()
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Descrição da natureza de operação
    descricao = models.CharField(max_length=50)
    # Natureza da operação (para o mesmo UF da empresa)
    cfop_uf = models.CharField(primary_key=True, max_length=4)
    # Natureza da operação (para um UF diferente do UF da empresa)
    cfop_fora_uf = models.CharField(primary_key=True, max_length=4)
    # Nome da natureza da operação (para o mesmo UF da empresa)
    nome_natureza_operacao_uf = models.CharField(max_length=50)
    # Nome da natureza da operação (para um UF diferente do UF da empresa)
    nome_natureza_operacao_fora_uf = models.CharField(max_length=50)
    # Tipo de preço da natureza de operação
    tipo_preco = models.IntegerField()
    # Tipo de natureza de operação
    natureza_cfop = models.IntegerField()
    # Status de natureza de operação para nota fiscal de entrada ou saída
    tipo_cfop_entrada_saida = models.CharField(max_length=1, default='S')
    # Status de alterar preço da natureza de operação
    nf_e_altera_preco = models.IntegerField(max_length=1, default=0)
    # Status de movimentação de estoque da natureza de operação
    movimentar_estoque = models.IntegerField(max_length=1, default=0)
    # Status de gerar financeiro da natureza de operação
    gerar_financeiro = models.IntegerField(max_length=1, default=0)
    # Status de baixar estoque do produto na geração de nota fiscal da natureza de operação
    baixar_estoque_nf = models.IntegerField(max_length=1, default=0)
    # Status de validação de quantidade em estoque do produto da natureza de operação
    validar_estoque = models.IntegerField(max_length=1, default=0)
    # CST padrão da natureza de operação
    cst_cfop = models.CharField(max_length=3)
    # CST IPI padrão da natureza de operação
    cst_ipi_cfop = models.CharField(max_length=3)
    # CST PIS padrão da natureza de operação
    cst_pis_cfop = models.CharField(max_length=3)
    # CST COFINS padrão da natureza de operação
    cst_cofins_cfop = models.CharField(max_length=3)
    # Alíquota PIS padrão da natureza de operação
    aliq_pis_cfop = models.DecimalField(max_digits=15, decimal_places=2)
    # Alíquota COFINS padrão natureza de operação
    aliq_cofins_cfop = models.DecimalField(max_digits=15, decimal_places=2)
    # Natureza da recita padrão da natureza de operação
    natureza_receita_cfop = models.CharField(max_length=3)
    # Tipo de tributação padrão da natureza de operação
    tributacao_cfop = models.IntegerField()
    # Tipo de receita padrão da natureza de operação
    tipo_receita_cfop = models.IntegerField()
    # Tipo de crédito padrão da natureza de operação
    tipo_credito_cfop = models.IntegerField()
    # Natureza base de crédito padrão da natureza de operação
    natureza_base_credito_cfop = models.IntegerField()
    # Status de natureza de operação ativo
    ativo = models.IntegerField(max_length=1)
    # Status de atualizar preço de venda quando uma NF de entrada é gerada
    atualiza_preco_venda = models.IntegerField(max_length=1, default=0)
    # Status de nf-e de devolução para cliente
    devolucao_cliente = models.IntegerField(max_length=1, default=0)
    # Indica se a Venda é considerada Venda.
    considerar_venda = models.IntegerField(max_length=1, default=1)
    # Código do Tipo de Compra e Venda no Sistema E-gestão.
    cod_tp_venda = models.CharField(max_length=2)
    
    class Meta:
        db_table = u'nnatureza_operacao'


'''
    Classe Atributo
        Define os Dados Referentes a um atributo de um determinado produto
'''
class Atributo(models.Model):
    # Identificador do atributo de um determinado produto
    id_atributo = models.IntegerField(primary_key=True)
    # Identificador do grupo de atributos
    id_geral = models.IntegerField()
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Descrição do atributo de um determinado produto
    descricao = models.CharField(max_length=200)
    # Valor do atributo de um determinado produto
    valor = models.CharField(max_length=200)
    # Status do atributo de um determinado produto
    ativo = models.IntegerField(max_length=1)

    class Meta:
        db_table = u'natributo'


'''
    Classe AtributoProduto
        Define os Dados Referentes a um relacionamento de um atributo com um produto
'''
class AtributoProduto(models.Model):
    # Identificador do relacionamento de um atributo com um produto
    id_atributo_produto = models.IntegerField()
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do atributo
    id_atributo = models.IntegerField(primary_key=True)
    # Identificador do produto
    id_produto = models.IntegerField(primary_key=True)

    class Meta:
        db_table = u'natributo_produto'


'''
    Classe Representante
        Define os Dados Referentes a um representante
'''
class Representante(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do representante
    id_representante = models.IntegerField(primary_key=True)
    # Identificador do fornecedor deste representante
    id_fornecedor = models.IntegerField(primary_key=True)
    # Nome do representante
    nome_representante = models.CharField(primary_key=True, max_length=100)
    # Email do representante
    email = models.CharField(max_length=50)
    # Telefone do representante
    telefone = models.CharField(max_length=14)
    # Status de representante ativo
    ativo = models.IntegerField(max_length=1)
    # imagem do representante
    imagem = models.CharField(max_length=90)

    class Meta:
        db_table = u'nrepresentante'


'''
    Classe RepresentanteCliente
        Define os dados referentes a um relacionamento de um representante com um cliente
'''
class RepresentanteCliente(models.Model):
    # Identificador da tabela de relacionamento de um representante com um cliente
    id_representante_cliente = models.IntegerField()
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do representante
    id_representante = models.IntegerField(primary_key=True)
    # Identificador do cliente
    id_cliente = models.IntegerField(primary_key=True)

    class Meta:
        db_table = u'nrepresentante_cliente'


'''
    Classe Permissao
        Define os dados referentes a uma permissão de acesso de um usuário.
'''
class Permissao(models.Model):
    # Identificador da permissão de usuário
    id = models.IntegerField(primary_key=True)
    # Chave de identificação da permissão
    name = models.CharField(max_length=50)
    # Código de identificação do grupo de páginas pertencentes ao mesmo módulo
    content_type_id = models.IntegerField()
    # Descrição da permissão de usuário
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = u'auth_permission'


'''
    Classe Permissao (Temporária)
        Define os dados referentes a uma permissão de acesso de um usuário.
'''
class PermissaoEdicao(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)
    selecionado = models.IntegerField(max_length=1)


'''
    Classe PermissaoUsuario
        Define os dados referentes ao relacionamento de uma permissão de acesso com um usuário.
'''
class PermissaoUsuario(models.Model):
    # Identificador do relacionamento de uma permissão de acesso com um usuário
    id = models.IntegerField(primary_key=True)
    # Identificador do usuário
    user_id = models.IntegerField()
    # Identificação da permissão de usuário
    permission_id = models.IntegerField()

    class Meta:
        db_table = u'auth_user_user_permissions'


'''
    Classe PerfilUser
        Define os dados referentes a um perfil de usuário
'''
class PerfilUser(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do perfil de usuário
    id_perfiluser = models.IntegerField()
    # Nome do perfil do usuário
    nome_perfil = models.CharField(primary_key=True, max_length=100)
    # Perfil pode ser editado (0 - Não ou 1 - Sim)
    editavel = models.IntegerField()
    # Status de perfil de usuário ativo
    ativo = models.IntegerField()

    class Meta:
        db_table = u'nperfiluser'


'''
    Classe TipoUsuarioAdministrativo
        Define os dados referentes a um tipo de usuário, do modo administrativo
'''
class TipoUsuarioAdministrativo(models.Model):
    # Identificador do tipo de usuário
    id_tipo_usuario = models.IntegerField()
    # Nome do tipo do usuário
    nome_tipo_usuario = models.CharField(primary_key=True, max_length=50)
    # Status de perfil de usuário ativo
    ativo = models.IntegerField(default=1)

    class Meta:
        db_table = u'ntipo_usuario_administrativo'


'''
    Classe PerfilTelas
        Define os dados referentes as Telas do sistema
'''
class PerfilTelas(models.Model):
    # Identificador da Tela.
    id_tela = models.IntegerField(primary_key=True)
    # Nome da Tela.
    nome_tela = models.CharField(max_length=100)
    # Nome de Exibição da Tela.
    nome_exibicao = models.CharField(max_length=50)

    class Meta:
        db_table = u'nperfil_telas'


'''
    Classe PermissaoPerfil
        Define os dados referentes a um relacionamento de um perfil com o usuário
'''
class PermissaoPerfil(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Nome do Perfil
    nome_perfil = models.CharField(primary_key=True, max_length=10)
    # Nome da Tela.
    nome_opcao = models.CharField(primary_key=True, max_length=30)
    # Status de permissão de inclusão (1 - Sim, 0 = Não)
    inc = models.IntegerField()
    # Status de permissão de alteração (1 - Sim, 0 = Não)
    alt = models.IntegerField()
    # Status de permissão de exclusão (1 - Sim, 0 = Não)
    exc = models.IntegerField()
    # Status de permissão de impressão (1 - Sim, 0 = Não)
    imp = models.IntegerField()

    class Meta:
        db_table = u'npermissao_perfil'


'''
    Classe CondicaoPagamento
        Define os dados referentes a uma condição de pagamento
'''
class CondicaoPagamento(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código da condição de pagamento
    codigo_condicao_pagamento = models.IntegerField(primary_key=True)
    # Nome da condição de pagamento
    nome = models.CharField(max_length=30, primary_key=True)
    # Status de condição dce pagamento para nota fiscal de entrada e compras
    nf_entrada_compras = models.IntegerField(max_length=1)
    # Status de condição dce pagamento para nota fiscal de saída e vendas
    n_saidas_vendas = models.IntegerField(max_length=1)
    # Status de condĩção de pagamento ativa
    ativo = models.IntegerField(max_length=1)

    class Meta:
        db_table = u'ncondicao_pagamento'


'''
    Classe NumeroDiasCP
        Define os dados referentes aos dias de uma condição de pagamento
'''
class NumeroDiasCP(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código da condição de pagamento
    codigo_condicao_pagamento = models.IntegerField(primary_key=True)
    # Dia da condição de pagamento
    dia = models.IntegerField(primary_key=True)
    # Valor do dia da condição de pagamento
    valor = models.IntegerField()

    class Meta:
        db_table = u'nnumero_dias_cp'


'''
    Classe TipoDocumento
        Define os dados referentes a um tipo de documento.
'''
class TipoDocumento(models.Model):
    # Identificador do tipo de documento
    id_tipodocumento = models.IntegerField()
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Descrição do tipo de documento
    descricao = models.CharField(primary_key=True, max_length=50)
    # Sigla do tipo de documento
    sigla = models.CharField(max_length=2, default=None)
    # Status de tipo de documento que permite valor negativo no contas a receber
    valor_negativo = models.IntegerField(max_length=1)
    # Status de tipo de docuemnto ativo
    ativo = models.IntegerField(max_length=1)

    class Meta:
        db_table = u'ntipodocumento'


'''
    Classe Sequenciador
        Armazena Sequencias.
'''
class Sequenciador(models.Model):
    # Codigo de Registro da Emailmpresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Nome
    nome = models.CharField(max_length=50)
    # Valor
    valor = models.IntegerField(max_length=11)

    class Meta:
        db_table = u'sequenciador'


'''
    Classe CarteiraBancaria
        Define os dados referentes a uma carteira bancária.
'''
class CarteiraBancaria(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código da carteira bancária
    id_carteira_bancaria = models.IntegerField(primary_key=True)
    # Código da carteira
    codigo_carteira = models.CharField(max_length=3)
    # Descrição da carteira bancária
    descricao = models.CharField(max_length=100)
    # Tipo de carteira integrada a carteira bancária
    carteira_integrada = models.IntegerField(default=None)
    # Valor de comissão da carteira bancária
    comissao = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Abatimento de comissão da carteira bancária
    ab_comissao  = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    # Status de carteira bancária descontada
    descontada = models.IntegerField(max_length=1, default=0)
    # Conta interna vinculada a carteira bancária
    conta_interna_vinculada = models.IntegerField(default=None)
    # Status de opcional ativo (padrao: "S" ou "N")
    ativo = models.IntegerField(max_length=1, default=1)

    class Meta:
        db_table = u'ncarteira_bancaria'


'''
    Classe CarteiraBoleta
        Define os dados referentes a uma carteira de boleto.
        #Obs: O modelo carteira boleta, equivale aos dados referente a tela de configuração de boleto.
        (viewConfiguracaoBoleto,script_configuracao_boleto,nova_configuracao_boleto.html,configuracao_boleto.html)
'''
class CarteiraBoleta(models.Model):
    #Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Nosso numero da carteira
    #nosso_numero = models.IntegerField(primary_key=True)
    # Código do banco
    banco = models.IntegerField(primary_key=True)
    # Código da conta
    conta = models.CharField(primary_key=True, max_length=15)
    # Espécie
    especie = models.CharField(max_length=2)
    # Aceite
    aceite = models.CharField(max_length=1)
    # Codigo Cedente
    codigo_cedente = models.CharField(max_length=25)
    # Variação da Carteira
    variacao_carteira = models.CharField(max_length=25, default=None)
    # Convênio Lider
    convenio_lider = models.CharField(max_length=25, default=None)
    # Juros dia
    juros_dia = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    # Dias Protesto
    dias_protesto = models.IntegerField(default=0)
    # Desconto
    desconto = models.DecimalField(max_digits=10, decimal_places=3)
    # Multa
    multa = models.DecimalField(max_digits=10, decimal_places=3)
    # Banco imprime boleto
    imprime_boleto = models.IntegerField(max_length=1)
    # Número da carteira bancária
    carteira = models.CharField(primary_key=True, max_length=15, default=0)
    # Layout do arquivo de remessa (0 = cnab 240, 1 = cnab 400)
    layout_arquivo = models.IntegerField(default=0)
    # Status de ativo (padrao: "S" ou "N")
    ativo = models.IntegerField(max_length=1, default=1)
    # Campo de descrição da carteira
    descricao = models.CharField(max_length=25, default='')
    # Campo de instrução 1 da carteira
    instrucao1 = models.TextField()
    # Campo de instrução 2 da carteira
    instrucao2 = models.TextField()
    # Campo de instrução 3 da carteira
    instrucao3 = models.TextField()
    # id_carteira
    id_carteira = models.IntegerField()
    # ùltima boleta emitida
    ultima_boleta_emitida = models.IntegerField(default=None)
    # Conta Padrão para geração de boletos e remessas
    cont_padrao_boleto_remessa = models.IntegerField(max_length=1, default=0)

    class Meta:
        db_table = u'ncarteira_boleta'


'''
    Classe Deposito
        Define os dados referentes a um depósito.
'''
class Deposito(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código do depósito
    id_deposito = models.IntegerField(primary_key=True)
    # Nome do depósito
    nome_deposito = models.CharField(max_length=100)
    # Status de depósito ativo (padrao: "S" ou "N")
    ativo = models.IntegerField(max_length=1, default=1)

    class Meta:
        db_table = u'ndeposito'


'''
    Classe Estoque
        Define os dados referentes a uma movimentação de estoque
'''
class Estoque(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Número do documento
    documento = models.CharField(max_length=8, primary_key=True)
    # Identificador do produto
    id_produto = models.IntegerField(primary_key=True)
    # Status da operação do estoque (E - nota fiscal de entrada; S - nota fiscal de saída; A - acerto de estoque
    # T - inventário provisório, N - Estorno de estoque)
    operacao = models.CharField(max_length=1, primary_key=True)
    # Identificador do estoque
    id_estoque = models.IntegerField()
    # Data da movimentação do estoque
    data_movimentacao = models.DateTimeField()
    # Quantidade do estoque antes da movimentação do estoque
    estoque_anterior = models.DecimalField(max_digits=10, decimal_places=2)
    # Quantidade da movimentação do estoque
    quantidade_movimentacao = models.DecimalField(max_digits=10, decimal_places=2)
    # Identificador do depósito
    id_deposito = models.IntegerField()
    # Núemro sis do estoque
    numero_sis = models.IntegerField()
    # Identificador do usuário que realizou a operação de movimentação de estoque
    id_usuario = models.IntegerField()
    # Número da nota fiscal
    numero_nf = models.CharField(max_length=100, default=None)
    # Status de operação com estorno
    estornado = models.IntegerField(max_length=1, default=0)
    # Identificador do estoque referente ao estorno, caso exista
    id_estoque_estorno = models.IntegerField(default=0)
    # Código da Sub-Empresa
    codempresa = models.IntegerField(primary_key=True, max_length=2)

    class Meta:
        db_table = u"nestoque"


'''
    Classe Financeira
        Define os dados referentes a uma financeira
'''
class Financeira(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador da financeira
    id_financeira = models.IntegerField(primary_key=True)
    # Nome da financeira
    nome_financeira = models.CharField(max_length=80)
    # Identificador da condição de pagamento
    id_condicao_pagamento = models.IntegerField(default=None)
    # Status de financeira ativa
    ativo = models.IntegerField(max_length=1, default=1)

    class Meta:
        db_table = u"nfinanceira"


'''
    Classe Cheque
        Define os dados referentes a um cheque
'''
class Cheque(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do cheque
    id_cheque = models.IntegerField(primary_key=True, unique=True)
    # Código do banco
    banco = models.CharField(max_length=3, primary_key=True)
    # Número da agência
    agencia = models.CharField(max_length=6, primary_key=True)
    # Número da conta
    conta = models.CharField(max_length=15, primary_key=True)
    # Data de abertura da conta
    data_abertura = models.DateField()
    # Número do cheque
    cheque = models.CharField(max_length=10, primary_key=True)
    # Data de emissão do cheque
    data_emissao = models.DateField()
    # Data de entrada do cheque
    data_entrada = models.DateField()
    # Valor do cheque
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    # Identificador do cliente
    id_cliente = models.IntegerField()
    # Descrição
    descricao = models.TextField()
    # Nome do Emitente.
    emitente = models.CharField(max_length=100)
    # Telefone do Emitente.
    telefone = models.CharField(max_length=14)
    # Endereço do Emitente.
    endereco = models.CharField(max_length=90)
    # CNPJ ou CPF do Emitente.
    cnpj_cpf = models.CharField(max_length=14)
    # RG do Emitente.
    rg = models.CharField(max_length=15)
    # Número do Sistema.
    numero_sis = models.CharField(max_length=15)
    # Número de Liquidação do Sistema.
    numero_sisliq = models.CharField(max_length=15)
    # Estornado ('S' = sim/ 'N' = não).
    estornado = models.CharField(max_length=1, unique=True)
    
    class Meta:
        db_table = u"ncheque"


'''
    Classe MotivoInventario
        Define os dados referentes a um motivo de inventário.
'''
class MotivoInventario(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código do motivo de inventário
    id_motivo_inventario = models.IntegerField(primary_key=True)
    # Motivo de inventário
    motivo = models.CharField(max_length=255)
    # Status de motivo de inventário ativo (padrao: "S" ou "N")
    ativo = models.IntegerField(max_length=1, default=1)

    class Meta:
        db_table = u'nmotivo_inventario'


'''
    Classe CartaCorrecao
        Define os dados referentes a uma carta de correção.
'''
class CartaCorrecao(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador da carta de correção
    id_carta = models.IntegerField(primary_key=True)
    # Número da Nota fiscal de saída
    numero_nf = models.CharField(primary_key=True,max_length=8)
    # Série da nota fiscal de saída
    serie = models.CharField(primary_key=True,max_length=20)
    # Identificador do usuário do sistema
    id_usuario = models.IntegerField()
    # Data da carta de correção
    data_carta = models.DateField()
    # Texto da carta de correção
    texto_carta = models.TextField()
    # Protocolo gerado na receita para carta de correção
    protocolo = models.CharField(max_length=30)
    # Sequencia de cartas transmitidas
    sequencia = models.CharField(max_length=11)

    class Meta:
        db_table = u'ncarta_correcao'


'''
    Classe CamposPadraoPesquisa
        Armazena os dados referentes a aos campos  preferenciais de pesquisa.
'''
class CamposPadraoPesquisa(models.Model):
    # Código de Registro da Empresa.
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Url da Tela.
    url_tela = models.CharField(primary_key=True, max_length=50)
    # Url da Pesquisa.
    url_pesquisa = models.CharField(primary_key=True, max_length=50)
    # Identificador do Usuário no Sistema.
    id_usuario = models.IntegerField(primary_key=True)
    # Campos à Serem Exibidos Por Padrão.
    campos = models.TextField()
    # Campo Pesquisado na Pesquisa Padrão.
    campo_padrao = models.CharField(max_length=30)

    class Meta:
        db_table = u'ncamp_padrao_pesq'


'''
    Classe ModuloSistema
        Define os dados referentes a um módulo de uso do sistema.
'''
class ModuloSistema(models.Model):
    # Identificador do módulo do sistema.
    id_modulo_sistema = models.CharField(primary_key=True)
    # Nome do módulo.
    nome_modulo = models.CharField(max_length=100)
    # status de módulo ativo.
    ativo = models.IntegerField(max_length=1)

    class Meta:
        db_table = u'nmodulo_sistema'


'''
    Classe ModuloTelas
        Define os dados referentes a um relacionamento entre um módulo e uma tela.
'''
class ModuloTelas(models.Model):
    # Identificador do relacionamento de um módulo com uma tela.
    id_modulo_tela = models.IntegerField()
    # Identificador do módulo.
    id_modulo_sistema = models.IntegerField(primary_key=True)
    # Identificador da tela.
    id_tela = models.IntegerField(primary_key=True)
    # Nome da tela
    nome_tela = models.CharField(max_length=100)

    class Meta:
        db_table = u'nmodulo_telas'


'''
    Classe Especie
        Define os dados referentes a uma espécie de NF-e.
'''
class Especie(models.Model):
    # Identificador da espécie de NF-e.
    id_especie = models.IntegerField()
    # Valor da espécie de NF-e.
    valor_especie = models.CharField(max_length=3, primary_key=True)
    # Descrição da espécie de NF-e.
    descricao_especie = models.CharField(max_length=255)
    # Status da espécie de NF-e
    ativo = models.IntegerField(max_length=1, default=1)

    class Meta:
        db_table = u'nespecie'


'''
    Classe Gostos
        Define os dados referentes ao gosto do restaurante.
'''
class Gostos(models.Model):
    # Identificador do Gosto.
    id_gosto = models.IntegerField()
    # Descrição do Gosto.
    descricao = models.CharField(max_length=100, primary_key=True)
    # Nom da Imagem do Gosto.
    imagem = models.CharField(max_length=100)    
    # data da última atualização
    data_ultima_atualizacao = models.DateTimeField()

    class Meta:
        db_table = u'ngosto'


'''
    Classe Gosto Restaurante
        Define os dados referentes ao gosto do restaurante.
'''
class GostoRestaurante(models.Model):
    # Identificador do Gosto.
    id_gosto_restaurante = models.IntegerField()
    # Código de Registro da Empresa.
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador que relaciona ao gosto.
    id_gosto = models.IntegerField(primary_key=True)

    class Meta:
        db_table = u'ngosto_restaurante'


'''
    Classe Gosto Restaurante
        Armazena o Cabeçalho dos Pedidos do App CardápioShow.
'''
class VendascChef(models.Model):
    # Código de Registro da Empresa.
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código do Pedido.
    cod_pedido = models.AutoField(primary_key=True)
    # Data e hora do Pedido.
    data_hora = models.DateTimeField()
    # Valor Total do Pedido.
    preco_total_pedido = models.DecimalField(max_digits=10, decimal_places=2)
    # Forma de Pagamento.
    forma_pagamento = models.CharField(max_length=30)    
    # Numero da Mesa.
    id_mesa_celular_ident = models.IntegerField()
    # Identificador do Dispositivo.
    id_celular = models.CharField(max_length=20)    
    # Identificador do Garçom.
    id_garcom = models.IntegerField()
    # Indica se o Tablet ja Exportou o Pedido.
    exportado = models.CharField(max_length=1)    
    # Indica se o Pedido ja Foi Importado Para o PDV.
    imppdv = models.CharField(max_length=1)    
    # Identificador do Cliente
    id_cliente = models.IntegerField()
    # Valor de Acrescimo do Pedido.
    valoracrescimo = models.DecimalField(max_digits=10, decimal_places=2)
    # Valor do Desconto do Pedido.
    valordesconto = models.DecimalField(max_digits=10, decimal_places=2)
    # Valor Recebido em Dinheiro.
    valordinheiro = models.DecimalField(max_digits=10, decimal_places=2)
    # Valor Recebido em Cartão de Débito.
    valordebito = models.DecimalField(max_digits=10, decimal_places=2)
    # Valor Recebido em Cartão de Crédito.
    valorcredito = models.DecimalField(max_digits=10, decimal_places=2)
    # Valor Recebido em Cheque.
    valorcheque = models.DecimalField(max_digits=10, decimal_places=2)
    # Valor do Troco Devolvido.
    valortroco = models.DecimalField(max_digits=10, decimal_places=2)
    #  Valor Bruto do Pedido.
    valorbruto = models.DecimalField(max_digits=10, decimal_places=2)
    # Indica se o Pedido Foi Cancelado.
    cancelado = models.CharField(max_length=1)
    # Status de venda ativa
    ativo = models.IntegerField(default=1)
    # Status de venda enviada para nuvem
    EnviadoNuvem = models.CharField(max_length=1)
    # Código de exportação
    cod_exportacao = models.BigIntegerField()
    # Hash do código de exportação
    hash_exportacao = models.TextField(default=None)
    # Status de importado pelo E-Gestão
    importado = models.CharField(max_length=1)
    # Data da última atualização do registro na tabela
    ultima_data_atualizacao = models.DateTimeField()
    # Status de tipo de entrega
    entrega = models.CharField(max_length=8)
    # Usuário que fez a venda
    CodUsuario = models.CharField(max_length=10)
    # Origem da venda ('A'->app 'S'->Site)
    OrigemDisp = models.CharField(max_length=1, default='S')
    # Tipo de venda
    cfop = models.IntegerField(default=1)
    # Nome do cartão de crédito
    nome_cartao = models.CharField(max_length=255, default=None)
    # Código do pedido gerado pelo Marketplace
    codigo_pedido_marketplace = models.CharField(max_length=255, default=None)

    class Meta:
        db_table = u'nvendasc_chef'


'''
    Classe Gosto VendasiChef
        Armazenas os Itens dos Pedidos da Tabela NVendasi_Chef.
'''
class VendasiChef(models.Model):
    # Código de Registro da Empresa.
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código do Pedido na Tabela NVendasc_Chef.
    cod_pedido_vendasc = models.IntegerField(primary_key=True)
    # Código do Pedido.
    cod_pedido = models.AutoField(primary_key=True)
    # Código do Produto.
    id_produto = models.IntegerField()
    # Preco do Produto.
    preco_produto = models.DecimalField(max_digits=10, decimal_places=2)
    # Quantidade do Produto.
    quantidade_produto = models.IntegerField()
    # Código do Opcional.
    id_opcional = models.IntegerField()
    # Preco do Opcional.
    preco_opcional = models.DecimalField(max_digits=10, decimal_places=2)
    # Quantidade do Opcional.
    quantidade_opcional = models.IntegerField()
    # Indica se o Pedido ja Foi Impresso.
    impresso = models.CharField(max_length=1)
    # Numero da Mesa.
    id_mesa_celular_ident = models.IntegerField()
    # Identificador do Garçom.
    id_garcom = models.IntegerField()
    # Identificador do Dispositivo.
    id_celular = models.CharField(max_length=20)
    # Indica se o Tablet ja Exportou o Pedido.
    exportado = models.CharField(max_length=1)
    # Indica se o Pedido Foi Cancelado.
    pedido_fechado = models.CharField(max_length=1)
    # Indica se o Pedido Foi Cancelado.
    pedido_finalizado = models.CharField(max_length=1)
    # Indica se o Pedido Foi Cancelado.
    visualizado = models.CharField(max_length=1)
    # Identificador do Cliente
    id_cliente = models.IntegerField()
    # Status de venda enviada para nuvem
    EnviadoNuvem = models.CharField(max_length=1)
    # Código de exportação
    cod_exportacao = models.BigIntegerField()
    # Hash do código de exportação
    hash_exportacao = models.TextField(default=None)
    # Status de importado pelo E-Gestão
    Importado = models.CharField(max_length=1)
    # Data da última atualização do registro na tabela
    ultima_data_atualizacao = models.DateTimeField()

    class Meta:
        db_table = u'nvendasi_chef'


'''
    Classe PostClienteCardapioShow
        Define os dados referentes ao gosto do restaurante.
'''
class PostClienteCardapioShow(models.Model):
    nome = models.CharField(max_length=100)

    email = models.CharField(max_length=100)

    telefone = models.CharField(max_length=15)

    class Meta:
        db_table= u'ncliente_chef'


'''
    Classe Cadusua
        Define os dados dos usuários para login nos aplciativos Ponto do Borracheiro e OrdemFácil
'''
class Cadusua(models.Model):
    name = models.CharField(max_length=255)

    email = models.CharField(max_length=255)

    CodRegistro = models.IntegerField(primary_key=True, max_length=14)

    CodUsuario = models.CharField(primary_key=True, max_length=10)

    CodVendedor = models.CharField(max_length=5)

    CodEmpresa = models.CharField(max_length=60)

    atualizacao_imp = models.CharField(max_length=93)

    atualizacao_exp = models.CharField(max_length=93)

    data_ultima_atualizacao = models.DateTimeField()

    class Meta:
        db_table= u'cadusua'


'''
    Classe Promocao
        Define os dados das promoções para o App CardápioShow
'''
class Promocao(models.Model):
    # codRegistro da tabela npromo
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # id das promocoes
    id_promocao = models.IntegerField(primary_key=True ,max_length = 11)
    # data de inicio da promocao
    dt_valini = models.DateField()
    #  data de termino da validade da promocao
    dt_valfim = models.DateField()
    # quantidade de promocoes existentes
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    # quantidade de promocoes iniciais
    quantidade_ini = models.DecimalField(max_digits=10, decimal_places=2)
    # regras de uso das promocoes
    regra = models.TextField()
    #imagem relacionada a promocao
    imagem =  models.CharField(max_length=200)
    #nome da promocao
    nomepromocao = models.CharField(max_length=100)
    #nome da Empresa
    nomecasa = models.CharField(max_length=100)
    # data de uso inicial
    dt_usoini = models.DateField()
    # data de uso Final
    dt_usofim = models.DateField()
    # PREÇO PROMOCIONAL
    precopromo = models.DecimalField(max_digits=10, decimal_places=2)
    # PREÇO NORMAL
    preconormal = models.DecimalField(max_digits=15, decimal_places=2)
    # ID do produto vinculado a esta promoção
    id_produto = models.IntegerField(default=None)
    # Quantidade em estoque desta promoção
    estoque_promocao = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    # Observação da promoção
    observacao = models.TextField(default=None)
    
    class Meta:
        db_table= u'npromocao'


'''
    Classe Cupom
        Define os dados cos cupons de uma promoção para o App CardápioShow
'''
class Cupom(models.Model):
    # codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # codigo do cupom  
    cod_cupom = models.CharField(max_length = 10)
    # id do Cliente que Comprou o cupom
    id_cliente = models.IntegerField(primary_key=True ,max_length = 11)
    # id da Promoção que o Cupom pertence
    id_promocao = models.IntegerField(primary_key=True ,max_length = 11)
    # data de uso do cupom
    dt_uso = models.DateField()
    # Se Valido S se não N
    valido = models.CharField(max_length=1)

    class Meta:
        db_table= u'ncupom'


'''
    Classe UsuarioChef
        Define os dados de um usuário do App CardápioShow
'''
class UsuarioChef(models.Model):
    #ID CLIENTE CHAVE PRIMARY
    id_cliente = models.CharField(max_length=11,primary_key=True)
    #Nome do Cliente
    nome = models.CharField(max_length=100)
    #CODREGISTRO DA EMPRESA A QUAL O CLIENTE PERTENCE
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    #EMAIL DO CLIENTE
    email = models.CharField(max_length=100)
    #Senha para login do CardapioShow
    senha = models.CharField(max_length=60)
    #Telefone para login do CardapioShow
    telefone = models.CharField(max_length=14)
    #Ativo se SIM 1 se NÃO 2
    ativo = models.IntegerField(max_length=1)
    #Cpf/Cnpj dos clientes cadastrados
    cpf_cnpj = models.CharField(max_length=14)
    

    class Meta:
        db_table= u'nusuario_chef'


'''
    Classe Circuito

'''
class Circuito(models.Model):
    #id circuito
    id = models.IntegerField(primary_key=True)
    #nome do circuito
    nome = models.CharField(max_length=100)
    #imagem do circuito
    imagem = models.CharField(max_length=300)

    class Meta:
        db_table=u'ncircuito'


'''
    Classe UsuaEmp

'''
class UsuaEmp(models.Model):
    # Username usuario.
    username = models.CharField(max_length=100, primary_key=True)
    # Codregistro.
    codregistro = models.IntegerField(primary_key=True, max_length=25)

    class Meta:
        db_table = u'usuaemp' 


'''
    Classe Contato
        Armazena os dados dos contatos cadastrados.
'''
class ContatoDados(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do contato
    id_contato = models.IntegerField(primary_key=True)
    # Nome do contato
    nome_contato = models.CharField(max_length=50)
    # Celular do contato
    celular_contato = models.CharField(max_length=20)
    # E-Mail do contato
    email_contato = models.CharField(max_length=50)
    # Data de nascimento do contato
    data_nascimento = models.DateField()
    # Status de contato ativo
    ativo = models.IntegerField(max_length=1)
    # Tipo de Contato "Externo/Interno"
    tipo_contato = models.CharField(max_length=1)
    # Nome da Imagem do Contato
    imagem = models.CharField(max_length=255)
    # Identificador do cliente
    id_cliente = models.IntegerField(default=0)
    # Entregador "S,1" ou "N,0"
    entregador = models.IntegerField(default=0)

    class Meta:
        db_table = u'ncontato'


'''
    Classe TipoServico
        Armazena os dados dos tipos de serviço cadastrados.
'''
class TipoServico(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do tipo de serviço
    id_tipo_servico = models.IntegerField(primary_key=True)
    # Nome do tipo de serviço
    nome = models.CharField(max_length=50)
    # Status de tipo de serviço ativo
    ativo = models.IntegerField(max_length=1)
    # Identificador do Produto
    id_produto = models.IntegerField(default=0)
    # Última data de atualização do tipo de serviço
    ultima_data_atualizacao = models.DateTimeField()

    class Meta:
        db_table = u'ntipo_servico'


'''
    Classe TipoServicoCliente
        Armazena os dados do vínculo de um cliente com um tipos de serviço cadastrados.
'''
class TipoServicoCliente(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do tipo de serviço/cliente
    id_tipo_servico_cliente = models.IntegerField()
    # Identificador do tipo de serviço
    id_tipo_servico = models.IntegerField(primary_key=True)
    # Identificador do cliente
    id_cliente = models.IntegerField(primary_key=True)
    # Valor do tipo de serviço/cliente
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    # Última data de atualização do tipo de serviço/cliente
    ultima_data_atualizacao = models.DateTimeField()

    class Meta:
        db_table = u'ntipo_servico_cliente'


'''
    Classe PontoColEnt
        Armazena os dados dos Pontos de Coleta e Entrega.
'''
class PontoColEnt(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do ponto de Coleta/Entrega
    id_ponto_col_ent = models.AutoField(primary_key=True)
    # Nome para Identificação do ponto do cliente
    nome = models.CharField(max_length=50)
    # Identificador do cliente do ponto
    id_cliente = models.IntegerField(primary_key=True)
    # Código de Endereço Postal da Coleta/Entrega
    cep = models.CharField(max_length=9)    
    # Endereço da Coleta/Entrega
    endereco = models.CharField(max_length=90)
    # Número do Endereço do ponto de Coleta/Entrega
    numero = models.IntegerField()
    # Complemento do Endereço da Coleta/Entrega
    complemento = models.CharField(max_length=90)
    # Identificador do Estado do Endereço do ponto
    id_estado = models.IntegerField()
    # Identificador da Cidade do Endereço do ponto
    id_cidade = models.IntegerField()
    # Bairro do Endereço da Coleta/Entrega
    bairro = models.CharField(max_length=90)
    # Ponto de Referência do Endereço da Coleta/Entrega
    ponto_referencia = models.CharField(max_length=90)
    # Status de tipo de serviço ativo
    ativo = models.IntegerField(max_length=1)

    class Meta:
        db_table = u'nponto_col_ent'        


'''
    Classe ProdutoCliente
        Armazena os dados do vínculo de um cliente com os produtos cadastrados.
'''
class ProdutoCliente(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código de Barra do Produto
    codbarra = models.CharField(max_length=20)
    # Identificador do Produto
    id_produto = models.AutoField(primary_key=True)
    # Identificador do cliente Relaciona ao Produto
    id_cliente = models.IntegerField(primary_key=True)    

    class Meta:
        db_table = u'nproduto_cliente'   


'''
    Classe ProdutoCliente
        Armazena os dados do vínculo de um cliente com os produtos cadastrados.
'''
class VdInsum(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código da Venda
    cod_venda = models.CharField(primary_key=True, max_length=11)
    # Identificador do cliente
    id_cliente = models.IntegerField(primary_key=True) 
    # Identificador da OS
    id_os = models.CharField(primary_key=True, max_length=11)
    # Identificador do Produto
    id_produto = models.IntegerField(primary_key=True)
    # Quantidade do Produto
    quantidade = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Valor do Produto
    valor = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        db_table = u'nvd_insum'


'''
    Classe Atendimento
        Define os daodos referentes ao atendimento realizado no webchat
'''
class Atendimento(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Numero do Whatsapp do Cliente
    num_zap_cliente = models.CharField(primary_key=True, max_length=15)
    # Identicador do atendimento
    id_atendimento = models.IntegerField(primary_key=True, max_length=11)
    # Status do atendimento
    status_atendimento = models.CharField(max_length=1)
    # Nome do Cliente
    nome_cliente = models.CharField(max_length=100)
    # Data do atendimento
    dt_atendimento = models.DateField(default=None)
    # Hora do atendimento
    hr_atendimento = models.TimeField(default=None)
    # Identificador do usuário
    id_usuario = models.IntegerField(max_length=11)
    # Identificador do Setor do Usuário
    id_setor = models.IntegerField(max_length=11)
    # Data da finalização do atendimento
    dt_atendimento_fim = models.DateField(default=None)
    # Hora da finalização do atendimento
    hr_atendimento_fim = models.TimeField(default=None)
    # Nome de quem finalizou o atendimento
    finalizado_por = models.CharField(max_length=100)
    
    class Meta:
        db_table = u'natendimento'

 
'''
    Classe AtendimentoMensagem
        Define os daodos referentes ao atendimento realizado no webchat
'''
class AtendimentoMensagem(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Numero do Whatsapp do Cliente
    num_zap_cliente = models.CharField(primary_key=True, max_length=15)
    # Identicador do atendimento
    id_atendimento = models.IntegerField(primary_key=True, max_length=11)
    # Armazena seuqencia das mensagens
    sequencia = models.AutoField(primary_key=True, max_length=11)
    # Situção
    situacao = models.CharField(max_length=1)
    # Mensagem
    msg = models.TextField(default=None) 
    # Resposta da Mensagem
    resp_msg = models.TextField(default=None)
    # Data da Mensagem
    dt_msg = models.DateField(default=None)
    # Hora da Mensagem
    hr_msg = models.TimeField(default=None)
    # Identificador do usuário
    id_usuario = models.IntegerField(max_length=11)
    # Nome Exibido no Chat
    nome_chat = models.CharField(max_length=100)
    # Indica se a Mensagm Foi Recebida no Servidor
    enviada = models.CharField(max_length=1, default=0)
    # Indica se a Mensagem Foi Recebida Pelo Usuário
    entregue = models.CharField(max_length=1, default=0)
    # Indica se a Mensagem Foi Lida Pelo Usuário
    lida = models.CharField(max_length=1, default=0)
    # Indica se a Mensagem Foi Notificada Para o Usuário
    notificada = models.CharField(max_length=1, default=0)

    class Meta:
        db_table = u'natendimento_msg'


'''
    Classe AtendimentoAgenda
        Define os dados referentes a agendamentos de atendimento do MegaZap
'''
class AtendimentoAgenda(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Numero do Whatsapp do Cliente
    num_zap_cliente = models.CharField(primary_key=True, max_length=15)
    # Identicador do atendimento
    id_atendimento = models.IntegerField(primary_key=True, max_length=11)
    # Identicador do agendamento
    id_agendamento = models.AutoField(primary_key=True, max_length=11)
    # Identicador do tipo de atendimento
    id_tipo_atendimento = models.IntegerField(max_length=1, default=0)
    # Não contatar
    nao_contatar = models.IntegerField(max_length=1)
    # Data do proximo contato
    data_novo_contato = models.DateTimeField()
    # Identificador do status de finalização
    id_status_finalizacao = models.IntegerField(max_length=1, default=0)
    # Observacao sobre a finalização do atendimento
    observacao = models.TextField(default=None) 
    
    class Meta:
        db_table = u'natendimento_agenda'


'''
    Classe Setor
        Define os dados referentes a um setor de trabalho do usuário
'''
class Setor(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do setor do usuário
    id_setor = models.IntegerField(primary_key=True)
    # Nome do setor do usuário
    nome_setor = models.CharField(max_length=50)
    # Status do setor do usuário - ativo = (0 - Não ou 1 - Sim)
    ativo = models.IntegerField()
    
    class Meta:
        db_table = u'nsetor'


'''
    Classe TpAtendimento
        Define os dados referentes a um setor de trabalho do usuário
'''
class TpAtendimento(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do tipo de atendimento
    id_tipo_atendimento = models.IntegerField(primary_key=True)
    # Nome do tipo de atendimento
    nome_tipo_atendimento = models.CharField(max_length=100)
    # Status do tipo de atendimento - ativo = (0 - Não ou 1 - Sim)
    ativo = models.IntegerField()
    
    class Meta:
        db_table = u'ntp_atend'


'''
    Classe StatusFinalizacao
        Define os dados referentes a um setor de trabalho do usuário
'''
class StatusFinalizacao(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do status de finalização
    id_status_finalizacao = models.IntegerField(primary_key=True)
    # Nome do status de finalização
    nome_status_finalizacao = models.CharField(max_length=100)
    # Status do status de finalização - ativo = (0 - Não ou 1 - Sim)
    ativo = models.IntegerField()
    
    class Meta:
        db_table = u'nstatus_fin'


'''
    Classe FormaPagamento
        Armazena os dados das formas de pagamento.
'''
class FormaPagamento(models.Model):
    # Código da forma de pagamento
    id_forma_pagamento = models.IntegerField()
    # Nome forma de pagamento
    nome_forma_pagamento = models.CharField(primary_key=True, max_length=100)
    # Status de forma de pagamento para ser enviada ao aplicativo
    enviaapp = models.IntegerField(default=0)
    # Status de forma de pagamento para ser enviada a loja virtual
    envialoja = models.IntegerField(default=0)
    # Status de forma de pagamento ativa
    ativo = models.IntegerField(default=1)
    # Última data de atualização da forma de pagamento
    ultima_data_atualizacao = models.DateTimeField()

    class Meta:
        db_table = u'nforma_pagamento'


'''
    Classe FormaEntrega
        Armazena os dados das formas de entrega.
'''
class FormaEntrega(models.Model):
    # Código da forma de entrega
    id_forma_entrega = models.IntegerField()
    # Nome forma de entrega
    nome_forma_entrega = models.CharField(primary_key=True, max_length=100) 
    # Status de forma de entrega para ser enviada ao aplicativo
    enviaapp = models.IntegerField(default=1)
    # Status de forma de entrega para ser enviada a loja virtual
    envialoja = models.IntegerField(default=1)
    # Status de forma de entrega ativa
    ativo = models.IntegerField(default=1)
    # Última data de atualização da forma de entrega
    ultima_data_atualizacao = models.DateTimeField()

    class Meta:
        db_table = u'nforma_entrega'


'''
    Classe ProdutoCategoria
        Define o relacionamento de um produto com um grupo
'''
class ProdutoCategoria(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do aplicativo
    id_aplicativo = models.IntegerField(default=0)
    # Identificador do grupo
    id_grupo = models.IntegerField(primary_key=True)
    # Identificador do produto
    id_produto = models.IntegerField(primary_key=True)

    class Meta:
        db_table = u"nproduto_categoria"


'''
    Classe Aplicativo
        Define os aplicativos nas quais os dados serão exibidos
'''
class Aplicativo(models.Model):
    # Identificador do aplicativo
    id_aplicativo = models.IntegerField(default=0)
    # Nome do aplicativo
    nome_aplicativo = models.CharField(primary_key=True, max_length=100)
    # Status de aplicativo ativo
    ativo = models.IntegerField(default=1)

    class Meta:
        db_table = u"naplicativo"


'''
    Classe EmpresaAplicativo
        Define o relacionamento de uma empresa com um aplicativo
'''
class EmpresaAplicativo(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do aplicativo
    id_aplicativo = models.IntegerField(primary_key=True, default=0)

    class Meta:
        db_table = u"nempresa_aplicativo"


'''
    Classe ComentarioProduroPedido
        Define os comentários de um cliente em relação ao produto ou pedido
'''
class ComentarioProduroPedido(models.Model):
    # Código de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do comentário
    id_comentario = models.IntegerField(primary_key=True)
    # Identificador do cliente ligado ao usuário que fez o comentário
    id_cliente = models.IntegerField()
    # Nome do usuário
    nome_usuario = models.CharField(max_length=255, default=None)
    # Identificador do produto
    id_produto = models.IntegerField()
    # Código do pedido
    cod_pedido = models.IntegerField()
    # Número de estrelas do comentário
    num_estrelas = models.IntegerField(default=0)
    # Comentário do usuário
    comentario = models.TextField(default=None)
    # Data e hora do comentário
    data_comentario = models.DateTimeField(default=0, auto_now_add=True)
    # Status de comentário ativo
    ativo = models.IntegerField(default=1)

    class Meta:
        db_table = u"ncomentario_produto_pedido"


'''
    Classe LojaMKPlace
        Define os atributos de uma loja.
'''
class LojaMKPlace(models.Model):
    #Identificador da loja
    id_loja = models.AutoField(primary_key=True)
    #Nome da loja
    nome_loja = models.CharField(primary_key=True, max_length=100)
    #Status de loja ativa
    ativo = models.IntegerField(default=1)

    class Meta:
        db_table = u'nlojas_mkplace'


'''
    Classe ApProducC
        Define os atributos do cabecalho de um apontamento.
'''
class ApProducC(models.Model):
    #Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    #Numero do apontamento
    num_apontamento = models.IntegerField(primary_key=True)
    #Numero da producao
    num_producao = models.CharField(max_length=12)
	#Numero da etapa
    num_etapa = models.CharField(max_length=12)
    #Codigo do funcionario
    cod_funcionario = models.CharField(max_length=4)
    #Data do apontamento
    dt_aponta = models.DateField()
    #Status de apontamento gravado no servidor da api do E-Soft
    enviou_esoft = models.IntegerField(default=1)
    #Nome da etapa
    nome_producao = models.CharField(max_length=255)

    class Meta:
        db_table = u'nap_produc_c'


'''
    Classe ApProducI
        Define os atributos dos itens de um apontamento.
'''
class ApProducI(models.Model):
    #Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    #Numero do apontamento
    num_apontamento = models.IntegerField(primary_key=True)
    #Codigo de barras do produto
    codbarra = models.CharField(primary_key=True, max_length=15)
	#Nome do produto
    nome_produto = models.CharField(max_length=255)
    #Quantidade do produto
    quantidade = models.DecimalField(max_digits=10, decimal_places=4)
    
    class Meta:
        db_table = u'nap_produc_i'


'''
    Classe CatMKPlace
        Define os atributos de uma categoria.
'''
class CatMKPlace(models.Model):
    # Código de registro
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    #Identificador da categoria
    id_categoria = models.AutoField(primary_key=True)
    # Nome da categoria
    nome_categoria = models.CharField(max_length=40)
    # Status de categoria que possui subcategorias ligadas a ela
    possui_subcategorias = models.CharField(max_length=1, default='N')
    # Recebe o id da categoria que é pai desta categoria
    id_pai = models.IntegerField(max_length=11, default=0)
    # Mostra a hierarquia das categorias, começando por zero seguido do id da categoria
    path = models.TextField(blank=True)
    # Status de categoria ativo (1 = ativo, 0 = inativo)
    ativo = models.IntegerField(default=1)
    # Lista de subcategorias (usado apenas para exibição dos dados)
    filhos = []

    class Meta:
        db_table = u'ncat_mkplace'


'''
    Classe CatLojaMKPlace
        Define os atributos referentes ao vinculo das lojas com categorias.
'''
class CatLojaMKPlace(models.Model):
    #Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    #Identificador da categoria
    id_categoria = models.IntegerField(primary_key=True, max_length=11)
    #Identificador da loja
    id_loja = models.IntegerField(primary_key=True, max_length=1)

    class Meta:
        db_table = u'ncat_loja_mkplace'


'''
    Classe ProdMkplace
        Define os atributos referentes ao vinculo dos produtos com marketplaces.
'''
class ProdMkplace(models.Model):
    # Codigo de registro do market place
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do produto
    id_produto = models.IntegerField(primary_key=True, max_length=11)
    # Identificador da loja, de acordo com a tabela de referencia 1.1
    id_loja = models.IntegerField(primary_key=True, max_length=1)
    # Identificador do produto na loja
    id_produto_loja = models.IntegerField(max_length=11)
    # Preco do produto na loja
    preco_loja = models.DecimalField(max_digits=10, decimal_places=4)
    # Preco da promocao na loja
    preco_promocao_loja = models.DecimalField(max_digits=10, decimal_places=4)
    # Identificador do fornecedor
    id_fornecedor = models.IntegerField(max_length=11)
    # Identificador da marca
    id_marca = models.IntegerField(max_length=11)

    class Meta:
        db_table = u'nprod_mkplace'


'''
    Classe ProdCatMkplace
        Define os atributos referentes ao vinculo das categorias de produtos com marketplaces.
'''
class ProdCatMkplace(models.Model):
    # Codigo de registro do market place
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do produto no market place
    id_produto = models.IntegerField(primary_key=True, max_length=11)
    # Identificador da loja
    id_loja = models.IntegerField(primary_key=True, max_length=1)
    # Identificador da categoria
    id_categoria = models.IntegerField(primary_key=True, max_length=11)

    class Meta:
        db_table = u'nprod_cat_mkplace'


'''
    Classe EncePed
        Define os atributos referentes aos dados de encerramento de um pedido
'''
class EncePed(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código da empresa
    codempresa = models.IntegerField()
    # Identificador do encerramento do pedido
    id_enceped = models.IntegerField()
    # Código do pedido
    cod_pedido = models.CharField(primary_key=True, max_length=8)
    # Origem da venda
    origem = models.CharField(max_length=50)
    # Data de encerramento da venda
    data_encerramento = models.DateTimeField()
    # Identificador do usuário que fez o encerramento
    id_usuario = models.IntegerField()
    # Código da operação (forma de pagamento)
    cod_operacao = models.CharField(primary_key=True, max_length=2)
    # Valor do pedido
    valor = models.DecimalField(max_digits=15, decimal_places=4)
    # Valor do troco do pedido
    #troco = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor do desconto do pedido
    #desconto = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Valor de acréscimo do pedido
    #acrescimo = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    # Campo com onformações adicionais, sejam de cheque, cartão, conta ou boleto
    informacoes_adicionais = models.TextField(default=None)
    # Status de pedido encerrado (0 pedido em aberto, 1 - pedido encerrado)
    pedido_encerrado = models.IntegerField(default=0)

    class Meta:
        db_table = u"nenceped"


class EncerramentoPedido():
    id


'''
    Classe LogMovimentacaoUsuario
        Define os atributos referentes aos dados de uma operação no sistema, relaizada por algum usuário
'''
class LogMovimentacaoUsuario(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Identificador do log de movimentação do usuário
    id_log_movimentacao = models.IntegerField()
    # Identificador do usuário
    id_usuario = models.IntegerField(primary_key=True)
    # Data do log de movimentação do usuário
    data_movimentacao = models.DateTimeField(primary_key=True)
    # Operação do log de movimentação do usuário
    operacao = models.CharField(primary_key=True, max_length=255)
    # Módulo onde foi feito o log de movimentação do usuário
    modulo = models.CharField(primary_key=True, max_length=255)
    # Tela onde foi feita o log de movimentação do usuário
    tela = models.CharField(primary_key=True, max_length=255)
    # Observação do log de movimentação do usuário
    observacao = models.TextField(default=None)

    class Meta:
        db_table = u"nlog_movimentacao_usuario"


'''
    Classe MagentoGruposAttr
        Define o os grupos de atributos da api magento
'''
class MagentoGruposAttr(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Id
    id_grupo_magento = models.IntegerField(max_length=11, primary_key=True)
    # Nome
    nome_grupo_magento = models.CharField(max_length=255)

    class Meta:
        db_table = u'nmagento_grupo_attr'


'''
    Classe MagentoCategoriaProd
        Define o as categorias de produtos da api magento
'''
class MagentoCategoriaProd(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Id
    id_categoria = models.IntegerField(max_length=11, primary_key=True)
    # Id pai
    id_pai = models.IntegerField(max_length=11)
    # Nome
    nome = models.CharField(max_length=100)
    # posicao
    posicao = models.IntegerField(max_length=11)
    # nivel
    nivel = models.IntegerField(max_length=11)
    # contador produto
    prod_contador = models.IntegerField(max_length=44)
    # ativo
    ativo = models.IntegerField(max_length=1, default=1)
    # Lista de subcategorias (usado apenas para exibição dos dados)
    filhos = []

    class Meta:
        db_table = u'nmagento_categoria_produto'


'''
    Classe MagentoGrupoAtributoProd
        Define a relação grupo com atributo
'''
class MagentoGrupoAtributoProd(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Id grupo
    id_grupo = models.IntegerField(primary_key=True, max_length=11)
    # Id atributo
    id_atributo = models.IntegerField(primary_key=True, max_length=11)
    # Valor
    valor = models.TextField(max_length=255)

    class Meta:
        db_table = u'nmagento_grupo_atributo'


'''
    Classe MagentoAtributo
        Define os atributos
'''
class MagentoAtributo(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Id atributo
    id_atributo = models.IntegerField(max_length=11, primary_key=True)
    # nome do atributo
    nome = models.CharField(max_length=100)
    # label
    label = models.CharField(max_length=100)
    # input frontend
    front_input = models.CharField(max_length=100)
    # tipo input backend
    back_input = models.CharField(max_length=100)
    # definido por user?
    user_defined = models.IntegerField(max_length=1)
    # valor
    options = models.TextField(max_length=255, default=None)
    # valor default
    valor_default = models.TextField(max_length=100)

    class Meta:
        db_table = u'nmagento_atributos'


'''
    Classe ConfigsPerfilUser
        Define o os campos da tabela de configuraçẽos de um perfil de usuário
'''
class ConfigsPerfilUser(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código da Sub-Empresa
    codempresa = models.IntegerField(primary_key=True, max_length=2)
    # Id configs perfil user
    id_configs_perfiluser = models.AutoField(max_length=25, primary_key=True)
    # ID do usuario
    id_perfiluser = models.IntegerField(max_length=11, primary_key=True)
    # empresa padrão
    empresa_default = models.CharField(max_length=100, default=0)

    class Meta:
        db_table = u'nconfigs_perfiluser'


'''
    Classe ConfigsUsuario
        Define o os campos da tabela de configuraçẽos de um usuário
'''
class ConfigsUsuario(models.Model):
    # Codigo de registro da empresa
    codregistro = models.IntegerField(primary_key=True, max_length=25)
    # Código da Sub-Empresa
    codempresa = models.IntegerField(primary_key=True, max_length=2)
    # Id configs perfil user
    id_configs_usuario = models.AutoField(max_length=25, primary_key=True)
    # ID do usuario
    id_usuario = models.IntegerField(max_length=11, primary_key=True)
    # empresa padrão
    empresa_default = models.CharField(max_length=100, default=0)
    # ativo
    ativo = models.IntegerField(max_length=1, default=1)

    class Meta:
        db_table = u'nconfigs_usuario'


'''
    Classe AppBase
        Define o os campos da tabela de configuraçẽos de um usuário
'''

class AppBase(models.Model):
    # Codigo de Registro da Empresa
    codregistro = models.IntegerField(max_length=25, primary_key=True)
    # ID do Aplicativo Base
    id_appbase = models.IntegerField(max_length=11, primary_key=True)
    # Nome do Aplicativo Base
    nome_appbase = models.CharField(max_length=100)
    # Status do Aplicativo Base
    ativo = models.IntegerField(default=0)

    class Meta:
        db_table = u'napp_base'


'''
    Classe ConfigsUsuario
        Define o os campos da tabela de configuraçẽos de um usuário
'''

class AppBaseUi(models.Model):
    # Codigo de Registro da Empresa
    codregistro = models.IntegerField(max_length=25, primary_key=True)
    # ID do Aplicativo Base
    id_appbase = models.IntegerField(max_length=11, primary_key=True)
    # ID do Atributo
    id_atributo = models.IntegerField(max_length=25, primary_key=True)
    # Nome do Atributo
    nome_atributo = models.CharField(max_length=50)
    # Valor do Atributo
    valor_atributo = models.CharField(max_length=100)
    # Status do Aplicativo Base
    ativo = models.IntegerField(default=0)

    class Meta:
        db_table = u'napp_base_ui'

# Testes
class tabela_opcionais_testes(models.Model):
    codregistro = models.IntegerField(max_length=25, primary_key=True)
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=255)
    unidade = models.IntegerField(max_length=11, default=0)
    ativo = models.IntegerField(max_length=11, default=0)
    observacao = models.TextField()

    class Meta:
        db_table = u'tabela_opcionais_testes'
