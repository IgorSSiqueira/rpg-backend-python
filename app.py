import os
from models.personagem import Personagem

ADICIONAR = True
REMOVER = False


def main():
    os.system('cls')

    Player = Personagem('Jogador', True)

    Inimigo = Personagem('Goblin', False)

    Player.atacar(Player.nome, Inimigo.nome)

    #Player.iniciar_rpg(Player.nome)
    
    #Player._atributos.listar_atributos(Player._nome)

    
    # print('\n' + Player._inventario.verificar_armamentos_no_inventario(Player._nome) + '\n')    
    # print(Player._equipamentos.equipar(Player.nome))
    # print(Player.atacar(Player.nome))


if __name__ == '__main__':
    main()