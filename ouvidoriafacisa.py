from metodosouvidoria import *

conexao = abrirBancoDados('localhost','root', '12345', 'bdouvidoria')

opcao = 6

while opcao != 5:
    opcao = menu()

    if opcao == 1:
        opcao = 5
        while opcao != 4:
            print(" Digite (1) Listar todas ocorrências.")
            print(" Digite (2) Listar todos elogios.")
            print(" Digite (3) Listar todos reclamações.")
            print(" Digite (4) Sair.")

            opcaoListar = int(input("Digite sua opção:"))

            if opcaoListar == 1:
                listaTodasOcorrencias(conexao)

            elif opcaoListar == 2 :
                listaTodosElogios(conexao)

            elif opcaoListar == 3:
                listaTodasReclamacoes(conexao)

            elif opcaoListar <= 0 or opcao > 4:
                print()
                print("Não existe essa opção.")
                print()

    elif opcao == 2:
        novaReclamacao(conexao)
        print("-Adicionado com sucesso!")
    elif opcao == 3:
        pesquisarOcorrenciaPeloCodigo(conexao)

    elif opcao == 4:
        removerReclamacao(conexao)


    elif opcao == 5:
        break

    elif opcao <= 0 or opcao > 5:
        print("Não existe essa opção")


print('Obrigado, volte sempre!!')
encerrarBancoDados(conexao)