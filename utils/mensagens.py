import msvcrt
from models.constantes import ATACAR, USAR_ITEM, USAR_MAGIA, FOGO, CURA, RESTAURAR
import os

#FRASES DE PARTES DO JOGO
INICIANDO_RPG = ('**********************\n'+'Iniciando Jogo de RPG\n'+'**********************\n')

def esperar_jogador():
    print('Aperte qualquer tecla para continuar!')
    msvcrt.getch()



def while_acao(texto_info, texto_input, nro_maximo, acao_inicial = False, escolher_itens = False, qtd_potion = 0, qtd_hipotion = 0, qtd_manapotion = 0):
    while True:
        try:
            if escolher_itens:
                if qtd_potion > 0 and qtd_hipotion > 0 and qtd_manapotion > 0:
                    print ('1 - Usar Potion. Restaura 30 pontos de HP\n'
                           '2 - Usar Hi Potion. Restaura 80 pontos de HP\n'
                           '3 - Usar Mana Potion. Restaura 50 pontos de MP\n'
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
                    print('1 - Usar Potion. Restaura 30 pontos de HP\n'
                          '2 - Usar Hi Potion. Restaura 80 pontos de HP\n'
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
                    print('1 - Usar Potion. Restaura 30 pontos de HP\n'
                          '3 - Usar Mana Potion. Restaura 50 pontos de MP\n'
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
                    print('1 - Usar Potion. Restaura 30 pontos de HP\n'
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
                    print('2 - Usar Hi Potion. Restaura 80 pontos de HP\n'
                          '3 - Usar Mana Potion. Restaura 50 pontos de MP\n'
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
                    print('2 - Usar Hi Potion. Restaura 80 pontos de HP\n'
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
                    print('3 - Usar Mana Potion. Restaura 50 pontos de MP\n'
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
                if opcao_selecionada == 4 and not acao_inicial:
                    break
                elif 0 < opcao_selecionada <= nro_maximo:
                    break
                else:
                    print('Opção inválida!\n')
        except ValueError:
            print('Entrada inválida! Por favor, digite um número\n')
        except KeyError:
            print('Item não encontrado para a opção escolhida\n')
   
    return opcao_selecionada


def escolher_acao(hp_atual, hp_max, mp_atual, mp_max, xp_atual, xp_level_up):
    os.system('cls')                
    print(f'Vida: {hp_atual} / {hp_max}')
    print(f'Mana: {mp_atual} / {mp_max}')
    print(f'XP: {xp_atual} / {xp_level_up}\n')

    texto_info = ('Possíveis ações:\n'
                  '1 - Atacar o inimigo\n'
                  '2 - Usar uma magia\n'
                  '3 - Usar um item\n')
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
    
    texto_input = 'Escolha a magia que deseja usar\n::: '
    if mana_player > 70:
        texto_info = ('Magia(s) disponível!\n'
                      '1 - Fire\n'
                      '2 - Cure\n'
                      '3 - Restore\n'
                      '4 - Voltar')
        opc = while_acao(texto_info, texto_input, 3)

    elif 20 > mana_player > 70:
        texto_info = ('Magia(s) disponível!\n'
                     '1 - Fire\n'
                     '2 - Cure\n'
                     '4 - Voltar')
        opc = while_acao(texto_info, texto_input, 2)
    else:
        texto_info = ('Magia(s) disponível!\n'
                     '1 - Fire\n'
                     '4 - Voltar')
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
        print('Não possui nenhuma poção disponível!')
        esperar_jogador()
        return ''
    
    texto_input = 'Selecione qual item deseta usar!\n'
    opc = while_acao('', texto_input, 0, False, True, qtd_potion, qtd_hipotion, qtd_manapotion)
    
    if opc == 4:
        return ''
    else:
        return opc