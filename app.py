import os
from models.personagem import Personagem
from models.constantes import USAR_ITEM, ATACAR, USAR_MAGIA, INICIANDO_RPG

def main():
    os.system('cls')
    print(INICIANDO_RPG)

    nome_jogador = input('Digite o nome do seu personagem: ')

    Player = Personagem(nome_jogador, True)
    Player.iniciar_rpg(Player.nome)    
    Player.mostrar_hp_mp(Player.nome)
    Player.listar_atributos(Player.nome)
    
    # print('\n' + Player._inventario.verificar_armamentos_no_inventario(Player._nome) + '\n')    
    # print(Player._equipamentos.equipar(Player.nome))
    # print(Player.atacar(Player.nome))
    
    Inimigo = Personagem('Goblin', False)


if __name__ == '__main__':
    main()