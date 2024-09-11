import os
import sys
import random
from models.personagem import Personagem
from utils.constantes import BATALHA_CONTINUA, INIMIGO_MORREU, PLAYER_MORREU, PROCURAR_INIMIGO, AREA_ANTERIOR, AREA_PROXIMA
from models.inimigos import gerar_inimigo, gerar_primeiro_inimigo
from utils.mensagens import INICIANDO_RPG, esperar_jogador

def comecar_jogo():
    os.system('cls')
    print(INICIANDO_RPG)
    
    nome_jogador = input('Digite o nome do seu personagem: ')

    Player = Personagem(nome_jogador, True)
    Player.iniciar_rpg(Player.nome)

    os.system('cls')
    print('Enquanto você estava terminando de se equipar, apareceu um goblin e te atacou.\nBATALHA INICIADA')
    esperar_jogador()
    inimigo_gerado = gerar_primeiro_inimigo()
    gold_inimigo = random.randint(inimigo_gerado['gold_min'], inimigo_gerado['gold_max'])
    Inimigo = Personagem(inimigo_gerado['nome'], False, inimigo_gerado['level'], inimigo_gerado['cod_arma'], gold_inimigo, inimigo_gerado['chefe'])

    #PRIMEIRA BATALHA
    dados_batalha = BATALHA_CONTINUA
    while dados_batalha == BATALHA_CONTINUA:
        dados_batalha = Player.acao_turno(Player.nome, Inimigo.nome)

        if dados_batalha == '':
            dados_batalha = BATALHA_CONTINUA
            continue
        elif dados_batalha == BATALHA_CONTINUA:
            continue
        elif dados_batalha == INIMIGO_MORREU:
            break
        elif dados_batalha == PLAYER_MORREU:
            print('GAME OVER')
            esperar_jogador()
            sys.exit()
            #CHAMAR FUNÇÃO PARA INICIAR O JOGO NOVAMENTE OU FECHAR O JOGO

    while True:
        dados_batalha = Player.acao_antes_batalha(Player.nome)

        if dados_batalha == PROCURAR_INIMIGO or dados_batalha == AREA_ANTERIOR or dados_batalha == AREA_PROXIMA:
            inimigo_gerado = gerar_inimigo(Player.area_atual)
            gold_inimigo = random.randint(inimigo_gerado['gold_min'], inimigo_gerado['gold_max'])
            Inimigo = Personagem(inimigo_gerado['nome'], False, inimigo_gerado['level'], inimigo_gerado['cod_arma'], gold_inimigo, inimigo_gerado['chefe'])

            print(f'Um {Inimigo.nome} te atacou. Batalha iniciada!')
            esperar_jogador()
            dados_turno = BATALHA_CONTINUA
            while dados_turno == BATALHA_CONTINUA:
                dados_turno = Player.acao_turno(Player.nome, Inimigo.nome)

                if dados_turno == '' or dados_turno == BATALHA_CONTINUA:
                    dados_turno = BATALHA_CONTINUA
                    continue
                elif dados_turno == INIMIGO_MORREU:
                    break
                elif dados_turno == PLAYER_MORREU:
                    print('GAME OVER')
                    esperar_jogador()
                    #CHAMAR FUNÇÃO PARA INICIAR O JOGO NOVAMENTE OU FECHAR O JOGO
                    sys.exit()
                    
            
            continue
        
        elif dados_batalha == '':
            continue