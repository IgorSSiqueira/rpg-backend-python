import random
from models.atributos import Atributos
from models.itens import Itens
from models.magias import Magias
from models.equipamentos import Equipamentos
from utils.constantes import ARMA, DEFESA, FORCA, INTELIGENCIA, VITALIDADE, ESCUDO, USAR_ITEM, ATACAR, USAR_MAGIA, QTD_PONTOS_ATRIBUTOS, PONTOS_LEVEL_UP, FOGO, CURA, INIMIGO_MORREU, BATALHA_CONTINUA, PLAYER_MORREU, PROCURAR_INIMIGO, USAR_MAGIA_ANTES_BATALHA, OLHAR_INVENTARIO, TROCAR_EQUIPAMENTO, AREA_PROXIMA, AREA_ANTERIOR, RESTAURAR, VERIFICAR_ATRIBUTOS, FORCA_EQUIPAMENTO, DEFESA_EQUIPAMENTO, INTELIGENCIA_EQUIPAMENTO, ADICIONAR, GUERREIRO, MAGO, FUGIR, REGEN
from utils.mensagens import esperar_jogador, escolher_acao, retornar_usar_magias, escolhas_acao_antes_batalha
import os

class Personagem:
    personagens = []

    def __init__(self, nome, player:bool, level = 1, cod_arma_inimigo = 4, gold_drop = 0, is_boss = False, cod_drop = 0, classe = ''):
        self._nome = nome 
        self._player = player   
        
        if player:
            self._level = 1
            self.HPmax = 100
            self.HP = self.HPmax
            self.MPmax = 80
            self.MP = self.MPmax
            self.XP = 0
            self.XPup = 30
            self.gold = 0
            self.area_atual = 1
            self.classe = classe
            self.regen = 0
            self._magias = Magias()
            self._equipamentos = Equipamentos(nome)
            self._inventario = Itens(nome)  
            self._atributos = Atributos(nome)   
        else:
            self._level = level
            self.HPmax = int(((60 * level) * 3) if is_boss else (60 * level))
            self.HP = self.HPmax
            # self.XP = int((20 + (20 * round(level * 1.8))) * 1.5) if is_boss else int((10 + (10 * round(level * 1.2))) * 1.5)
            self.XP = int((20 + (20 * round(level * 1.8))) * 8) if is_boss else int((10 + (10 * round(level * 1.2))) * 4)
            self.dano_base = (random.randint(level * 3, (level * 7)) * 4) if is_boss else (random.randint(level * 3, (level * 7)))
            self.defesa_base = (int(random.randint(level, (level * 4)) * 1.5)) if is_boss else (random.randint(level, (level * 4)))
            self.cod_arma = cod_arma_inimigo
            self.gold_drop = gold_drop
            self.is_boss = is_boss
            self.cod_drop = cod_drop

        Personagem.personagens.append(self)

    @property
    def nome(self):
        return self._nome
    
    def while_incluir_atributos(self, nome_personagem, qtd_pontos):
        while qtd_pontos > 0:
            os.system('cls')
            try:
                print(f'Você possui {qtd_pontos} de pontos de atributo para distribuir\n')  
                self._atributos.selecao_atributo()
                opc = int(input('Informe qual atributo deseja incluir 1 ponto: '))
                if opc > 0 and opc < 5:
                    if opc == 1:
                        self._atributos.adicionar_remover_ponto_atributo(nome_personagem, FORCA, True)
                    elif opc == 2:
                        self._atributos.adicionar_remover_ponto_atributo(nome_personagem, INTELIGENCIA, True)
                    elif opc == 3:
                        self._atributos.adicionar_remover_ponto_atributo(nome_personagem, VITALIDADE, True)
                    else:
                        self._atributos.adicionar_remover_ponto_atributo(nome_personagem, DEFESA, True)

                    qtd_pontos -= 1                    
                else:
                    print('Opção não existente')
            except ValueError:
                print('Entrada inválida! Por favor, digite um número')
            except KeyError:
                    print('Item não encontrado para a opção escolhida')

    def iniciar_rpg(self, nome_personagem):       
        print(f'Olá {nome_personagem}, seja bem vindo!!')
        esperar_jogador()    
        self.while_incluir_atributos(nome_personagem, QTD_PONTOS_ATRIBUTOS)        
        

        espada_ini = self._inventario._itens[nome_personagem][4]
        cetro_ini = self._inventario._itens[nome_personagem][5]

        os.system('cls')
        print('Escolha qual equipamento deseja iniciar a sua campanha!!')
        while True:
            try:
                opc_equip = int(input(f'{espada_ini['cod']} - {espada_ini['nome']} - Dano: {espada_ini['dano_min']} - {espada_ini['dano_max']} - {espada_ini['bonus']} pontos de bônus em {espada_ini['tipo_bonus']}\n'
                                     +f'{cetro_ini['cod']} - {cetro_ini['nome']} - Dano: {cetro_ini['dano_min']} - {cetro_ini['dano_max']} - {cetro_ini['bonus']} pontos de bônus em {cetro_ini['tipo_bonus']}\n::: '))
                if opc_equip >= 4 and opc_equip <= 5:
                    self._inventario.adicionar_item(nome_personagem, opc_equip)
                    self._equipamentos.equipar_primeiro_item(nome_personagem, opc_equip)
                    # self._inventario.adicionar_item(nome_personagem, 10)
                    # self._equipamentos.equipar_primeiro_item(nome_personagem, 10)
                    # self.adicionar_remover_atributos_equipamentos(nome_personagem, ARMA, ADICIONAR)
                    self.update_dados(nome_personagem)
                    break
                else:
                    print('\nOpção Inválida! Selecione uma opção válida\n')

            except ValueError:
                print('Entrada inválida! Por favor, digite um número')
            except KeyError:
                    print('Item não encontrado para a opção escolhida')
        
        self._inventario.adicionar_item(nome_personagem, 1, 5)
        self._inventario.adicionar_item(nome_personagem, 3, 2)
        esperar_jogador()

    def acao_antes_batalha(self, nome_player):
        for player in Personagem.personagens:
            if player.nome == nome_player: 
                acao_realizada = escolhas_acao_antes_batalha(player.area_atual, player.HP,player.HPmax, player.MP, player.MPmax, player.XP, player.XPup, player._level, player.gold)

                if acao_realizada == PROCURAR_INIMIGO:
                    return PROCURAR_INIMIGO

                elif acao_realizada == USAR_MAGIA_ANTES_BATALHA:
                    opc_magia = retornar_usar_magias(player.HP, player.HPmax, player.MP, player.MPmax, player.XP, player.XPup, player._level, player.gold, True)
                    
                    if opc_magia == '':
                            return ''
                    
                    
                    if opc_magia == CURA:
                        cura_recebida = player._magias.cure(player.HPmax, self._atributos.retornar_atributo(nome_player, INTELIGENCIA))
                        player.HP += cura_recebida
                        player.MP -= self._magias.custo_mana(CURA)
                        print(f'Restaurou {cura_recebida} de HP!')
                        if player.HP > player.HPmax:
                            player.HP = player.HPmax
                    else:
                        player.MP -= self._magias.custo_mana(RESTAURAR)
                        player.HP = player._magias.restore(player.HPmax)
                        print('Todo o HP foi restaurado!')
                    
                    esperar_jogador()
                    return ''
                
                elif acao_realizada == USAR_ITEM:
                    pocao_utilizada = self._inventario.verificar_usar_pocao(player.nome, player.HP, player.HPmax, player.MP, player.MPmax, player.XP, player.XPup)
                    if pocao_utilizada == '':
                        return ''
                    
                    self._inventario.usar_pocao(player.nome, pocao_utilizada)

                    if pocao_utilizada == 1 or pocao_utilizada == 2:
                        print(f'{player.nome} utilizou uma poção de cura, que restaura {Itens._itens[player.nome][pocao_utilizada]['cura']} pontos de HP!')
                        player.HP += Itens._itens[nome_player][pocao_utilizada]['cura']
                        if player.HP > player.HPmax:
                            player.HP = player.HPmax

                        print(f'{player.nome} está agora com {player.HP}/{player.HPmax} pontos de HP!')
                    else:
                        print(f'{player.nome} utilizou uma poção de cura, que restaura {Itens._itens[player.nome][pocao_utilizada]['cura']} pontos de MP!\n')
                        player.MP += Itens._itens[nome_player][pocao_utilizada]['cura']
                        if player.MP > player.MPmax:
                            player.MP = player.MPmax
                        
                        print(f'{player.nome} está agora com {player.MP}/{player.MPmax} pontos de MP!\n')
                    
                    esperar_jogador()
                    return ''
                
                elif acao_realizada == OLHAR_INVENTARIO:
                    armamentos_no_inventario = self._inventario.verificar_armamentos_no_inventario(player.nome)
                    if armamentos_no_inventario == 0:
                        print('Não possui nenhum equipamento no inventário!')
                    
                    print(armamentos_no_inventario)
                    esperar_jogador()
                    return ''

                elif acao_realizada == TROCAR_EQUIPAMENTO:
                    trocar_equipamento = self._inventario.verificar_armamentos_no_inventario(player.nome, True)
                    if trocar_equipamento == 0:
                        print('Não possui nenhum equipamento no inventário!')
                    else:
                        self.equipar(player.nome)
                    esperar_jogador()
                    return ''
                
                elif acao_realizada == VERIFICAR_ATRIBUTOS:
                    print(self._atributos.listar_atributos(player.nome))
                    esperar_jogador()

                elif acao_realizada == AREA_PROXIMA:
                    player.area_atual += 1
                    return AREA_PROXIMA
                    

                elif acao_realizada == AREA_ANTERIOR:
                    player.area_atual -= 1
                    return AREA_ANTERIOR

                
                

    def acao_turno(self, nome_player, nome_inimigo):  
        dano_causado_player = 0      
        defesa_inimigo = 0
        life_steal_player = False
        is_cure = False

        for player in Personagem.personagens:
            if player.nome == nome_player:
                for inimigo in Personagem.personagens:
                    if inimigo.nome == nome_inimigo:
                        acao_turno = escolher_acao(player.HP,player.HPmax, player.MP, player.MPmax, player.XP, player.XPup, inimigo.nome, inimigo.HP, player._level, inimigo._level, player.gold)
                
                        if acao_turno == FUGIR:
                            Personagem.personagens.remove(inimigo) 
                            return FUGIR

                        if acao_turno == ATACAR:
                            cod_arma_player = self._equipamentos.retornar_arma_escudo(nome_player, ARMA)      
                            life_steal_player = (cod_arma_player == 10)
                            dano_min_player = Itens._itens[nome_player][cod_arma_player]['dano_min']
                            dano_max_player = Itens._itens[nome_player][cod_arma_player]['dano_max']

                            str_player = self._atributos.retornar_atributo(nome_player, FORCA)
                            dano_causado_player = random.randint(dano_min_player, dano_max_player) + (str_player * 3)            
                        
                        elif acao_turno == USAR_MAGIA:
                            if player.MP > 5:
                                opc_magia = retornar_usar_magias(player.HP, player.HPmax, player.MP, player.MPmax, player.XP, player.XPup, player._level, player.gold)
                                if opc_magia == '':
                                    return ''
                            
                            inteligencia_total = self._atributos.retornar_atributo(nome_player, INTELIGENCIA) + self._atributos.retornar_atributo(nome_player, INTELIGENCIA_EQUIPAMENTO)
                            
                            if opc_magia == FOGO:
                                player.MP -= self._magias.custo_mana(FOGO)
                                dano_causado_player = self._magias.magia_ataque(opc_magia, inteligencia_total, player._level)               
                            
                            else: 
                                if opc_magia == CURA:
                                    curou = self._magias.cure(player.HPmax, inteligencia_total)
                                    player.HP += curou
                                    player.MP -= self._magias.custo_mana(CURA)
                                    if player.HP > player.HPmax:
                                        player.HP = player.HPmax
                                    print(f'Restaurou {curou} de HP!')

                                elif opc_magia == REGEN:
                                    player.regen = player._magias.regen(player.HPmax, inteligencia_total)
                                    player.MP -= self._magias.custo_mana(REGEN)
                                    
                                else:
                                    player.MP -= self._magias.custo_mana(RESTAURAR)
                                    player.HP = player._magias.restore(player.HPmax)
                                    print('Restaurou todo o HP!')
                                
                                is_cure = True

                        if acao_turno == USAR_ITEM:
                            cod_pocao = self._inventario.verificar_usar_pocao(player.nome, player.HP, player.HPmax, player.MP, player.MPmax, player.XP, player.XPup)

                            if cod_pocao == '':
                                return ''
                            
                            self._inventario.usar_pocao(player.nome, cod_pocao)
                            
                            if cod_pocao == 1 or cod_pocao == 2:
                                print(f'{player.nome} utilizou uma poção de cura, que restaura {Itens._itens[player.nome][cod_pocao]['cura']} pontos de HP!')
                                player.HP += Itens._itens[nome_player][cod_pocao]['cura']
                                if player.HP > player.HPmax:
                                    player.HP = player.HPmax

                                print(f'{player.nome} está agora com {player.HP}/{player.HPmax} pontos de HP!')
                            else:
                                print(f'{player.nome} utilizou uma poção de cura, que restaura {Itens._itens[player.nome][cod_pocao]['cura']} pontos de MP!\n')
                                player.MP += Itens._itens[nome_player][cod_pocao]['cura']
                                if player.MP > player.MPmax:
                                    player.MP = player.MPmax
                                
                                print(f'{player.nome} está agora com {player.MP}/{player.MPmax} pontos de MP!\n')
                                
                        dano_min_inimigo = Itens._itens[nome_player][inimigo.cod_arma]['dano_min']
                        dano_max_inimigo = Itens._itens[nome_player][inimigo.cod_arma]['dano_max'] 
                        dano_causado_inimigo = random.randint(dano_min_inimigo, dano_max_inimigo) + (inimigo.dano_base)
                        
                        defesa_player = self._atributos.retornar_atributo(nome_player, DEFESA) + self._atributos.retornar_atributo(nome_player, DEFESA_EQUIPAMENTO)
                        dano_causado_inimigo -= defesa_player  
                        defesa_inimigo = inimigo.defesa_base

                        if not (acao_turno == USAR_ITEM) and not is_cure:
                            dano_causado_player -= defesa_inimigo
                            print(f'\n{inimigo.nome} perdeu {dano_causado_player} pontos de vida!')
                            inimigo.HP -= dano_causado_player

                            if life_steal_player:
                                print(f'Player recuperou {dano_causado_player} pontos de vida!\n')
                                player.HP += dano_causado_player
                                if player.HP > player.HPmax:
                                    player.HP = player.HPmax

                        #INIMIGO MORREU
                        if inimigo.HP <= 0:
                            player.regen = 0
                            print(f'{inimigo.nome} morreu. Você ganhou {inimigo.XP} de experiência!\n')                 
                            player.XP += inimigo.XP 

                            player.gold = inimigo.gold_drop

                            if random.randint(1, 100) <= self._inventario._itens[player.nome][1]['drop_chance']:
                                print(f'Inimigo dropou {self._inventario._itens[player.nome][1]['nome']}')
                                player._inventario.adicionar_item(player.nome, 1)
                                                
                            if inimigo._level > 4:
                                if random.randint(1, 100) <= self._inventario._itens[player.nome][2]['drop_chance']:
                                    print(f'Inimigo dropou {self._inventario._itens[player.nome][2]['nome']}')
                                    player._inventario.adicionar_item(player.nome, 2)
                    
                            if random.randint(1, 100) <= self._inventario._itens[player.nome][3]['drop_chance']:
                                print(f'Inimigo dropou {self._inventario._itens[player.nome][3]['nome']}')
                                player._inventario.adicionar_item(player.nome, 3)
                    
                            if random.randint(1, 100) <= (self._inventario._itens[player.nome][inimigo.cod_drop]['drop_chance'] * 5 if inimigo.is_boss else self._inventario._itens[player.nome][inimigo.cod_drop]['drop_chance']):
                                if inimigo.nome == 'Gigante' and player.classe == GUERREIRO:
                                    print(f'Inimigo dropou {self._inventario._itens[player.nome][inimigo.cod_drop]['nome']}')
                                    player._inventario.adicionar_item(player.nome, inimigo.cod_drop) 
                                elif inimigo.nome == 'Gigante' and player.classe == MAGO:
                                    player._inventario.adicionar_item(player.nome, 8) 
                                else:
                                    player._inventario.adicionar_item(player.nome, inimigo.cod_drop)                                                    
                        
                            if player.XP >= player.XPup:
                                self.passou_level(nome_player)               

                            Personagem.personagens.remove(inimigo)   
                            esperar_jogador() 
                            return INIMIGO_MORREU            

                        else:
                            print(f'{inimigo.nome} está com {inimigo.HP} pontos de vida!\n')
                           
                            #INIMIGO ATACA
                            player.HP -= dano_causado_inimigo
                            print(f'O {inimigo.nome} te atacou de volta!\n{player.nome} perdeu {dano_causado_inimigo} pontos de vida!\n')
                            
                            if inimigo.cod_arma == 10:
                                print(f'{inimigo.nome} recuperou {dano_causado_inimigo} ponto de vida!\n')
                                inimigo.HP += dano_causado_inimigo
                                if inimigo.HP > inimigo.HPmax:
                                    inimigo.HP = inimigo.HPmax   
                            
                            if player.HP <= 0:
                                return PLAYER_MORREU
                            
                            if player.regen > 0:
                                print(f'{player.nome} recupera -> {player.regen} <- pontos de HP devido a magia de regeneração!')
                                player.HP += player.regen
                                if player.HP > player.HPmax:
                                    player.HP = player.HPmax

                            esperar_jogador()
                            return BATALHA_CONTINUA

    def equipar(self, nome_personagem):
        if self._equipamentos.equipar(nome_personagem):
            self.update_dados(nome_personagem)

    def listar_atributos(self, nome_personagem):
        self._atributos.listar_atributos(nome_personagem)

    def mostrar_hp_mp(self, nome_personagem):
        for personagem in Personagem.personagens:
            if personagem.nome == nome_personagem:
                print(f'{self.HP} / {self.HPmax}')
                print(f'{self.MP} / {self.MPmax}')

    def update_dados(self, nome_personagem):
        str = self._atributos.retornar_atributo(nome_personagem, FORCA)
        str += self._atributos.retornar_atributo(nome_personagem, FORCA_EQUIPAMENTO)

        int = self._atributos.retornar_atributo(nome_personagem, INTELIGENCIA)
        int += self._atributos.retornar_atributo(nome_personagem, INTELIGENCIA_EQUIPAMENTO)

        vit = self._atributos.retornar_atributo(nome_personagem, VITALIDADE)

        for personagem in self.personagens:
            if personagem.nome == nome_personagem:

                if personagem.classe == GUERREIRO:
                    personagem.HPmax = 120 + (str * 5) + (vit * 20)
                    personagem.MPmax = 70 + (int * 5)
                
                elif personagem.classe == MAGO:
                    personagem.HPmax = 100 + (str * 2) + (vit * 10)
                    personagem.MPmax = 90 + (int * 10)

                personagem.HP = personagem.HPmax
                personagem.MP = personagem.MPmax
                
                if personagem.HP > personagem.HPmax:
                    personagem.HP = personagem.HPmax

                if personagem.MP > personagem.MPmax:
                    personagem.MP = personagem.MPmax

    def passou_level(self, nome_personagem):
        for player in Personagem.personagens:
            if player.nome == nome_personagem:
                print(f'Parabéns, você subiu para o level {player._level + 1}\n')
                esperar_jogador()
                XPRestante = player.XP - player.XPup
                player._level += 1
                player.XP = 0
                player.XPup = int (30 * player._level * 1.4)

                self._atributos.adicionar_remover_ponto_atributo(player.nome, FORCA, ADICIONAR)
                self._atributos.adicionar_remover_ponto_atributo(player.nome, INTELIGENCIA, ADICIONAR)
                self._atributos.adicionar_remover_ponto_atributo(player.nome, DEFESA, ADICIONAR)
                self._atributos.adicionar_remover_ponto_atributo(player.nome, VITALIDADE, ADICIONAR)
                
                self.while_incluir_atributos(nome_personagem, PONTOS_LEVEL_UP)
                self.update_dados(nome_personagem)

                player.XP = XPRestante
                if player.XP >= player.XPup:
                    self.passou_level(player.nome)
                    
        

    def adicionar_remover_atributos_equipamentos(self, nome_personagem, arma_escudo, adicionar_remover = bool):    
        for personagem in self.personagens:
            if personagem.nome == nome_personagem:
                if arma_escudo == ESCUDO:
                    cod_escudo = self._equipamentos.retornar_arma_escudo(nome_personagem, arma_escudo) 
                    if cod_escudo != 0:
                        def_escudo = Itens._itens[nome_personagem][cod_escudo]['bonus']        
                        personagem._atributos.adicionar_remover_ponto_atributo(nome_personagem, DEFESA, adicionar_remover, def_escudo)
                else: 
                    cod_arma = self._equipamentos.retornar_arma_escudo(nome_personagem, arma_escudo)
                    tipo_str_int = Itens._itens[nome_personagem][cod_arma]['tipo_bonus']
                    bonus_str_int = Itens._itens[nome_personagem][cod_arma]['bonus']
                 
                    if tipo_str_int == 'str':
                        personagem._atributos.adicionar_remover_ponto_atributo(nome_personagem, FORCA, adicionar_remover, bonus_str_int)
                    else:
                        personagem._atributos.adicionar_remover_ponto_atributo(nome_personagem, INTELIGENCIA, adicionar_remover, bonus_str_int)