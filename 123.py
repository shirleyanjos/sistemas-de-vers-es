import sqlite3

BD = 'SJKI'

print('#' * 35)
print('#        MENU - SOFTWARE          #')
print('#' * 35)
print('# 1 - Cadastrar software          #')
print('# 2 - Buscar por id               #')
print('# 3 - Buscar por data do cadastro #')
print('# 4 - Listar Softwares            #')
print('# 5 - Buscar por descrição        #')
print('# 6 - Buscar por nome             #')
print('# 7 - Excluir Software            #')
print('# 8 - Sair                        #')
print('#' * 35)


def cadastrar_software(nome, descricao, data_cadastro):
    ''''Cadastrar um software'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "INSERT INTO software (nome,descricao,data_cadastro) VALUES ('%s', '%s','%s')" % (
    nome, descricao, data_cadastro)
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print('Produto ', nome, ' cadastrado')
    else:
        conexao.rollback()
        print('Não foi possível cadastrar o software')
    cursor.close()
    conexao.close()


def buscar_software_id(id_software):
    ''''Buscar os softwares por id'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM software WHERE id_software='%d'" % id_software
    cursor.execute(sql)
    software = cursor.fetchone()
    # print(software)
    if software:
        print('id_software: ', software[0], ' //-// nome: ', software[1], ' //-// data_cadastro: ', software[3] )
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
        print('id_software: ', software[0], ' //-// nome: ', software[1], ' //-// data_cadastro: ', software[3])
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
            print(('Id_software: ', software[0], ' //-// nome: ', software[1],
            ' //-// descricao: ', software[2], ' //-// data_cadastro: ', software[3]))
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
            print('Id_software: ', software[0], ' //-// nome: ', software[1],
                  ' //-// descricao: ', software[2], ' //-// data_cadastro: ', software[3] )
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
            print('Id_software: ', software[0], ' //-// nome: ', software[1],
                   ' //-// data_cadastro: ', software[3] )
        return True
    else:
        print('Nenhum nome encontrado')
        return False
    cursor.close()
    conexao.close()


def excluir_por_id(id_software):
    '''Exclui o software por id'''
    if buscar_software_id(id_software):
        resposta = input('Deseja realmente exlcuir este software ?(s/n)').lower()
        if resposta == 's':
            conexao = sqlite3.connect(BD)
            cursor = conexao.cursor()
            sql = "DELETE FROM software WHERE id_software='%d'" % (id_software)
            cursor.execute(sql)
            if cursor.rowcount == 1:
                conexao.commit()
                print('software deletado!')
            else:
                conexao.rollback()
                print('Não foi possível deletar o software!')


op = 0
while op != 8:

    op = int(input('Opção: '))
    if op == 1:
        nome = input('Informe o nome do software: ')
        descricao = input('Informe a descrição do software: ')
        data_cadastro = input('Informe a data do cadastro do software:')

        lista_data = data_cadastro.split('-')
        lista_data.reverse()
        data_cadastro = "-".join(lista_data)

        cadastrar_software(nome, descricao, data_cadastro)

    if op == 2:
        id_software = int(input('Digite o id: '))
        buscar_software_id(id_software)

    if op == 3:
        data_cadastro = input('Informe a data de cadastro do software: ')

        lista_data = data_cadastro.split('-')
        lista_data.reverse()
        data_cadastro = "-".join(lista_data)

        buscar_software_data(data_cadastro)

    if op == 4:
        listar_software()

    if op == 5:
        descricao = input('Informe a descrição do software: ')
        buscar_descricao_software(descricao)

    if op == 6:
        nome = input('Informe um nome: ')
        buscar_nome_software(nome)

    if op == 7:
        id_software = int(input('Informe o id que deseja excluir: '))
        excluir_por_id(id_software)

    if op == 8:
        print('Você saiu do inferno !!!!! Uuurrrruuulllllllll')
        break

else:
    print("Opção invalida!")