import sqlite3

BD = 'SJKI'

print('#' * 44)
print('#        MENU - VERSÔES                    #')
print('#' * 44)
print('# 9 - Cadastrar versao do software         #')
print('# 10 - Buscar ID da versao                 #')
print('# 11 - Buscar versao do software pelo nome #')
print('# 12 - Buscar por data de lançamento       #')
print('# 13 - Buscar por versoes Beta             #')
print('# 14 - Buscar por versoes Alfa             #')
print('# 15 - Excluir versao do Software          #')
print('# 16 - Listar versoes                      #')
print('# 17 - Sair                                #')
print('#' * 44)


def cadastrar_versao(nome, id_software, informacoes, data_lancamento, alfa, beta):
    '''Cadastrar as versoes dos softwares'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = ("INSERT INTO versoes (nome, id_software, informacoes, data_lancamento, alfa, beta) "
           "VALUES ('%s', '%d', '%s', '%s', '%s', '%s')"
           % (nome, id_software, informacoes, data_lancamento, alfa, beta))
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print('Versao ', nome, ' cadastrada')
    else:
        conexao.rollback()
        print('Não foi possível cadastrar a versao')
    cursor.close()
    conexao.close()


def buscar_versoes_id(id_versao):
    ''''Buscar versoes dos softwares por id'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM versoes WHERE id_versao='%d'" % id_versao
    cursor.execute(sql)
    versao = cursor.fetchone()
    # print(versao)
    if versao:
        print('id_versao: ', versao[0], ' //-// nome_versao: ', versao[2],
              ' //-// data_lancamento: ', versao[4], ' //-// alfa: ', versao[5], ' //-// beta: ', versao[6])
        return True
    else:
        print('id não encontrado')
        return False
    cursor.close()
    conexao.close()


def buscar_nome_versao(nome):
    ''''Buscar por nome das versoes dos softweares'''
    nome = nome + '%'
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM versoes WHERE nome LIKE '%s'" % nome
    cursor.execute(sql)
    versoes = cursor.fetchall()
    if versoes:
        for versao in versoes:
            print('id_versao: ', versao[0], ' //-// nome_versao: ', versao[2],
                  ' //-// data_lancamento: ', versao[4], ' //-// alfa: ', versao[5], ' //-// beta: ', versao[6])
        return True
    else:
        print('Nome nâo encontrado')
        return False
    cursor.close()
    conexao.close()


def buscar_versao_data_lancamento(data_lancamento):
    ''''Buscar versoes dos softweres por data'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM versoes WHERE data_lancamento='%s'" % data_lancamento
    cursor.execute(sql)
    versao = cursor.fetchone()
    # print(versao)
    if versao:
        print('id_versao: ', versao[0], ' //-// nome_versao: ', versao[2],
              ' //-// data_lancamento: ', versao[4], ' //-// alfa: ', versao[5], ' //-// beta: ', versao[6])
        return True
    else:
        print('Data lancamento não encontrado')
        return False
    cursor.close()
    conexao.close()


def buscar_versao_beta():
    ''''Buscar versoes beta dos softwares '''

    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM versoes WHERE beta = 'true'"
    cursor.execute(sql)
    versoes = cursor.fetchall()
    if versoes:
        for versao in versoes:
            print('id_versao: ', versao[0], ' //-// nome_versao: ', versao[2],
                  ' //-// data_lancamento: ', versao[4], ' //-// beta: ', versao[6])
        return True
    else:
        print('Não ha versoes beta')
        return False
    cursor.close()
    conexao.close()


def buscar_versao_alfa():
    ''''Buscar versoes alfa dos softwares '''

    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM versoes WHERE alfa = 'true'"
    cursor.execute(sql)
    versoes = cursor.fetchall()
    if versoes:
        for versao in versoes:
            print('id_versao: ', versao[0], ' //-// nome_versao: ', versao[2],
                  ' //-// data_lancamento: ', versao[4], ' //-// alfa: ', versao[5])
        return True
    else:
        print('Não ha versoes alfa')
        return False
    cursor.close()
    conexao.close()


def excluir_por_id(id_versao):
    ''''Exclui o software por id'''
    if buscar_versoes_id(id_versao):
        resposta = input('Deseja realmente exlcuir esta versao ?(s/n)').lower()
        if resposta == 's':
            conexao = sqlite3.connect(BD)
            cursor = conexao.cursor()
            sql = "DELETE FROM versoes WHERE id_versao='%d'" % (id_versao)
            cursor.execute(sql)
            if cursor.rowcount == 1:
                conexao.commit()
                print('Versao deletada!')
            else:
                conexao.rollback()
                print('Não foi possível deletar esta versao!')


def listar_versoes():
    ''''Lista todas as versoes cadastradas'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM versoes"
    cursor.execute(sql)
    versoes = cursor.fetchall()
    if versoes:
        for versao in versoes:
            print('id_versao: ', versao[0], 'id_software: ', versao[1], ' //-// nome_versao: ', versao[2],
                  '//-// informacoes: ', versao[3], ' //-// data_lancamento: ', versao[4], 'alfa: ', versao[5],
                  ' //-// beta: ', versao[6])
    else:
        print('Nenhuma versão encontrada!')
    cursor.close()
    conexao.close()


op = 0
while op != 17:

    op = int(input('Opção: '))
    if op == 9:
        nome = input('Informe o nome da versao do software: ')
        # id_versao = int(input('Informe o id da versao do software: '))
        id_software = int(input('Informe o id do software: '))
        informacoes = input('Digite informacoes da versao: ')
        data_lancamento = input('Informe a data do lancamento da versao:')
        alfa = input('Informe se a versao é alfa: ')
        beta = input('Informe se a versao é beta: ')

        cadastrar_versao(nome, id_software, informacoes, data_lancamento, alfa, beta)

    if op == 10:
        id_versao = int(input('Digite o id: '))
        buscar_versoes_id(id_versao)

    if op == 11:
        nome = input('Informe um nome: ')
        buscar_nome_versao(nome)

    if op == 12:
        data_lancamento = input('Informe a data de lancamento da versao: ')
        buscar_versao_data_lancamento(data_lancamento)

    if op == 13:
        buscar_versao_beta()

    if op == 14:
        buscar_versao_alfa()

    if op == 15:
        id_versao = int(input('Informe o id que deseja excluir: '))
        excluir_por_id(id_versao)

    if op == 16:
        listar_versoes()

    if op == 17:
        print('Você saiu do inferno !!!!! Uuurrrruuulllllllll')
        break

else:
    print("Opção invalida!")
