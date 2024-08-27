import os
from models.personagem import Personagem

Player = Personagem('Jogador', True)

def main():
    os.system('cls')
    print('\n' + Player._inventario.verificar_armamentos(Player._nome) + '\n')
    pass

if __name__ == '__main__':
    main()