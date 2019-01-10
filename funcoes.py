'''importando o banco de dados do sqlite3'''
import sqlite3
BD = 'SJKI'

#Cadastrar um software
def cadastrar_software(nome, descricao, data_cadastro):
    #faz a conexão do  sqlite3 com o banco de dados
    conexao = sqlite3.connect(BD)
    #
    cursor = conexao.cursor()
    sql = "INSERT INTO software (nome,descricao,data_cadastro) VALUES ('%s', '%s','%s')" % (
        nome, descricao, data_cadastro)
    cursor.execute(sql)
    if cursor.rowcount != 1:
        conexao.rollback()
        print('Não foi possível cadastrar o software')

    else:
        conexao.commit()
        print('Produto ', nome, ' cadastrado')
    cursor.close()
    conexao.close()


def buscar_software_id(id_software):
    ''''Busca um software por id'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM software WHERE id_software='%s'" % id_software
    cursor.execute(sql)
    software = cursor.fetchone()
    # print(software)
    #se o id for encontrado, retorna o print
    if software:
        print('id_software: ', software[0], ' --- nome: ', software[1], ' --- data_cadastro: ', software[3])
        return True
    else:
        print('id não encontrado')
        return False
    cursor.close()
    conexao.close()


def buscar_software_data(data_cadastro):
    ''''Buscar os softweres por data'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM software WHERE data_cadastro='%s'" % data_cadastro
    cursor.execute(sql)
    software = cursor.fetchone()
    print(software)
    if software:
        print('id_software: ', software[0], ' --- nome: ', software[1], ' --- data_cadastro: ', software[3])
        return True
    else:
        print('Data não encontrada')
        return False
    cursor.close()
    conexao.close()


def listar_software():
    '''Lista todos os softwares cadastrados'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM software"
    cursor.execute(sql)
    softwares = cursor.fetchall()
    if softwares:
        for software in softwares:
            print('Id_software: ', software[0], ' --- nome: ', software[1],
                   ' --- descricao: ', software[2], ' --- data_cadastro: ', software[3])
    else:
        print('Nenhum produto cadastrado!')
    cursor.close()
    conexao.close()


def buscar_descricao_software(descricao):
    ''''Buscar a descrição dos software'''
    descricao = descricao + '%'
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM software WHERE descricao LIKE '%s'" % descricao
    cursor.execute(sql)
    software = cursor.fetchall()
    if software:
        for software in software:
            print('Id_software: ', software[0], ' --- nome: ', software[1],
                  ' --- descricao: ', software[2], ' --- data_cadastro: ', software[3])
        return True
    else:
        print('Nenhuma descrição encontrada')
        return False
    cursor.close()
    conexao.close()


def buscar_nome_software(nome):
    ''''Buscar por nome os softwares'''
    nome = nome + '%'
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM software WHERE nome LIKE '%s'" % nome
    cursor.execute(sql)
    softwares = cursor.fetchall()
    if softwares:
        for software in softwares:
            print('Id_software: ', software[0], ' --- nome: ', software[1],
                  ' --- data_cadastro: ', software[3])
        return True
    else:
        print('Nenhum nome encontrado')
        return False
    cursor.close()
    conexao.close()


def excluir_por_id(id_software):
    '''Exclui o software por id'''
    if buscar_software_id(id_software):
        resposta = input('Deseja realmente exlcuir este software?(s/n)').lower()
        if resposta == 's':
            conexao = sqlite3.connect(BD)
            cursor = conexao.cursor()
            sql = "DELETE FROM software WHERE id_software='%s'" % (id_software)
            cursor.execute(sql)
            if cursor.rowcount == 1:
                conexao.commit()
                print('software deletado!')
            else:
                conexao.rollback()
                print('Não foi possível deletar o software!')


#apartir daqui tabela versoes
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
        print('id_versao: ', versao[0], ' --- nome_versao: ', versao[2],
              ' --- data_lancamento: ', versao[4], ' --- alfa: ', versao[5], ' --- beta: ', versao[6])
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
            print('id_versao: ', versao[0], ' --- nome_versao: ', versao[2],
                  ' --- data_lancamento: ', versao[4], ' --- alfa: ', versao[5], ' --- beta: ', versao[6])
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
        print('id_versao: ', versao[0], ' --- nome_versao: ', versao[2],
              ' --- data_lancamento: ', versao[4], ' --- alfa: ', versao[5], ' --- beta: ', versao[6])
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
            print('id_versao: ', versao[0], ' --- nome_versao: ', versao[2],
                  ' --- data_lancamento: ', versao[4], ' --- beta: ', versao[6])
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
            print('id_versao: ', versao[0], ' --- nome_versao: ', versao[2],
                  ' --- data_lancamento: ', versao[4], ' --- alfa: ', versao[5])
        return True
    else:
        print('Não ha versoes alfa')
        return False
    cursor.close()
    conexao.close()


def excluir_por_id_versao(id_versao):
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
            print('id_versao: ', versao[0], '--- id_software: ', versao[1], ' --- nome_versao: ', versao[2],
                  '--- informacoes: ', versao[3], ' --- data_lancamento: ', versao[4], 'alfa: ', versao[5],
                  ' --- beta: ', versao[6])
    else:
        print('Nenhuma versão encontrada!')
    cursor.close()
    conexao.close()


def buscar_versoes_software(id_software):
    ''''Buscar versoes dos softwares por id'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM versoes WHERE id_software='%s'" % id_software
    cursor.execute(sql)
    versoes = cursor.fetchall()
    # print(versao)

    if versoes:
        for versoes in versoes:
            print('id_versao: ', versoes[0], '--- id_software: ', versoes[1], ' --- nome_versao: ', versoes[2],
              '--- informacoes: ', versoes[3], ' --- data_lancamento: ', versoes[4], 'alfa: ', versoes[5],
              ' --- beta: ', versoes[6])
    else:
        print('id não encontrado')
    cursor.close()
    conexao.close()