import os
from models.personagem import Personagem

ADICIONAR = True
REMOVER = False


def main():
    os.system('cls')

    Player = Personagem('Jogador', True)

    # Player._atributos.adicionar_remover_ponto_atributo(Player._nome, 'forca', 3, ADICIONAR)
    # Player._atributos.adicionar_remover_ponto_atributo(Player._nome, 'inteligencia', 2, ADICIONAR)
    # Player._atributos.adicionar_remover_ponto_atributo(Player._nome, 'vitalidade', 5, ADICIONAR)

    # Player._atributos.adicionar_remover_ponto_atributo(Player._nome, 'vitalidade', 2, REMOVER)

    # print(Player._atributos.listar_atributos(Player._nome))
    
    # print('\n' + Player._inventario.verificar_armamentos_no_inventario(Player._nome) + '\n')    
    print(Player._equipamentos.equipar(Player._nome))
    print(Player.atacar(Player._nome))
    
    # print(Player._equipamentos.verificar_equipamentos(Player._nome) + '\n')    
    # print('\n' + Player._inventario.verificar_armamentos_no_inventario(Player._nome) + '\n')

    # Player._equipamentos.equipar(Player._nome)

    # print('\nDepois de equipar o escudo\n')
    # print(Player._equipamentos.verificar_equipamentos(Player._nome) + '\n')  
    # print('\n' + Player._inventario.verificar_armamentos_no_inventario(Player._nome) + '\n')

    # print('\nAntes de equipar a arma de 2 mãos\n')
    # Player._equipamentos.equipar(Player._nome)


if __name__ == '__main__':
    main()