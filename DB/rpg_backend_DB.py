import psycopg2

def return_connection():
    return psycopg2.connect(database='rpg_backend', user='postgres', password='1234', host='localhost', port='5432')

def create_database():
    try:
        conn = psycopg2.connect(database='postgres', user='postgres', password='1234', host='localhost', port='5432')
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Criando o banco de dados rpg_backend
        cursor.execute('CREATE DATABASE rpg_backend;')
        print('Database rpg_backend criada com sucesso.')
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f'Erro ao criar o banco de dados: {e}')
        
#################### ***** ####################
#################### ***** ####################

def create_tables():
    try:
        conn = return_connection()
        cursor = conn.cursor()
        # Criando o banco de dados rpg_backend
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS PLAYER (
            nome        VARCHAR(100) NOT NULL PRIMARY KEY,
            level       INT,
            hpmax       INT,
            hp          INT,
            mpmax       INT,
            mp          INT,
            xp          INT,
            xpup        INT,
            gold        INT,
            area_atual  INT,
            classe      VARCHAR(10) 
        );
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS ATRIBUTOS (
            nome_player VARCHAR(100) NOT NULL,
            forca INT,
            inteligencia INT,
            vitalidade INT,
            defesa INT,
            FOREIGN KEY (nome_player) REFERENCES PLAYER (nome)
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS EQUIPAMENTOS(
            nome_player VARCHAR(100) NOT NULL,
            arma        INT,
            escudo      INT,
            FOREIGN KEY (nome_player) REFERENCES PLAYER (nome)
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS ITEMS(
            nome_player VARCHAR(100) NOT NULL,
            cod_item    INT,
            quantidade  INT,
            FOREIGN KEY (nome_player) REFERENCES PLAYER (nome)
        );
        ''')
        conn.commit()
        print('Tabelas criadas com sucesso.')
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f'Erro ao criar as tabelas\n{e}')

#################### ***** ####################
#################### ***** ####################

def salvar_player(nome_player, level, hpmax, hp, mpmax, mp, xp, xpup, gold, area_atual, classe):
    try:
        conn = return_connection()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT EXISTS (
                SELECT 1 FROM PLAYER WHERE nome = '%s'
            );
        ''', (nome_player,))
        
        existe_player = cursor.fetchone()[0]

        if existe_player:
            cursor.execute('''
                UPDATE PLAYER
                SET level      = %s,
                    hpmax      = %s,
                    hp         = %s,
                    mpmax      = %s,
                    mp         = %s,
                    xp         = %s,
                    xpup       = %s,
                    gold       = %s,
                    area_atual = %s
                WHERE nome = %s;
            ''', (level, hpmax, hp, mpmax, mp, xp, xpup, gold, area_atual, nome_player))
        else:
            cursor.execute('''
                INSERT INTO PLAYER (nome, level, hpmax, hp, mpmax, mp, xp, xpup, gold, area_atual, classe)
                            VALUES (%s  , %s   , %s   , %s, %s   , %s, %s, %s  , %s  , %s        , %s    );
            ''', (nome_player, level, hpmax, hp, mpmax, mp, xp, xpup, gold, area_atual, classe))
        
        conn.commit()
        print('Dados salvos com sucesso!')
        
        cursor.close()
        conn.close()

    except Exception as e:
        print(f'Erro ao salvar PLAYER: {e}')    

#################### ***** ####################
#################### ***** ####################

def salvar_atributos(nome_player, forca, inteligencia, vitalidade, defesa):
    try:
        conn = return_connection()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT EXISTS (
                SELECT 1 FROM ATRIBUTOS WHERE nome = '%s'
            );
        ''', (nome_player,))
        
        existe_atributo = cursor.fetchone()[0]
        
        if existe_atributo:
            cursor.execute('''
            UPDATE ATRIBUTOS
            SET forca         = %s,
                inteligencia  = %s,
                vitalidade    = %s,
                defesa        = %s
            WHERE nome_player = '%s';
            ''', (forca, inteligencia, vitalidade, defesa, nome_player))
        else:
            cursor.execute('''
                INSERT INTO ATRIBUTOS (nome_player, forca, inteligencia, vitalidade, defesa)
                               VALUES (%s         , %s   , %s          , %s        , %s    );
            ''', (nome_player, forca, inteligencia, vitalidade, defesa))
        
        conn.commit()
        print('Dados atualizados com sucesso.')
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f'Erro ao salvar ATRIBUTOS: {e}')

#################### ***** ####################
#################### ***** ####################

def salvar_equipamento(nome_player, arma, escudo):
    try:
        conn = psycopg2.connect(database='rpg_backend', user = 'postgres', password='1234', host='localhost', port='5432')
        cursor = conn.cursor()

        cursor.execute('''
                SELECT EXISTS (
                    SELECT 1 FROM EQUIPAMENTOS WHERE nome = '%s'
                );
            ''', (nome_player,))
        
        existe_equipamento = cursor.fetchone()[0]
    
        if existe_equipamento:
            cursor.execute('''
            UPDATE EQUIPAMENTOS
               SET arma        = %s,
                   escudo      = %s
             WHERE nome_player = '%s';
            ''', (arma, escudo, nome_player))
        else:
            cursor.execute('''
                INSERT INTO EQUIPAMENTOS (nome_player, arma, escudo)
                                  VALUES (%s         , %s  , %s    );                           
            ''', (nome_player, arma, escudo))
        conn.commit()
        print('Dados atualizados com sucesso.')      

        cursor.close()
        conn.close()
    except Exception as e:
        print(f'Erro ao atualizar os dados: {e}')

#################### ***** ####################
#################### ***** ####################

def salvar_items(nome_player, cod_item, quantidade):
    try:
        conn = psycopg2.connect(database='rpg_backend', user = 'postgres', password='1234', host='localhost', port='5432')
        cursor = conn.cursor()
        
        cursor.execute('''
                SELECT EXISTS (
                    SELECT quantidade FROM ITEMS WHERE nome_player = '%s' and cod_item = %s
                );
            ''', (nome_player, cod_item))
        
        existe_item = cursor.fetchone()[0]
        print(f'Printando fech: {existe_item} <-\n')
    
        if existe_item:
            print('Se entrou aqui tá errado!')
            cursor.execute('''
            UPDATE ITEMS
            SET cod_item   = %s,
                quantidade = %s
            WHERE nome_player = '%s';
            ''', (cod_item, quantidade, nome_player))
        else:
            cursor.execute('''
                INSERT INTO ITEMS(nome_player, cod_item, quantidade)
                           VALUES(%s         , %s      , %s);                           
            ''', (nome_player, cod_item, quantidade))
        conn.commit()
        print('Dados atualizados com sucesso.')      

        cursor.close()
        conn.close()
    except Exception as e:
        print(f'Erro ao atualizar os dados: {e}')

#################### ***** ####################
#################### ***** ####################

def ler_tabela(dados, tabela, where = ''):
    try:
        conn = return_connection()
        cursor = conn.cursor()

        query = f'SELECT {dados} FROM {tabela} {where};'
        cursor.execute(query)
        rows = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return rows
    except Exception as e:
        print(f'Erro ao ler os dados: {e}')

#################### ***** ####################
#################### ***** ####################

def veriquicar_player_existe(nome):
    try:
        conn = return_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT nome FROM PLAYER WHERE nome = '%s'", (nome,))
        
        existe_player = cursor.fetchone()

        cursor.close()
        conn.close()

        if existe_player is not None:
            return True
        else:
            return False
    except Exception as e:
        print(f'Erro ao ler os dados: {e}')

#################### ***** ####################
#################### ***** ####################

# def delete_data(nome_player):
#     try:
#         conn = return_connection()
#         cursor = conn.cursor()
        
#         ##
#         ## APENAS UM EXEMPLO, AINDA VOU ALTERAR
#         ##
#         cursor.execute('DELETE FROM PLAYER WHERE nome = %s;', (nome_player,))
#         conn.commit()
#         print('Dados deletados com sucesso.')
        
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         print(f'Erro ao deletar os dados: {e}')
