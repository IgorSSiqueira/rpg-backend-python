import os
from models.personagem import Personagem
from models.constantes import USAR_ITEM, ATACAR, USAR_MAGIA
from models.inimigos import gerar_inimigo
from utils.mensagens import INICIANDO_RPG, esperar_jogador

def main():
    os.system('cls')
    print(INICIANDO_RPG)

    nome_jogador = input('Digite o nome do seu personagem: ')

    Player = Personagem(nome_jogador, True)
    Player.iniciar_rpg(Player.nome)

    os.system('cls')
    print('Enquanto você estava terminando de se equipar, apareceu um goblin e te atacou.\nBATALHA INICIADA')
    esperar_jogador()

    inimigo_gerado = gerar_inimigo(Player._level)
    Inimigo = Personagem(inimigo_gerado['nome'], False, inimigo_gerado['level'], inimigo_gerado['cod_arma'])

    opc = ''
    while opc == '':
        opc = Player.acao_turno(Player.nome, Inimigo.nome)

    # PRECISAMOS FAZER AGORA A PARTE DA BATALHA
    # SEMPRE MOSTRAR A VIDA DO PLAYER

    

if __name__ == '__main__':
    main()