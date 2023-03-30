from operacoesbd import *


def menu():
    print()
    print("1) Listar ocorrências: ")
    print("2) Adicionar nova ocorrência: ")
    print("3) Pesquisar pelo código da ocorrência: ")
    print("4) Remover ocorrências: ")
    print("5) Sair: ")
    opcao = int(input('Digite sua opção: '))
    return opcao

def listaTodasOcorrencias(conexao):

    print('OUVIDORIA FACISA | OCORRÊNCIAS:')
    print()

    consultaListagemOcorrencias = 'select * from ouvidoriafacisa'
    listaTodasOcorrencias = listarBancoDados(conexao, consultaListagemOcorrencias)

    for i in listaTodasOcorrencias:
        print('-CÓDIGO DA Ocorrência:', i[0])
        print('-', i[1], ':', i[2])
        print()
        if len(listaTodasOcorrencias) == 0:
                print('Não existem reclamações a serem exibido.')

def listaTodosElogios(conexao):
    elogio = 'elogio'
    consultaOcorrenciaElogio = 'select * from ouvidoriafacisa where tipo =' + elogio
    listaTodosElogios= listarBancoDados(conexao, consultaOcorrenciaElogio)

    for i in listaTodosElogios(conexao):
        if len(listaTodosElogios) == 0:
            print('Não existem elogios a serem exibido.')
        else:
            for elogio in listaTodosElogios:
                print('-Código da Ocorrência:', elogio[0])
                print('-', elogio[1], ':', elogio[2])
                print()


def listaTodasReclamacoes(conexao):
    reclamacao = 'reclamação'
    consultaListagemReclamacoes = 'select * from ouvidoriafacisa where tipo = ' + reclamacao
    listaTodasReclamacoes = listarBancoDados(conexao, consultaListagemReclamacoes)

    for reclamacao in listaTodasReclamacoes():
        print('-CÓDIGO DA Ocorrência:', reclamacao[0])
        print('-', reclamacao[1], ':', reclamacao[2])
        print()


def novaReclamacao(conexao):

    opcao = 3
    while opcao != 4:
        print(" Digite (elogio) para elogio.")
        print(" Digite (reclamação) para reclamação.")
        print()
        tipoOcorrencia = input("Qual o tipo da sua ocorrência: ")
        if tipoOcorrencia == 'elogio' or tipoOcorrencia == 'reclamação' :
            novaOcorrencia = input('Digite suas Informações: ')

            consultaNovaReclamacao = 'insert into ouvidoriafacisa(tipo, descrição_ocorrências)values(%s,%s)'
            dados = (tipoOcorrencia,novaOcorrencia)
            insertNoBancoDados(conexao, consultaNovaReclamacao, dados)
            break
        else:
            print('Não existe esse tipo de ocorrência.')


def pesquisarOcorrenciaPeloCodigo(conexao):
    consultaListagemOcorrencias = 'select * from ouvidoriafacisa'
    listaTodasOcorrencias = listarBancoDados(conexao, consultaListagemOcorrencias)

    for i in listaTodasOcorrencias:
        print('-CÓDIGO DA Ocorrência:', i[0])
        print('-', i[1], ':', i[0])
        print()

    print("|PESQUISE PELO CODIGO| ")
    codigo = input('digite o codigo:')
    print()
    consultaReclamacaoCodigo = 'select * from ouvidoriafacisa where codigo_ocorrências=' + codigo
    listaOcorrencias = listarBancoDados(conexao, consultaReclamacaoCodigo)

    for i in listaOcorrencias:
        if len(listaOcorrencias) == 0:
            print('Não existem reclamações a serem exibido.')
        else:
            for i in listaOcorrencias:
                print('-CÓDIGO DA RECLAMAÇÃO:', i[0])
                print('-',i[1],':', i[2])
                print()

def removerReclamacao(conexao):
    opcao = 4
    while opcao != 3:
        print(" Digite (1) Remover ocorrência pelo código.")
        print(" Digite (2) Remover todas ocorrência.")
        print(" Digite (3) Sair.")
        opcao = int(input("Digite sua opção:"))

        if opcao == 1 :
            codigo =  int(input('Digite o codigo da reclamação a ser removido: '))
            consultaRemoverOcorrenciaCodigo = 'delete from ouvidoriafacisa where codigo_ocorrências = %s '
            dados = (codigo,)
            excluirBancoDados(conexao, consultaRemoverOcorrenciaCodigo, dados)
            break

        elif opcao == 2:
            consultaRemoverReclamacao = ' delete from ouvidoriafacisa; '
            excluirBancoDados(conexao, consultaRemoverReclamacao)
            break

        elif opcao  <= 0 or opcao > 3:
            print("Não existe essa opção. ")

