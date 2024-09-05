import msvcrt
from models.constantes import ATACAR, USAR_ITEM, USAR_MAGIA, FOGO, CURA, RESTAURAR
import os

#FRASES DE PARTES DO JOGO
INICIANDO_RPG = ('**********************\n'+'Iniciando Jogo de RPG\n'+'**********************\n')

def esperar_jogador():
    print('Aperte qualquer tecla para continuar!')
    msvcrt.getch()

def while_acao(texto_info, texto_input, nro_maximo, acao_inicial = False):
    while True:
        try:
            print(texto_info)
            opcao_selecionada = int(input(texto_input))
            if opcao_selecionada == 4 and not acao_inicial:
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


def escolher_acao(hp_atual, hp_max, mp_atual, mp_max, xp_atual, xp_level_up):
    os.system('cls')                
    print(f'Vida: {hp_atual} / {hp_max}')
    print(f'Mana: {mp_atual} / {mp_max}')
    print(f'XP: {xp_atual} / {xp_level_up}\n')

    texto_info = ('Possíveis ações:'
            +'1 - Atacar o inimigo\n'
            +'2 - Usar uma magia\n'
            +'3 - Usar um item\n')
    texto_input = 'Qual ação deseja realizar?\n::: '

    acao = while_acao(texto_info, texto_input, 3, True)

    if acao == 1:
        return ATACAR
    elif acao == 2:
        return USAR_MAGIA
    else:
        return USAR_ITEM 

def retornar_usar_magias(mana_player, hp_atual, hp_max, mp_atual, mp_max, xp_atual, xp_level_up):
    os.system('cls') 
    print(f'Vida: {hp_atual} / {hp_max}')
    print(f'Mana: {mp_atual} / {mp_max}')
    print(f'XP: {xp_atual} / {xp_level_up}\n')

    if mana_player < 5:
        print('Não é possível utilizar nenhuma magia com a quantidade de mana atual!')
        esperar_jogador()
        return ''
    
    texto_input = 'Escolha a magia que deseja usar:'
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


def retornar_usar_pocao(qtd_potion, qtd_hipotion, qtd_manapotion, hp_atual, hp_max, mp_atual, mp_max, xp_atual, xp_level_up):
    os.system('cls') 
    print(f'Vida: {hp_atual} / {hp_max}')
    print(f'Mana: {mp_atual} / {mp_max}')
    print(f'XP: {xp_atual} / {xp_level_up}\n')

    if qtd_potion == 0 and qtd_hipotion == 0 and qtd_manapotion == 0:
        return ''
    
    texto_input = 'Selecione qual item deseta usar!\n'
    texto_info = []

    if qtd_potion > 0:
        texto_info.append('1 - Usar Potion. Restaura 30 pontos de HP')
    
    if qtd_hipotion > 1:
        texto_info.append('2 - Usar Hi Potion. Restaura 80 pontos de HP')

    if qtd_manapotion > 0:
        texto_info.append('3 - Usar Mana Potion. Restaura 50 pontos de MP')
    
    opc = while_acao(texto_info, texto_input)
    
    if opc == 4:
        return ''
    else:
        return opc