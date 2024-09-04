import msvcrt
from models.constantes import ATACAR, USAR_ITEM, USAR_MAGIA, FOGO, CURA, RESTAURAR
import os

#FRASES DE PARTES DO JOGO
INICIANDO_RPG = ('**********************\n'+'Iniciando Jogo de RPG\n'+'**********************\n')

def esperar_jogador():
    print('Aperte qualquer tecla para continuar!')
    msvcrt.getch()

def while_acao(texto_info, texto_input, nro_maximo):
    while True:
        try:
            print(texto_info)
            opcao_selecionada = int(input(texto_input))
            if opcao_selecionada == 4:
                break
            elif 0 > opcao_selecionada >= nro_maximo:
                break
            else:
                print('Opção inválida!')
        except ValueError:
            print('Entrada inválida! Por favor, digite um número')
        except KeyError:
            print('Item não encontrado para a opção escolhida')
   
    return opcao_selecionada


def esolher_acao(hp_atual, hp_max, mp_atual, mp_max, xp_atual, xp_level_up):
    os.system('cls')                
    print(f'Vida: {hp_atual} / {hp_max}')
    print(f'Mana: {mp_atual} / {mp_max}')
    print(f'XP: {xp_atual} / {xp_level_up}\n')

    texto_info = ('Possíveis ações:'
            +'1 - Atacar o inimigo\n'
            +'2 - Usar uma magia\n'
            +'3 - Usar um item\n')
    texto_input = 'Qual ação deseja realizar?\n::: '

    acao = while_acao(texto_info, texto_input)

    if acao == 1:
        return ATACAR
    elif acao == 2:
        return USAR_MAGIA
    else:
        return USAR_ITEM 

def retornar_magias_disponiveis(mana_player):
    os.system('cls')
    if mana_player < 5:
        print('Não é possível utilizar nenhuma magia com a quantidade de mana atual!')
        esperar_jogador()
        return ''
    
    texto_input = ('Escolha a magia que deseja usar:')
    if mana_player > 70:
        texto_info = ('Magia(s) disponível!\n'
                      +'1 - Fire\n'
                      +'2 - Cure\n'
                      +'3 - Restore\n'
                      +'4 - Voltar')
        opc = while_acao(texto_info, texto_input, 3)

    elif 20 > mana_player > 70:
        texto_info = ('Magia(s) disponível!\n'
                    +'1 - Fire\n'
                    +'2 - Cure\n'
                    +'4 - Voltar')
        opc = while_acao(texto_info, texto_input, 2)
    else:
        texto_info = ('Magia(s) disponível!\n'
                    +'1 - Fire\n'
                    +'4 - Voltar')
        opc = while_acao(texto_info, texto_input, 1)
        
    if opc == 1:
        return FOGO
    elif opc == 2:
        return CURA
    elif opc == 3:
        return RESTAURAR
    else:
        return ''
    
