# Rozendoxxxxxxxxxxxxxxxxxxxx
"""
MIT License

Copyright (c) [2023] [CARLOS GABRIEL ROZENDO GUIMARAES TAVARES]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Copyright (c) [2023] [CARLOS GABRIEL ROZENDO GUIMARAES TAVARES]

A permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia
deste software e arquivos de documentação associados (o "Software"), para lidar
no Software sem restrições, incluindo, sem limitação, os direitos
usar, copiar, modificar, fundir, publicar, distribuir, sublicenciar e/ou vender
cópias do Software e para permitir que as pessoas a quem o Software é
munidos para o efeito, nas seguintes condições:

O aviso de direitos autorais acima e este aviso de permissão devem ser incluídos em todos os
cópias ou partes substanciais do Software.

O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU
IMPLÍCITAS, INCLUINDO, SEM LIMITAÇÃO, AS GARANTIAS DE COMERCIALIZAÇÃO,
ADEQUAÇÃO PARA UM FIM ESPECÍFICO E NÃO VIOLAÇÃO. EM NENHUM CASO O
OS AUTORES OU DETENTORES DOS DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER REIVINDICAÇÃO, DANOS OU OUTROS
RESPONSABILIDADE, SEJA EM UMA AÇÃO DE CONTRATO, ILÍCITO OU DE OUTRA FORMA, DECORRENTE DE,
FORA DE OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTROS NEGÓCIOS NO
PROGRAMAS.

Авторское право (с) [2023] [CARLOS GABRIEL ROZENDO GUIMARAES TAVARES]

Настоящим предоставляется бесплатное разрешение любому лицу, получившему копию
данного программного обеспечения и связанных с ним файлов документации ("Программное обеспечение"), для
в Программном обеспечении без ограничений, включая, помимо прочего, права
использовать, копировать, изменять, объединять, публиковать, распространять, сублицензировать и/или продавать
копий Программного обеспечения, а также разрешить лицам, которым Программное обеспечение
предоставляется для этого при соблюдении следующих условий:

Вышеприведенное уведомление об авторских правах и это уведомление о разрешении должны быть включены во все
копии или существенные части Программного обеспечения.

ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ, ЯВНЫХ ИЛИ
ПОДРАЗУМЕВАЕТСЯ, ВКЛЮЧАЯ, ПОМИМО ПРОЧЕГО, ГАРАНТИИ КОММЕРЧЕСКОЙ ЦЕННОСТИ,
ПРИГОДНОСТЬ ДЛЯ ОПРЕДЕЛЕННОЙ ЦЕЛИ И НЕНАРУШЕНИЕ ПРАВ. НИ ПРИ КАКИХ ОБСТОЯТЕЛЬСТВАХ
АВТОРЫ ИЛИ ВЛАДЕЛЕЦ АВТОРСКИХ ПРАВ НЕСУТ ОТВЕТСТВЕННОСТЬ ЗА ЛЮБЫЕ ПРЕТЕНЗИИ, УЩЕРБ ИЛИ ДРУГОЕ.
ОТВЕТСТВЕННОСТЬ, БУДУЩАЯ ПО ДОГОВОРУ, ДЕЛИКТУ ИЛИ ИНЫМ ОБРАЗОМ, ВОЗНИКАЮЩАЯ ИЗ,
ВНЕ ИЛИ В СВЯЗИ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ ИЛИ ИСПОЛЬЗОВАНИЕМ ИЛИ ДРУГИМИ СДЕЛКАМИ В
ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ.

# -----------------------------------------------------------------
# ---------------------- PROPOSTA DO PROJETO ----------------------
# -----------------------------------------------------------------
    O projeto foi criado com o intuito de organizar horarios em dias de semana de segunda a sábado.
    Após inicar o projeto com a seguinte imagem: https://postlmg.cc/DSxnwNjK



# -----------------------------------------------------------------
# ---------------AREA DE ERROS, PROBLEMAS E SOLUÇÕES---------------
# -----------------------------------------------------------------

    # FIXME: PROBLEMAS ATUAIS:

        FIXME: $$$ ARRUMAR URGENTEMENTE $$$:
            --
            NOTA ESTÁ REFERENCIANDO NOTA
                fixed. 11/04/23
                    IMPLEMENTED: mudança no código, criação de nota através de constraint's
                                 Ao criar tabelas o usuario escolhe qual tabela referenciar a nota
                                 SEGUNDA À SABADO


            NOTA NÃO ESTÁ FUNCIONANDO A CRIAÇÃO--
                fixed. 11/04/23
            CRIAR TABELAS NÃO ESTÁ FUNCIONANDO--

            QUANDO PUXO PARA VER A AGENDA NÃO RETORNA, E DÁ ERRO--
                fixed. 07/04/23
            DUAS TABELAS ESTÃO COM A TIPAGEM ERRADA--
                fixed. 10/04/23
            CODIGO DE MUDANÇA DE TIPO DA COLUNA GERANDO ERRO NA SINTAXE --(NEAR TO MODIFY)--

            TABELA CRIAÇÃO DE NOTA FOI FEITA, MAS NÃO EXISTE A TABELA INSERÇÃO DE CONTEÚDO--

                # fixme: Possível solução:
                    a criação pode ser feita através de um menu de escolha depois de criar a tabela desejada
                    ou através do laço de repetição




# -----------------------------------------------------------------
# ----------- RESPOSTA DO CHAT GPT EM RELAÇÃO AO CODIGO -----------
# -----------------------------------------------------------------




    # FIXME: == RESPOSTA DO CHAT GPT SOBRE PROBLEMAS EM CIMA DO CÓDIGO ATUAL==

    Existem alguns problemas de segurança no código que devem ser abordados:

        O código usa diretamente as entradas do usuário em consultas SQL sem sanitização adequada.
        Isso pode permitir ataques de injeção de SQL.
        É importance usar consultas preparadas ou escapar as entradas do usuário para evitar esses problemas.


        O código usa uma senha padrão para o banco de dados. Isso é um risco de segurança.
        A senha deve ser forte e exclusiva para o banco de dados em questão.

        O código não faz nenhuma verificação de autenticação para as operações de edição e exclusão de contatos.
        Isso significa que qualquer pessoa que acesse a página pode editar ou excluir qualquer contato.
        É importante implementar autenticação adequada para
        garantir que apenas usuários autorizados possam realizar essas operações.

        O código usa uma conexão global com o banco de dados, o que pode ser um problema de desempenho e segurança.
        É importante usar uma conexão por solicitação e garantir que a conexão
        seja fechada corretamente após cada solicitação.

        Além disso, algumas práticas recomendadas de codificação não são seguidas,
        como o uso de nomes de variáveis descritivos e o comentário adequado do código.
        É importante seguir essas práticas para tornar o código mais legível e fácil de manter.

    # FIXME: == AREA DE PROPOSTAS DO CHAT GPT ==

        1.Use consultas preparadas ou escape as entradas do usuário ao criar consultas SQL.
        Isso ajudará a evitar ataques de injeção de SQL.

        2.Armazene as senhas dos usuários de maneira segura, usando funções de hash seguras, como bcrypt.

        3.Use uma senha forte e exclusiva para o banco de dados.

        4.Implemente autenticação adequada para garantir que apenas usuários autorizados possam editar ou excluir
        contatos.
            Criar um formulário de login: Crie uma página de login para que os usuários possam se
            autenticar com nome de usuário e senha.
            O formulário deve ser seguro e protegido contra ataques de injeção de SQL e outros tipos de ataques.

            Verificar as credenciais do usuário: Quando um usuário enviar o formulário de login,
            você deve verificar as credenciais do usuário no banco de dados.
            Você pode fazer isso comparando o nome de usuário e a senha fornecidos pelo usuário com as
            informações de nome de usuário e senha armazenadas no banco de dados.

            Armazenar informações de autenticação: Depois que um usuário for autenticado com sucesso,
            você pode armazenar informações de autenticação em uma sessão ou cookie para que o
            usuário não precise inserir suas credenciais novamente em cada página.
            Certifique-se de que as informações de autenticação sejam armazenadas com segurança e não possam ser
            acessadas por usuários não autorizados.

            Proteger as páginas de edição e exclusão de contatos: Em suas páginas de edição e exclusão de contatos,
            verifique se o usuário está autenticado antes de permitir que ele acesse a página.
            Você pode fazer isso verificando se as informações de autenticação estão presentes na sessão ou cookie.

            Limitar o acesso do usuário: Se você tiver vários usuários com diferentes níveis de acesso,
            deverá limitar o acesso do usuário às páginas de edição e exclusão de contatos
            com base em suas permissões de usuário. Isso pode ser feito armazenando informações de permissão
            no banco de dados ou em um arquivo de
            configuração e verificando essas informações quando o usuário tenta acessar uma página.


        5.Use uma conexão por solicitação e feche a conexão corretamente após cada solicitação.


        6.Implementar no código uma api para envio de mensagem no what's

        7.Pra isso funcioar precisamos instanciar o codigo dentro de um servidor (PODE SER tecnologia CONTAINER ou
        DOCKER)

        8.CRIAÇÃO DE NOTAS DE REFERENCIAS FIXAS ATRAVÉS DE WHILE LOOP
            COMO SERÁ O FUNCIONAMENTO DISSO:
                O CODIGO IRÁ PEDIR O NOME DA TABELA,

                                create table table_name
                (
                    ID       integer not null
                        constraint table_name_pk
                            primary key autoincrement
                        constraint table_name_SEGUNDA_id_fk
                            references SEGUNDA,
                    Titulo   text    not null,
                    conteudo text    not null
                );

        9.CRIAÇÃO DE NOTA REFERENCIA SOMENTE TABELAS EXISTENTES- CRIAR CODIGO QUE REFERENCIE TABELAS N EXISTENTES







     FIXME: == QUAIS TIPOS DE DADOS ESTE BANCO DE DADOS POSSUI ==

        -DML
            FUNÇÕES NESTE CODIGO QUE REALIZAM ESTA OPERAÇÃO:

        -DDL
            FUNÇÕES NESTE CODIGO QUE REALIZAM ESTA OPERAÇÃO

        -DQL
            FUNÇÕES NESTE CODIGO QUE REALIZAM ESTA OPERAÇÃO







"""

import sqlite3


# -----------------------------------------------------------------
# CRIANDO AS TABELAS SQL

# $TABELA SEGUNDA FEIRA
# conn.execute('''CREATE TABLE SEGUNDA
#            (id INTEGER PRIMARY KEY AUTOINCREMENT,
#            HORARIO1 INT NOT NULL,
#            MATERIA1 TEXT NOT NULL,
#            HORARIO2 INT NOT NULL,
#            MATERIA2 INT NOT NULL);''')

# $TABELA TERCA FEIRA
# conn.execute(''' CREATE TABLE TERCA
#            ( id INTEGER PRIMARY KEY AUTOINCREMENT,
#            HORARIO1 INT NOT NULL,
#            MATERIA1 TEXT NOT NULL,
#            HORARIO2 INT NOT NULL,
#            MATERIA2 INT NOT NULL);''')

# $TABELA QUARTA FEIRA
# conn.execute(''' CREATE TABLE QUARTA
#            (id INTEGER PRIMARY KEY AUTOINCREMENT,
#            HORARIO1 INTEGER NOT NULL,
#            MATERIA1 TEXT NOT NULL,
#            HORARIO2 INTEGER NOT NULL,
#            MATERIA2 TEXT NOT NULL);''')

# $TABELA QUINTA FEIRA
# conn.execute(''' CREATE TABLE QUINTA
#            (id INTEGER PRIMARY KEY AUTOINCREMENT,
#            HORARIO1 INTEGER NOT NULL,
#           MATERIA1 TEXT NOT NULL,
#            HORARIO2 INTEGER NOT NULL,
#            MATERIA2 TEXT NOT NULL); ''')

# $TABELA SEXTA FEIRA
# conn.execute(''' CREATE TABLE SEXTA
#            (id INTEGER PRIMARY KEY AUTOINCREMENT,
#            HORARIO1 INTEGER NOT NULL,
#            MATERIA1 TEXT NOT NULL,
#            HORARIO2 INTEGER NOT NULL,
#            MATERIA2 TEXT NOT NULL);''')

# $TABELA SABADO
# conn.execute(''' CREATE TABLE SABADO
#            (id INTEGER PRIMARY KEY AUTOINCREMENT,
#            HORARIO INTEGER NOT NULL,
#            MATERIA1 TEXT NOT NULL,
#            HORARIO2 INTEGER NOT NULL,
#            MATERIA2 TEXT NOT NULL);''')


# -----------------------------------------------------------------

# VER AGENDA:

def verSEG():
    try:
        connverseg = sqlite3.connect('AGENDA.db')

        # Criar um cursor
        cur = connverseg.cursor()

        # Executar o SELECT
        cur.execute("SELECT * FROM SEGUNDA")

        # Obter todos os resultados
        resultados = cur.fetchall()

        # Percorrer os resultados e imprimir cada linha
        for linha in resultados:
            print(linha)

        # Fechar o cursor e a conexão
        cur.close()
        connverseg.close()

        # Retornar mensagem de sucesso
        return "Operação ver Segunda-Feira bem-sucedida"
    except Exception as e:
        # Retornar mensagem de erro
        return "Operação ver Segunda-Feira não-sucedida. Erro: {}".format(e)


def verTER():
    try:
        connverterc = sqlite3.connect('AGENDA.db')

        # Criar um cursor
        cur = connverterc.cursor()

        # Executar o SELECT
        cur.execute("SELECT * FROM TERCA")

        # Obter todos os resultados
        resultados = cur.fetchall()

        # Percorrer os resultados e imprimir cada linha
        for linha in resultados:
            print(linha)

        # Fechar o cursor e a conexão
        cur.close()
        connverterc.close()

        # Retornar mensagem de sucesso
        return "Operação ver Segunda-Feira bem-sucedida"
    except Exception as e:
        # Retornar mensagem de erro
        return "Operação ver Segunda-Feira não-sucedida. Erro: {}".format(e)


def verQUA():
    try:
        connverseg = sqlite3.connect('AGENDATESTE.db')

        # Criar um cursor
        cur = connverseg.cursor()

        # Executar o SELECT
        cur.execute("SELECT * FROM QUARTA")

        # Obter todos os resultados
        resultados = cur.fetchall()

        # Percorrer os resultados e imprimir cada linha
        for linha in resultados:
            print(linha)

        # Fechar o cursor e a conexão
        cur.close()
        connverseg.close()
        return "Operação bem sucedida."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


def verQUI():
    try:
        connverqui = sqlite3.connect('AGENDA.DB')

        # Criar um cursor
        cur = connverqui.cursor()

        # Obter todos os Resultados
        resultados = cur.fetchall()

        # Percorrer os resultados e imprimir cada linha
        for linha in resultados:
            print(linha)

        cur.close()
        connverqui.close()
        return "Operação bem sucedida."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


def verSex():
    try:
        connversex = sqlite3.connect('AGENDA.DB')

        # Criar um cursor
        cur = connversex.cursor()

        # Obter todos os resultados
        resultados = cur.fetchall()

        # Percorrer os resultados e imprimir cada linha
        for linha in resultados:
            print(linha)

        cur.close()
        connversex.close()
        return "Operação bem sucedida."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


def verSAB():
    try:
        connversab = sqlite3.connect('AGENDA.DB')

        # Criar um cursor
        cur = connversab.cursor()

        # Obter todos os resultados
        resultados = cur.fetchall()

        # Percorrer os resultados e imprimir cada linha
        for linha in resultados:
            print(linha)

        cur.close()
        connversab.close()
        return "Operação bem sucedida."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


# -----------------------------------------------------------------
# PARTE DO CODIGO PARA DAR UPDATE NAS TABELAS DE TODAS AS INFORMAÇÕES


def updateSEG():
    try:
        connseg = sqlite3.connect('AGENDA.db')
        cursor = connseg.cursor()

        nv_m1, nv_h1, nv_m2, nv_h2 = input("Digite o novo valor para {}: ".format("MATERIA1")), input(
            "Digite o novo valor para {}: ".format("HORARIO1")), input(
            "Digite o novo valor para {}: ".format("MATERIA2")), input(
            "Digite o novo valor para {}: ".format("HORARIO2"))

        # Atualiza a tabela segunda feira
        cursor.execute("UPDATE SEGUNDA SET MATERIA1 = ?, MATERIA2 = ?, MATERIA3 = ?, MATERIA4 = ?",
                       (nv_m1, nv_h1, nv_m2, nv_h2))

        # Salva as alterações
        connseg.commit()

        # Fecha a conexão com o banco de dados
        connseg.close()

        print("OPERAÇÃO BEM SUCEDIDA, UPDATE NA TABELA SEGUNDA FEIRA, FINALIZADA SEM ERROS")
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"

    # Retorna ao menu principal após a atualização
    menu_principal()


def updateTER():
    try:
        connter = sqlite3.connect('AGENDA.db')
        cursor = connter.cursor()

        nv_m1, nv_h1, nv_m2, nv_h2 = input("Digite o novo valor para {}: ".format("MATERIA1")), input(
            "Digite o novo valor para {}: ".format("HORARIO1")), input(
            "Digite o novo valor para {}: ".format("MATERIA2")), input(
            "Digite o novo valor para {}: ".format("HORARIO2"))

        # Atualiza a tabela terca feira
        cursor.execute("UPDATE SEGUNDA SET MATERIA1 = ?, MATERIA2 = ?, MATERIA3 = ?, MATERIA4 = ?",
                       (nv_m1, nv_h1, nv_m2, nv_h2))

        # Salva as alterações
        connter.commit()

        # Fecha a conexão com o banco de dados
        connter.close()

        return "OPERAÇÃO BEM SUCEDIDA,UPDATE NA TERCA FEIRA FINALIZADA SEM ERROS."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


def updateQUA():
    try:

        connqua = sqlite3.connect('AGENDA.db')
        cursor = connqua.cursor()

        nv_m1, nv_h1, nv_m2, nv_h2 = input("Digite o novo valor para {}: ".format("MATERIA1")), input(
            "Digite o novo valor para {}: ".format("HORARIO1")), input(
            "Digite o novo valor para {}: ".format("MATERIA2")), input(
            "Digite o novo valor para {}: ".format("HORARIO2"))

        # Atualiza a tabela quarta feira
        cursor.execute("UPDATE SEGUNDA SET MATERIA1 = ?, MATERIA2 = ?, MATERIA3 = ?, MATERIA4 = ?",
                       (nv_m1, nv_h1, nv_m2, nv_h2))

        # Salva as alterações
        connqua.commit()

        # Fecha a conexão com o banco de dados
        connqua.close()
        return "OPERAÇÃO BEM SUCEDIDA, UPDATE REALIZADO NA TABELA QUARTA FEIRA."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


def updateQUI():
    try:
        connqui = sqlite3.connect('AGENDA.db')
        cursor = connqui.cursor()

        nv_m1, nv_h1, nv_m2, nv_h2 = input("Digite o novo valor para {}: ".format("MATERIA1")), input(
            "Digite o novo valor para {}: ".format("HORARIO1")), input(
            "Digite o novo valor para {}: ".format("MATERIA2")), input(
            "Digite o novo valor para {}: ".format("HORARIO2"))

        # Atualiza a tabela quinta feira
        cursor.execute("UPDATE SEGUNDA SET MATERIA1 = ?, MATERIA2 = ?, MATERIA3 = ?, MATERIA4 = ?",
                       (nv_m1, nv_h1, nv_m2, nv_h2))

        # Salva as alterações
        connqui.commit()

        # Fecha a conexão com o banco de dados
        connqui.close()
        return "OPERAÇÃO BEM SUCEDIDA, UPDATE RALIZADO NA TABELA QUINTA FEIRA"
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


def updateSEX():
    try:
        connsex = sqlite3.connect('AGENDA.db')
        cursor = connsex.cursor()

        nv_m1, nv_h1, nv_m2, nv_h2 = input("Digite o novo valor para {}: ".format("MATERIA1")), input(
            "Digite o novo valor para {}: ".format("HORARIO1")), input(
            "Digite o novo valor para {}: ".format("MATERIA2")), input(
            "Digite o novo valor para {}: ".format("HORARIO2"))

        # Atualiza a tabela sexta feira
        cursor.execute("UPDATE SEGUNDA SET MATERIA1 = ?, MATERIA2 = ?, MATERIA3 = ?, MATERIA4 = ?",
                       (nv_m1, nv_h1, nv_m2, nv_h2))

        # Salva as alterações
        connsex.commit()

        # Fecha a conexão com o banco de dados
        connsex.close()
        return "OPERAÇÃO SUCEDIDA, UPDATE REALIZADO NA TABELA QUARTAFEIRA"
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


def updateSAB():
    try:
        connsab = sqlite3.connect('AGENDA.db')
        cursor = connsab.cursor()

        nv_m1, nv_h1, nv_m2, nv_h2 = input("Digite o novo valor para {}: ".format("MATERIA1")), input(
            "Digite o novo valor para {}: ".format("HORARIO1")), input(
            "Digite o novo valor para {}: ".format("MATERIA2")), input(
            "Digite o novo valor para {}: ".format("HORARIO2"))

        # Atualiza a tabela sabado
        cursor.execute("UPDATE SEGUNDA SET MATERIA1 = ?, MATERIA2 = ?, MATERIA3 = ?, MATERIA4 = ?",
                       (nv_m1, nv_h1, nv_m2, nv_h2))

        # Salva as alterações
        connsab.commit()

        # Fecha a conexão com o banco de dados
        connsab.close()
        return "OPERAÇÃO BEM SUCEDIDA, TABELA ATUALIZADA"
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


# ------------------------------------------------------------------
# PARTE DO CODIGO DE FUNÇÕES PARA DELETAR OS DADOS DAS TABELAS

def deletSEG():
    try:
        conndelseg = sqlite3.connect('AGENDA.DB')
        cursor = conndelseg.cursor()

        # EXCLUI TODOS OS DADOS DA TABELA SEGUNDA
        cursor.execute("DELETE FROM SEGUNDA;")

        # SALVA AS ALTERAÇÕES
        conndelseg.commit()

        # FECHA A CONEXÃO COM O BANCO DE DADOS
        conndelseg.close()
        return "OPERAÇÃO BEM SUCEDIDA, DADOS DA TABELA SEGUNDA APAGADOS COM SUCESSO."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


def deletTER():
    try:
        conndelter = sqlite3.connect('AGENDA.DB')
        cursor = conndelter.cursor()

        # EXCLUI TODOS OS DADOS DA TABELA TERÇA
        cursor.execute("DELETE FROM TERCA;")

        # SALVA AS ALTERAÇÕES
        conndelter.commit()

        # FECHA A CONEXÃO COM O BANCO DE DADOS
        conndelter.close()
        return "OPERAÇÃO BEM SUCEDIDA, DADOS DA TABELA TERÇA APAGADOS COM SUCESSO."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


def deletQUA():
    try:
        conndelqua = sqlite3.connect('AGENDA.DB')
        cursor = conndelqua.cursor()

        cursor.execute("DELETE FROM QUA;")

        conndelqua.commit()

        conndelqua.close()
        return "OPERAÇÃO BEM SUCEDIDA, DADOS DA TABELA QUARTA APAGADOS COM SUCESSO."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


def deletQUI():
    try:
        conndelqui = sqlite3.connect('AGENDA.DB')
        cursor = conndelqui.cursor()

        cursor.execute("DELETE FROM QUI;")

        conndelqui.commit()

        conndelqui.close()
        return "OPERAÇÃO BEM SUCEDIDA, DADOS DA TABELA QUINTA APAGADOS COM SUCESSO."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


def deletSEX():
    try:
        conndelsex = sqlite3.connect('AGENDA.DB')
        cursor = conndelsex.cursor()

        cursor.execute("DELETE FROM SEX;")

        conndelsex.commit()

        conndelsex.close()
        return "OPERAÇÃO BEM SUCEDIDA, DADOS DA TABELA SEXTA APAGADOS COM SUCESSO."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


def deletSAB():
    try:
        conndelsab = sqlite3.connect('AGENDA.DB')
        cursor = conndelsab.cursor()

        cursor.execute("DELETE FROM SAB;")

        conndelsab.commit()

        conndelsab.close()
        return "OPERAÇÃO BEM SUCEDIDA, DADOS DA TABELA SABADO APAGADOS COM SUCESSO."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


# -------------------------------------------------------------------
# ADICIONAR COLUNA ÀS COLUNAS

# noinspection PyGlobalUndefined
def adicionarCol():
    try:
        connadd = sqlite3.connect('AGENDA.DB')
        cursor = connadd.cursor()

        tabela = input("DIGITE O NOME DA TABELA")
        tabela_upper = tabela.upper()
        coluna = input("DIGITE O NOME DA COLUNA")

        tipo_dado = input("DIGITE O TIPO DE DADO DA COLUNA:")

        # concatena as informações na string da consulta SQL
        sql_query = f"ALTER TABLE{tabela_upper}ADD COLUMN {coluna} {tipo_dado}"

        cursor.execute(sql_query)

        connadd.commit()

        connadd.close()
        return "OPERAÇÃO BEM SUCEDIDA, COLUNA ADICIONADA COM SUCESSO."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


# -------------------------------------------------------------------
# DELETAR ESPECIFICAMENTE UMA COLUNA

def apagar_coluna():
    try:
        connapgcol = sqlite3.connect('AGENDA.DB')
        cursor = connapgcol.cursor()

        tabeladc = input("DIGITE O NOME DA TABELA:")
        colunadc = input("DIGITE O NOME DA COLUNA A SER EXCLUÍDA:")

        sql_query = f"ALTER TABLE {tabeladc} DROP COLUMN {colunadc}"

        cursor.execute(sql_query)

        connapgcol.commit()

        connapgcol.close()
        return "OPERAÇÃO BEM SUCEDIDA, DADOS DA TABELA QUARTA APAGADOS COM SUCESSO."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


# -------------------------------------------------------------------
# ADICIONAR TABELAS NO BDD


def add_tabble():
    try:
        connaddtable = sqlite3.connect('AGENDA.DB')
        cursor = connaddtable.cursor()

        # SOLICITA O NOVO NOME DA TABELA QUE IREMOS CRIAR
        nome_tabela = str(input("INFORME O NOME DA NOVA TABELA"))

        # CRIA UMA STRING DE CONSULTA SQL PARA CRIAR UMA NOVA TABELA, COM AS COLUNAS QUE JA EXISTEM NAS OUTRAS TABELAS
        sql_query = f"CREATE TABLE {nome_tabela} (" \
                    f"ID INTEGER PRIMARY KET AUTOINCREMENT MATERIA1 TEXT, HORARIO1 TEXT, MATERIA2 TEXT, HORARIO2 TEXT)"
        cursor.execute(sql_query)

        connaddtable.commit()

        connaddtable.close()
        return "OPERAÇÃO BEM SUCEDIDA, TABELA ADICIONADA COM SUCESSO."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


# -------------------------------------------------------------------
# DELETAR TABLES DO BANCO DE DADOS----------------------------------
# -------------------------------------------------------------------


def apagar_tabela():
    try:
        conndeltable = sqlite3.connect('AGENDA.DB')
        tabela_at = input("INFORME O NOME DA TABELA...")
        cursor = conndeltable.cursor()
        cursor.execute("DROP TABLE IF EXISTS" + tabela_at)
        conndeltable.commit()
        conndeltable.close()
        return "OPERAÇÃO BEM SUCEDIDA TABELA EXCLUIDA COM SUCESSO..."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


def decisao_sair():
    try:
        print("\t:::DESEJA VOLTAR AO MENU PRINCIPAL? S OU N::::")
        voltar = str(input("$DIGITE A OPÇÃO DESEJADA$\n---"))
        if voltar.lower() == 's' or voltar.lower() == 'sim':
            menu_principal()
        elif voltar.lower() == 'n' or voltar.lower() == 'nao':
            try:
                print("@@==$OPERAÇÃO FINALIZADA COM SUCESSO$==@@")
                sair = input("DESEJA SAIR DO SISTEMA?\n---")
                if sair.lower() == 's' or sair.lower() == 'sim':
                    exit()
                elif sair.lower() == 'n' or sair.lower() == 'nao':
                    menu_principal()
                else:
                    print("\t@@==:$OPERAÇÃO FINALIZADA, ENTRADA DE DADOS ERRADA$:==@@")
                return "@@==:$OPERAÇÃO BEM SUCEDIDA$:==@@"
            except sqlite3.OperationalError as e:
                return f"Operação não sucedida. Erro: {str(e)}"
        else:
            print("@@==:$OPERAÇÃO FINALIZADA, ENTRADA DE DADOS ERRADA$:==@@")
            menu_principal()
        return "@@==:$OPERAÇÃO BEM SUCEDIDA$:==@@"
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


# -------------------------------------------------------------------
# NOTAS CRIAR, INSERIR E REFERENCIAR---------------------------------
# -------------------------------------------------------------------

def adicionar_nota():
    try:
        connNota = sqlite3.connect('AGENDA.DB')
        cursor = connNota.cursor()
        semana_dia = str(input("EM QUE DIA DA SEMANA SUA NOTA IRÁ APARECER?"))
        if semana_dia == 'segunda':
            try:
                Nome_nota = input("INFORME O NOME DA NOTA...")
                titulo = str(input("INFORME O TITULO DA NOTA"))

                sql_query = f"               create table {Nome_nota}" \
                            f"( ID  integer not null " \
                            f"  constraint table_name_pk" \
                            f"     primary key autoincrement" \
                            f"   constraint table_SEGUNDA_id_fk" \
                            f"   references SEGUNDA" \
                            f" {titulo}   text  not null" \
                            f" conteudo  text   not null"

                cursor.execute(sql_query)

                connNota.commit()

                connNota.close()
                return "OPERAÇÃO BEM SUCEDIDA, TABELA ADICIONADA COM SUCESSO."
            except sqlite3.OperationalError as e:
                return f"Operação não sucedida. Erro: {str(e)}"
        elif semana_dia.lower() == 'terca':
            try:
                Nome_nota = input("INFORME O NOME DA NOTA...")
                titulo = str(input("INFORME O TITULO DA NOTA"))

                sql_query = f"               create table {Nome_nota}" \
                            f"( ID  integer not null " \
                            f"  constraint table_name_pk" \
                            f"     primary key autoincrement" \
                            f"   constraint table_TERCA_id_fk" \
                            f"   references TERCA" \
                            f" {titulo}   text  not null" \
                            f" conteudo  text   not null"

                cursor.execute(sql_query)

                connNota.commit()

                connNota.close()
                return "OPERAÇÃO BEM SUCEDIDA, TABELA ADICIONADA COM SUCESSO."
            except sqlite3.OperationalError as e:
                return f"Operação não sucedida. Erro: {str(e)}"
        elif semana_dia.lower() == 'quarta':
            try:
                Nome_nota = input("INFORME O NOME DA NOTA...")
                titulo = str(input("INFORME O TITULO DA NOTA"))

                sql_query = f"               create table {Nome_nota}" \
                            f"( ID  integer not null " \
                            f"  constraint table_name_pk" \
                            f"     primary key autoincrement" \
                            f"   constraint table_QUARTA_id_fk" \
                            f"   references QUARTA" \
                            f" {titulo}   text  not null" \
                            f" conteudo  text   not null"

                cursor.execute(sql_query)

                connNota.commit()

                connNota.close()
                return "OPERAÇÃO BEM SUCEDIDA, TABELA ADICIONADA COM SUCESSO."
            except sqlite3.OperationalError as e:
                return f"Operação não sucedida. Erro: {str(e)}"
        elif semana_dia.lower() == 'quinta':
            try:
                Nome_nota = input("INFORME O NOME DA NOTA...")
                titulo = str(input("INFORME O TITULO DA NOTA"))

                sql_query = f"               create table {Nome_nota}" \
                            f"( ID  integer not null " \
                            f"  constraint table_name_pk" \
                            f"     primary key autoincrement" \
                            f"   constraint table_QUINTA_id_fk" \
                            f"   references QUINTA" \
                            f" {titulo}   text  not null" \
                            f" conteudo  text   not null"

                cursor.execute(sql_query)

                connNota.commit()

                connNota.close()
                return "OPERAÇÃO BEM SUCEDIDA, TABELA ADICIONADA COM SUCESSO."
            except sqlite3.OperationalError as e:
                return f"Operação não sucedida. Erro: {str(e)}"
        elif semana_dia.lower() == 'sexta':
            try:
                Nome_nota = input("INFORME O NOME DA NOTA...")
                titulo = str(input("INFORME O TITULO DA NOTA"))

                sql_query = f"               create table {Nome_nota}" \
                            f"( ID  integer not null " \
                            f"  constraint table_name_pk" \
                            f"     primary key autoincrement" \
                            f"   constraint table_SEXTA_id_fk" \
                            f"   references SEXTA" \
                            f" {titulo}   text  not null" \
                            f" conteudo  text   not null"

                cursor.execute(sql_query)

                connNota.commit()

                connNota.close()
                return "OPERAÇÃO BEM SUCEDIDA, TABELA ADICIONADA COM SUCESSO."
            except sqlite3.OperationalError as e:
                return f"Operação não sucedida. Erro: {str(e)}"
        elif semana_dia.lower() == 'sabado':
            try:
                Nome_nota = input("INFORME O NOME DA NOTA...")
                titulo = str(input("INFORME O TITULO DA NOTA"))

                sql_query = f"               create table {Nome_nota}" \
                            f"( ID  integer not null " \
                            f"  constraint table_name_pk" \
                            f"     primary key autoincrement" \
                            f"   constraint table_SABADO_id_fk" \
                            f"   references SABADO" \
                            f" {titulo}   text  not null" \
                            f" conteudo  text   not null"

                cursor.execute(sql_query)

                connNota.commit()

                connNota.close()
                return "OPERAÇÃO BEM SUCEDIDA, TABELA ADICIONADA COM SUCESSO."
            except sqlite3.OperationalError as e:
                return f"Operação não sucedida. Erro: {str(e)}"

        return "OPERAÇÃO BEM SUCEDIDA, TABELA ADICIONADA COM SUCESSO."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


# -------------- ANTIGO CODIGO ------------------------------

#   Criando uma tabela para notas se ela ainda não existir
#    conn = sqlite3.connect("AGENDA.DB")
#
#    nome_da_nota = str(input("INFORME O NOME DA NOTA\n---"))
#
#    sql_query = f'''CREATE TABLE IF NOT EXISTS {nome_da_nota}
#                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   NOME TEXT NOT NULL,
#                   CONTEUDO TEXT NOT NULL);'''
#
#    conn.execute(sql_query)
#
#    # Recebendo o nome da tabela por input
#    tabela = input('Digite o nome da tabela a ser alterada: ').upper()
#
#    # Adicionando a coluna NOTA_ID à tabela especificada
#    conn.execute(f'''ALTER TABLE {tabela}
#                    ADD COLUMN NOTA_ID INTEGER,
#                    FOREIGN KEY (NOTA_ID) REFERENCES NOTA(id));''')#
#
#    print("Coluna NOTA_ID adicionada com sucesso à tabela ", tabela)"""


# -------------------------------------------------------------------
# MODIFICAR O TIPO DE UMA COLUNA ------------------------------------
# -------------------------------------------------------------------


def alterar_tipo_coluna():
    # Conecta-se ao banco de dados
    conexao = sqlite3.connect('AGENDA.db')

    # Cria um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Recebe os valores de entrada do usuário
    nome_tabela = input("\t@@@DIGITE O NOME DA TABELA@@@:\n--- ")
    nome_coluna = input("\t@@@DIGITE O NOME DA COLUNA A SER MODIFICADA@@@:\n--- ")
    novo_tipo = input("\t@@@DIGITE O TIPO QUE DESEJA ATRIBUIR A COLUNA SELECIONADA:@@@@\n--- ")

    # Executa o comando SQL para modificar o tipo de uma coluna na tabela especificada
    comando_sql = f"ALTER TABLE {nome_tabela} MODIFY COLUMN {nome_coluna} {novo_tipo};"
    cursor.execute(comando_sql)

    # Salva as alterações no banco de dados
    conexao.commit()

    # Fecha a conexão com o banco de dados
    conexao.close()


# ----------------------------------------------------------------------
# --------------------------- MENU PRINCIPAL ---------------------------
# ----------------------------------------------------------------------


def menu_principal():
    print("\t\t\t\t@====================================@")
    print("\t\t\t\t@==-BEM VINDO À SUA AGENDA ROZENDO-==@")
    print("\t\t\t\t@====================================@")

    # nesta variavel será decidido qual opção o usuario Rozendo irá usar

    print("\t\t\t@@@==== 1 - VER AGENDA ================@@@")
    print("\t\t\t@@@==== 2 - MODIFICAR AGENDA ==========@@@")
    print("\t\t\t@@@==== 3 - APAGAR DADOS DAS TABELAS ==@@@")
    print("\t\t\t@@@==== 4-  ADICIONAR COLUNAS =========@@@")
    print("\t\t\t@@@==== 5 - REMOVER COLUNAS ===========@@@")
    print("\t\t\t@@@==== 6-  ADICIONAR TABELAS =========@@@")
    print("\t\t\t@@@==== 7-  APAGAR TABELAS ============@@@")
    print("\t\t\t@@@==== 8-  MODIFICAR TIPO DA COLUNA ==@@@")
    print("\t\t\t@@@==== 9-  ADICIONAR NOTAS ===========@@@")

    decisao = int(input("Oque deseja fazer?\n---"))

    # VER AGENDA
    if decisao == 1:
        print("\t\t$ digite segunda para segunda feira              $")
        print("\t\t$ digite terça para terça feira                  $")
        print("\t\t$ digite quarta para quarta feira                $")
        print("\t\t$ digite quinta para quinta feira                $")
        print("\t\t$ digite sexta para sexta feira                  $")
        print("\t\t$ digite sabado para sabado                      $")
        print("\t\t$ digite outra tabela para acessar outra tabela  $")
        entrada = input('\t::-  DIGITE O DIA DA SEMANA QUE VOCÊ DESEJA VER  -::\n---')
        while entrada != "exit":

            if entrada.lower() == 'segunda':
                print('\nSUA AGENDA DE SEGUNDA FEIRA É:\n')
                print(verSEG() + "\n")
                decisao_sair()
            elif entrada.lower() == 'terca':
                print(verTER() + "\n")
                decisao_sair()
            elif entrada.lower() == "quarta":
                print(verQUA())
                decisao_sair()
            elif entrada.lower() == "quinta":
                print(verQUI())
                decisao_sair()
            elif entrada.lower() == "sexta":
                print(verSex())
                decisao_sair()
            elif entrada.lower() == "sabado":
                print(verSAB())
                decisao_sair()
            elif entrada == "exit":
                print("@@OBRIGADO POR USAR O SISTEMA DE GERENCIAMENTO DE AGENDA.@@")
                break
            # FIXME: PENSAR NA PROPOSTA DE INFORMAR A TABELA A SER ACESSADA
            # elif entrada == 'outra tabela':
            # outra_tabela = input("INFORME A OUTRA TABELA A SER ACESSADA")

            else:
                raise Exception("ENTRADA DE DADOS ERRADA, TERMINANDO SUA SESSÃO...")

    # MODIFICAR AGENDA- MODIFICAR POR INTEIRA
    elif decisao == 2:
        decisao_MOD = input("@@=INFORME O DIA DA SEMANA PARA ALTERAR=@@")
        while decisao_MOD != "exit":
            if decisao_MOD.lower() == 'segunda':
                updateSEG()
                decisao_sair()
            elif decisao_MOD.lower() == 'terca':
                updateTER()
                decisao_sair()
            elif decisao_MOD.lower() == 'quarta':
                updateQUA()
                decisao_sair()
            elif decisao_MOD.lower() == 'quinta':
                updateQUI()
                decisao_sair()
            elif decisao_MOD.lower() == 'sexta':
                updateSEX()
                decisao_sair()
            elif decisao_MOD.lower() == 'sabado':
                updateSAB()
                decisao_sair()
            elif decisao_MOD == 'exit':
                print("@@OBRIGADO POR USAR O SISTEMA DE GERENCIAMENTO DE AGENDA, FINALIZANDO@@")
                break
            else:
                raise Exception("@@@ENTRADA DE DADOS ERRADA, TERMINANDO A SESSÃO@@@")

    # APAGAR TODOS OS DADOS DA TABELA
    elif decisao == 3:
        print("\t@@@BEM VINDO, ESTA OPÇÃO IRÁ APAGAR A TABELA COMPLETAMENTE@@@")
        print("@escreva o dia ou escreva -EXIT- para sair@")
        decisao3 = input("INFORME -[]- ")

        while decisao3 != "EXIT":
            if decisao3.lower() == 'segunda':
                deletSEG()
                decisao_sair()
            elif decisao3.lower() == "terca":
                deletTER()
                decisao_sair()
            elif decisao3.lower() == "quarta":
                deletQUA()
                decisao_sair()
            elif decisao3.lower() == "quinta":
                deletQUI()
                decisao_sair()
            elif decisao3.lower() == "sexta":
                deletSEX()
                decisao_sair()
            elif decisao3.lower() == "sabado":
                deletSAB()
                decisao_sair()
            # ADICIONAR ITENS NA TABELA
    elif decisao == 4:
        print("\t@@@BEM VINDO, ESTA OPÇÃO IRÁ ADICIONAR ITENS A TABELA QUE DESEJA@@@")
        adicionarCol()
        decisao_sair()
    # REMOVER COLUNAS
    elif decisao == 5:
        print("\t@@@BEM VINDO, ESTA OPÇÃO IRÁ REMOVER COLUNAS DA SUA TABELA@@@")
        apagar_coluna()
        decisao_sair()
    # ADICIONAR TABELA
    elif decisao == 6:
        print("\t@@@BEM VINDO, ESTA OPÇÃO IRÁ ADICIONAR UMA TABELA NOVA AO SEU BDD@@@")
        add_tabble()
        decisao_sair()
    elif decisao == 7:
        print("\t@@@BEM VINDO, ESTA OPÇÃO IRÁ REMOVER A TABELA DESEJADA@@@")
        apagar_tabela()
        decisao_sair()
    elif decisao == 8:
        print("@@@BEM VINDO, ESTA OPÇÃO IRÁ ALTERAR O TIPO DA SUA COLUNA DESEJADA@@@\n")
        alterar_tipo_coluna()
        decisao_sair()
    elif decisao == 9:
        print("\t@@@BEM VINDO, ESTÁ OPÇÃO IRA ADICIONAR UMA NOTA@@@")
        adicionar_nota()
        decisao_sair()
    else:
        raise Exception("------------------ OPÇÃO INVALIDA -------------------------")


menu_principal()
