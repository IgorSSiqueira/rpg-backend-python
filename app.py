import os
from models.personagem import Personagem



def main():
    os.system('cls')
    Player = Personagem('Jogador', True)
    # print('\n' + Player._inventario.verificar_armamentos(Player._nome) + '\n')
    Player._equipamentos.equipar(Player._nome)
    print(Player._equipamentos.verifica_equipamentos(Player._nome) + '\n')
    print('\n' + Player._inventario.verificar_armamentos(Player._nome) + '\n')
    pass

if __name__ == '__main__':
    main()