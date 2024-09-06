import os
import random
from models.personagem import Personagem
from utils.constantes import BATALHA_CONTINUA, INIMIGO_MORREU, PLAYER_MORREU
from models.inimigos import gerar_inimigo, gerar_primeiro_inimigo
from utils.mensagens import INICIANDO_RPG, esperar_jogador

def main():
    os.system('cls')
    print(INICIANDO_RPG)
    
    nome_jogador = input('Digite o nome do seu personagem: ')

    Player = Personagem(nome_jogador, True)
    Player.iniciar_rpg(Player.nome)

    ###
    ###
    ###
    ###
    os.system('cls')
    print('Enquanto você estava terminando de se equipar, apareceu um goblin e te atacou.\nBATALHA INICIADA')
    esperar_jogador()
    inimigo_gerado = gerar_primeiro_inimigo()
    gold_inimigo = random.randint(inimigo_gerado['gold_min'], inimigo_gerado['gold_max'])
    Inimigo = Personagem(inimigo_gerado['nome'], False, inimigo_gerado['level'], inimigo_gerado['cod_arma'], gold_inimigo, inimigo_gerado['chefe'])

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
            #CHAMAR FUNÇÃO PARA INICIAR O JOGO NOVAMENTE
    ###
    ###
    ###
    ###
    
    #
    # FAZER A CONTINUAÇÃO DO JOGO
    #

    # o que vc quer fazer?
    # vou me curar com magia ou item
    # vou procurar um novo inimigo na mesma área

    # level 5
    # passar para a próxima área
    
    # área += 1
    # passei para a próxima área - enfrentar inimigo



    

if __name__ == '__main__':
    main()