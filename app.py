import os
from models.personagem import Personagem



def main():
    os.system('cls')

    Player = Personagem('Jogador', True)
    
    print('\n' + Player._inventario.verificar_armamentos_no_inventario(Player._nome) + '\n')    
    Player._equipamentos.equipar(Player._nome)
    
    print(Player._equipamentos.verificar_equipamentos(Player._nome) + '\n')    
    print('\n' + Player._inventario.verificar_armamentos_no_inventario(Player._nome) + '\n')

    Player._equipamentos.equipar(Player._nome)

    print('\nDepois de equipar o escudo\n')
    print(Player._equipamentos.verificar_equipamentos(Player._nome) + '\n')  
    print('\n' + Player._inventario.verificar_armamentos_no_inventario(Player._nome) + '\n')

    print('\nAntes de equipar a arma de 2 mãos\n')
    Player._equipamentos.equipar(Player._nome)


if __name__ == '__main__':
    main()