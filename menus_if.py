from funcoes import *

print('#' * 90)
print('#        MENU - SOFTWARE            ####          MENU - VERSÔES                         #')
print('#' * 90)
print('# 1 - Cadastrar software            ###  8 - Cadastrar versao do software                #')
print('# 2 - Buscar por id                 ###  9 - Buscar ID da versao                         #')
print('# 3 - Buscar por data do cadastro   ###  10 - Buscar versao do software pelo nome        #')
print('# 4 - Listar Softwares              ###  11 - Buscar por data de lançamento              #')
print('# 5 - Buscar por descrição          ###  12 - Buscar por versoes Beta                    #')
print('# 6 - Buscar por nome               ###  13 - Buscar  por versoes Alfa                   #')
print('# 7 - Excluir Software              ###  14 - Excluir versao do Software                 #')
print('#                                   ###  15 - Listar versoes                             #')
print('#                                   ###  16 - buscar versoes de um determinado software  #')
print('#                                   ###  17 - Sair                                       #')
print('#' * 90)


op = 0
while True:

    op = int(input('Opção: '))
    if op == 1:
        nome = input('Informe o nome do software: ')
        descricao = input('Informe a descrição do software: ')
        data_cadastro = input('Informe a data do cadastro do software:')

        #lista_data = data_cadastro.split('-')
        #lista_data.reverse()
        #data_cadastro = "-".join(lista_data)

        cadastrar_software(nome, descricao, data_cadastro)

    elif op == 2:
        id_software = int(input('Digite o id: '))
        buscar_software_id(id_software)

    elif op == 3:
        data_cadastro = input('Informe a data de cadastro do software: ')

        #lista_data = data_cadastro.split('-')
        #'''lista_data.reverse()'''
        #data_cadastro = "-".join(lista_data)

        buscar_software_data(data_cadastro)

    elif op == 4:                      
        listar_software()

    elif op == 5:
        descricao = input('Informe a descrição do software: ')
        buscar_descricao_software(descricao)

    elif op == 6:
        nome = input('Informe um nome: ')
        buscar_nome_software(nome)

    elif op == 7:
        id_software = int(input('Informe o id que deseja excluir: '))
        excluir_por_id(id_software)


    #Apartir daqui  tabela versoes

    elif op == 8:
        nome = input('Informe o nome da versao do software: ')
        # id_versao = int(input('Informe o id da versao do software: '))
        id_software = int(input('Informe o id do software: '))
        informacoes = input('Digite informacoes da versao: ')
        data_lancamento = input('Informe a data do lancamento da versao:')
        alfa = input('Informe se a versao é alfa: ')
        beta = input('Informe se a versao é beta: ')

        cadastrar_versao(nome, id_software, informacoes, data_lancamento, alfa, beta)

    elif op == 9:
        id_versao = int(input('Digite o id: '))
        buscar_versoes_id(id_versao)

    elif op == 10:
        nome = input('Informe um nome: ')
        buscar_nome_versao(nome)

    elif op == 11:
        data_lancamento = input('Informe a data de lancamento da versao: ')
        buscar_versao_data_lancamento(data_lancamento)

    elif op == 12:
        buscar_versao_beta()

    elif op == 13:
        buscar_versao_alfa()

    elif op == 14:
        id_versao = int(input('Informe o id que deseja excluir: '))
        excluir_por_id_versao(id_versao)

    elif op == 15:
        listar_versoes()

    elif op == 16:
        id_software = input('Informe o id do software: ')
        buscar_versoes_software(id_software)

    elif op == 17:
        print('Você saiu do sistema!')
        break ; exit()

    else:
        print("Opção invalida!")
