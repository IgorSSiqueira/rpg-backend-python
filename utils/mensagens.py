import msvcrt
from utils.constantes import ATACAR, USAR_ITEM, USAR_MAGIA, FOGO, CURA, RESTAURAR, PROCURAR_INIMIGO, USAR_MAGIA_ANTES_BATALHA, OLHAR_INVENTARIO, TROCAR_EQUIPAMENTO, AREA_ANTERIOR, AREA_PROXIMA, VERIFICAR_ATRIBUTOS, POTION, HIPOTION, MANAPOTION, GUERREIRO, MAGO, FUGIR, REGEN
import os


#FRASES DE PARTES DO JOGO
INICIANDO_RPG = ('**********************\n'+'Iniciando Jogo de RPG\n'+'**********************\n')

def esperar_jogador():
    print('Aperte qualquer tecla para continuar!')
    msvcrt.getch()



def while_acao(texto_info, texto_input, nro_maximo, acao_inicial = False, escolher_itens = False, qtd_potion = 0, qtd_hipotion = 0, qtd_manapotion = 0, magia_cura_antes_batalha_while = False, nome_personagem = '', area_max = False, magia = False):
    while True:
        try:
            if escolher_itens:
                if qtd_potion > 0 and qtd_hipotion > 0 and qtd_manapotion > 0:
                    print (f'1 - Usar Potion. Restaura {POTION} pontos de HP (Possui {qtd_potion})\n'
                           f'2 - Usar Hi Potion. Restaura {HIPOTION} pontos de HP (Possui {qtd_hipotion})\n'
                           f'3 - Usar Mana Potion. Restaura {MANAPOTION} pontos de MP (Possui {qtd_manapotion})\n'
                           '4 - Voltar')
                    opcao_selecionada = int(input(texto_input))
                    if opcao_selecionada == 4:
                        break                    
                    if 0 < opcao_selecionada <= 3:
                        break
                    else:
                        print('Opção inválida!\n')
                        continue                      
                elif qtd_potion > 0 and qtd_hipotion > 0 and qtd_manapotion <= 0:
                    print(f'1 - Usar Potion. Restaura {POTION} pontos de HP (Possui {qtd_potion})\n'
                          f'2 - Usar Hi Potion. Restaura {HIPOTION} pontos de HP (Possui {qtd_hipotion})\n'
                          '4 - Voltar')
                    opcao_selecionada = int(input(texto_input))                    
                    if opcao_selecionada == 4:
                        break

                    if 0 < opcao_selecionada <= 2:
                        break
                    else:
                        print('Opção inválida!\n')
                        continue
                elif qtd_potion > 0 and qtd_hipotion <= 0 and qtd_manapotion > 0:
                    print(f'1 - Usar Potion. Restaura {POTION} pontos de HP (Possui {qtd_potion})\n'
                          f'3 - Usar Mana Potion. Restaura {MANAPOTION} pontos de MP (Possui {qtd_manapotion})\n'
                          '4 - Voltar')
                    opcao_selecionada = int(input(texto_input))                    
                    if opcao_selecionada == 4:
                        break

                    if opcao_selecionada == 1 or opcao_selecionada == 3:
                        break
                    else:
                        print('Opção inválida!\n')
                        continue                    
                elif qtd_potion > 0 and qtd_hipotion <= 0 and qtd_manapotion <= 0:
                    print(f'1 - Usar Potion. Restaura {POTION} pontos de HP (Possui {qtd_potion})\n'
                          '4 - Voltar')
                    opcao_selecionada = int(input(texto_input))
                    if opcao_selecionada == 4:
                        break
                    
                    if opcao_selecionada == 1:
                        break
                    else:
                        print('Opção inválida!\n')
                        continue                      
                elif qtd_potion <= 0 and qtd_hipotion > 0 and qtd_manapotion > 0:
                    print(f'2 - Usar Hi Potion. Restaura {HIPOTION} pontos de HP (Possui {qtd_hipotion})\n'
                          f'3 - Usar Mana Potion. Restaura {MANAPOTION} pontos de MP (Possui {qtd_manapotion})\n'
                          '4 - Voltar')
                    opcao_selecionada = int(input(texto_input))
                    if opcao_selecionada == 4:
                        break
                    
                    if 1 < opcao_selecionada <= 3:
                        break
                    else:
                        print('Opção inválida!\n')
                        continue                      
                elif qtd_potion <= 0 and qtd_hipotion > 0 and qtd_manapotion <= 0:
                    print(f'2 - Usar Hi Potion. Restaura {HIPOTION} pontos de HP (Possui {qtd_hipotion})\n'
                          '4 - Voltar')
                    opcao_selecionada = int(input(texto_input))
                    if opcao_selecionada == 4:
                        break                    
                    if opcao_selecionada == 2:
                        break
                    else:
                        print('Opção inválida!\n')
                        continue                      
                else: # qtd_potion <= 0 and qtd_hipotion <= 0 and qtd_manapotion > 0:
                    print(f'3 - Usar Mana Potion. Restaura {MANAPOTION} pontos de MP (Possui {qtd_manapotion})\n'
                          '4 - Voltar')
                    opcao_selecionada = int(input(texto_input))
                    if opcao_selecionada == 4:
                        break                    
                    if opcao_selecionada == 3:
                        break
                    else:
                        print('Opção inválida!\n')
                        continue                          
            else:
                print(texto_info)
                opcao_selecionada = int(input(texto_input))   

                if area_max and opcao_selecionada == 7:
                    print('Opção inválida!\n')
                    continue

                if opcao_selecionada == 4 and not acao_inicial and not magia:
                    break
                elif magia and opcao_selecionada == 5:
                    break
                elif magia_cura_antes_batalha_while:
                    if 1 < opcao_selecionada <= nro_maximo:
                        break
                    else:
                        print('Opção inválida!\n')
                        continue
                elif 0 < opcao_selecionada <= nro_maximo:
                    break
                else:
                    print('Opção inválida!\n')
                    continue
        except ValueError:
            print('Entrada inválida! Por favor, digite um número\n')
        except KeyError:
            print('Item não encontrado para a opção escolhida\n')
   
    return opcao_selecionada

def escolher_classe():
    os.system('cls')
    texto_info = ('Escolha a sua classe, entre guerreiro e mago\n'
                 +'O guerreiro começa com 145 pontos de HP, cada ponto de STR almenta 5 ponto de HP e cada ponto em VIT almenta 20 pontos de HP!\n'
                 +'Porém começa com 75 pontos de MP, cada ponto de INT almenta 5 ponto de MP!\n'
                 +'O mago começa com 112 pontos de HP, cada ponto de STR almenta 2 ponto de HP e cada ponto em VIT almenta 10 pontos de HP!\n'
                 +'Porém começa com 100 pontos de MP, cada ponto de INT almenta 10 ponto de MP!\n')
    texto_input = 'Selecione a classe desejada!\n1 - Guerreiro\n2 - Mago\n::: '

    escolha = while_acao(texto_info, texto_input, 2, True)

    if escolha == 1:
        return GUERREIRO
    else:
        return MAGO

def escolher_acao(hp_atual, hp_max, mp_atual, mp_max, xp_atual, xp_level_up, nome_inimigo, hp_inimigo, player_level, inimigo_level, player_gold):
    os.system('cls')                
    print(f'Vida: {hp_atual} / {hp_max} - Mana: {mp_atual} / {mp_max} --------- Gold: {player_gold}')
    print(f'Level: {player_level} ---- XP: {xp_atual} / {xp_level_up}\n')
    print(f'{nome_inimigo} - HP: {hp_inimigo} ---- Level: {inimigo_level}\n')

    texto_info = ('Possíveis ações:\n'
                  '1 - Atacar o inimigo\n'
                  '2 - Usar uma magia\n'
                  '3 - Usar um item\n'
                  '4 - Fugir da batalha')
    texto_input = 'Qual ação deseja realizar?\n::: '

    acao = while_acao(texto_info, texto_input, 4, True)

    if acao == 1:
        return ATACAR
    elif acao == 2:
        return USAR_MAGIA
    elif acao == 3:
        return USAR_ITEM 
    else:
        return FUGIR 

def retornar_usar_magias(hp_atual, hp_max, mp_atual, mp_max, xp_atual, xp_level_up, player_level, player_gold, magia_cura_antes_batalha = False):
    os.system('cls') 
    print(f'Vida: {hp_atual} / {hp_max} - Mana: {mp_atual} / {mp_max} --------- Gold: {player_gold}')
    print(f'Level: {player_level} ---- XP: {xp_atual} / {xp_level_up}\n')

    if mp_atual < 5:
        print('Não é possível utilizar nenhuma magia com a quantidade de mana atual!')
        esperar_jogador()
        return ''
    
    if magia_cura_antes_batalha and mp_atual < 20:
        print('\nNão é possível utilizar nenhuma magia de cura com a quantidade de mana atual!\n')
        esperar_jogador()
        return ''
    
    texto_input = 'Escolha a magia que deseja usar\n::: '
    if mp_atual > 150:
        texto_info = ('Magia(s) disponível!\n'
                      f"{'' if magia_cura_antes_batalha else '1 - Fire\n'}"
                      '2 - Cure\n'
                      '3 - Restore\n'
                      '4 - Regeneração\n'
                      '5 - Voltar')
        opc = while_acao(texto_info, texto_input, 4, magia_cura_antes_batalha_while = magia_cura_antes_batalha, magia=True)

    elif 90 < mp_atual < 150:
        texto_info = ('Magia(s) disponível!\n'
                      f"{'' if magia_cura_antes_batalha else '1 - Fire\n'}"
                      '2 - Cure\n'
                      '3 - Restore\n'
                      '5 - Voltar')
        opc = while_acao(texto_info, texto_input, 3, magia_cura_antes_batalha_while = magia_cura_antes_batalha, magia=True)

    elif 20 < mp_atual < 90:
        texto_info = ('Magia(s) disponível!\n'
                     f"{'' if magia_cura_antes_batalha else '1 - Fire\n'}"
                     '2 - Cure\n'
                     '5 - Voltar')
        opc = while_acao(texto_info, texto_input, 2, magia_cura_antes_batalha_while = magia_cura_antes_batalha, magia=True)
    else:
        texto_info = ('Magia(s) disponível!\n'
                     '1 - Fire\n'
                     '5 - Voltar')
        opc = while_acao(texto_info, texto_input, 1)
        
    if opc == 1:
        return FOGO
    elif opc == 2:
        return CURA
    elif opc == 3:
        return RESTAURAR
    elif opc == 4:
        return REGEN
    else:
        return ''


def retornar_usar_pocao(nome_personagem, qtd_potion, qtd_hipotion, qtd_manapotion, hp_atual, hp_max, mp_atual, mp_max, xp_atual, xp_level_up):
    os.system('cls') 
    print(f'Vida: {hp_atual} / {hp_max}')
    print(f'Mana: {mp_atual} / {mp_max}')
    print(f'XP: {xp_atual} / {xp_level_up}\n')

    if qtd_potion == 0 and qtd_hipotion == 0 and qtd_manapotion == 0:
        print('Não possui nenhuma poção disponível!')
        esperar_jogador()
        return ''
    
    texto_input = 'Selecione qual item deseta usar!\n'
    opc = while_acao('', texto_input, 0, False, True, qtd_potion, qtd_hipotion, qtd_manapotion, False, nome_personagem)
    
    if opc == 4:
        return ''
    else:
        return opc
    
def escolhas_acao_antes_batalha(area_atual, hp_atual, hp_max, mp_atual, mp_max, xp_atual, xp_level_up, player_level, player_gold):
    os.system('cls')                
    print(f'Vida: {hp_atual} / {hp_max} ---- Mana: {mp_atual} / {mp_max} --------- Gold: {player_gold}')
    print(f'Level: {player_level} ---- XP: {xp_atual} / {xp_level_up}\n')

    print('Selecione abaixo qual opção você deseja!\n'
          'Cuidado ao passar para a próxima área, fazendo isso você entrará diretamente em uma batalha!\n')

    opc_max = 7
    mensagem_voltar_area = ''
    mensagem_proxima_area = f'7 - Ir para próxima área e enfrentar um inimigo! (área: {area_atual+1})'

    if area_atual > 1:
        opc_max = 8
        mensagem_voltar_area = f'\n8 - Ir para área anterior e enfrentar um inimigo! (área: {area_atual-1})'
    
    if area_atual == 8:
        mensagem_proxima_area = ''

    texto_info = ('Possíveis ações:\n'
                  f'1 - Procurar um inimigo na área atual (área: {area_atual})\n'
                  '2 - Usar uma magia de cura\n'
                  '3 - Usar um item\n'
                  '4 - Olhar os equipamentos no inventário\n'
                  '5 - Selecionar equipamento para trocar\n'
                  '6 - Verificar atributos\n'
                  + mensagem_proxima_area
                  + mensagem_voltar_area)
                  #9 - SALVAR O JOGO

    texto_input = '\nQual ação deseja realizar?\n::: '

    acao = while_acao(texto_info, texto_input, opc_max)

    if acao == 1:
        return PROCURAR_INIMIGO
    elif acao == 2:
        return USAR_MAGIA_ANTES_BATALHA
    elif acao == 3:
        return USAR_ITEM 
    elif acao == 4:
        return OLHAR_INVENTARIO
    elif acao == 5:
        return TROCAR_EQUIPAMENTO
    elif acao == 6:
        return VERIFICAR_ATRIBUTOS
    elif acao == 7:
        return AREA_PROXIMA
    elif acao == 8:
        return AREA_ANTERIOR
    

    # acao = while_antes_batalha(texto_info, texto_input, 3, True)