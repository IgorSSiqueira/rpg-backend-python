import random
from models.atributos import Atributos
from models.itens import Itens
from models.magias import Magias
from models.equipamentos import Equipamentos
from models.constantes import ARMA, DEFESA, FORCA, INTELIGENCIA, VITALIDADE, ESCUDO, USAR_ITEM, ATACAR, USAR_MAGIA, QTD_PONTOS_ATRIBUTOS, PONTOS_LEVEL_UP, FOGO, CURA, INIMIGO_MORREU, BATALHA_CONTINUA, PLAYER_MORREU
from utils.mensagens import esperar_jogador, escolher_acao, retornar_usar_magias
import os

class Personagem:
    personagens = []

    def __init__(self, nome, player:bool, level = 1, cod_arma_inimigo = 4):
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
            self._magias = Magias()
            self._equipamentos = Equipamentos(nome)
            self._inventario = Itens(nome)  
            self._atributos = Atributos(nome)   
        else:
            self._level = level
            self.HPmax = 40 * level
            self.HP = self.HPmax
            self.XP = 10 + (10 * round(level * 1.2))
            self.dano_base = random.randint(level, (level * 7))
            self.defesa_base = random.randint(level, (level * 4))
            self.cod_arma = cod_arma_inimigo

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
                    self.update_dados(nome_personagem, True)
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

    # def informacoes_batalha(self, nome_personagem):
    #     os.system('cls')
    #     for jogador in Personagem.personagens:
    #         if jogador.nome == nome_personagem:                
    #             print(f'Vida: {self.HP} / {self.HPmax}')
    #             print(f'Mana: {self.MP} / {self.MPmax}')
    #             print(f'XP: {self.XP} / {self.XPup}')


    def acao_turno(self, nome_player, nome_inimigo):  
        dano_causado_player = 0      
        defesa_inimigo = 0

        for player in Personagem.personagens:
            if player.nome == nome_player: 
                acao_turno = escolher_acao(player.HP,player.HPmax, player.MP, player.MPmax, player.XP, player.XPup)
                
                if acao_turno == ATACAR:
                    cod_arma_player = self._equipamentos.retornar_arma_escudo(nome_player, ARMA)            
                    dano_min_player = Itens._itens[nome_player][cod_arma_player]['dano_min']
                    dano_max_player = Itens._itens[nome_player][cod_arma_player]['dano_max']

                    str_player = self._atributos.retornar_atributo(nome_player, FORCA)
                    dano_causado_player = random.randint(dano_min_player, dano_max_player) + (str_player * 3)            
                
                elif acao_turno == USAR_MAGIA:
                    if player.MP > 5:
                        opc_magia = retornar_usar_magias(player.MP, player.HP,player.HPmax, player.MP, player.MPmax, player.XP, player.XPup)
                        if opc_magia == '':
                            return ''
                    
                    if opc_magia == FOGO:
                        dano_causado_player = self._magias.magia_ataque(opc_magia, self._atributos.retornar_atributo(nome_player, INTELIGENCIA))               
                    else: 
                        if opc_magia == CURA:
                            player.HP += player._magias.cure(player.HPmax, self._atributos.retornar_atributo(nome_player, INTELIGENCIA))
                            if player.HP > player.HPmax:
                                player.HP = player.HPmax
                        else:
                            player.HP = player._magias.restore(player.HPmax)

                if acao_turno == USAR_ITEM:
                    cod_pocao = self._inventario.verificar_usar_pocao(player.nome, player.HP, player.HPmax, player.MP, player.MPmax, player.XP, player.XPup)

                    if cod_pocao == '':
                        return ''
                    
                    self._inventario.usar_pocao(player.nome, cod_pocao)
                    
                    if cod_pocao == 1 or cod_pocao == 2:
                        print(f'{player.nome} utilizou uma poção de cura, que restaura 30 pontos de HP!')
                        player.HP += Itens._itens[nome_player][cod_pocao]['cura']
                        if player.HP > player.HPmax:
                            player.HP = player.HPmax

                        print(f'{player.nome} está agora com {player.HP}/{player.HPmax} pontos de HP!')
                    else:
                        print(f'{player.nome} utilizou uma poção de cura, que restaura 80 pontos de HP!\n')
                        player.MP += Itens._itens[nome_player][cod_pocao]['cura']
                        if player.MP > player.MPmax:
                            player.MP = player.MPmax
                        
                        print(f'{player.nome} está agora com {player.HP}/{player.HPmax} pontos de HP!\n')

                for inimigo in Personagem.personagens:
                    if inimigo.nome == nome_inimigo:
                        dano_min_inimigo = Itens._itens[nome_player][inimigo.cod_arma]['dano_min']
                        dano_max_inimigo = Itens._itens[nome_player][inimigo.cod_arma]['dano_max'] 
                        dano_causado_inimigo = random.randint(dano_min_inimigo, dano_max_inimigo) + (inimigo.dano_base)
                        defesa_player = self._atributos.retornar_atributo(nome_player, DEFESA)
                        dano_causado_inimigo -= defesa_player  
                        defesa_inimigo = inimigo.defesa_base

                        if not acao_turno == USAR_ITEM:
                            dano_causado_player -= defesa_inimigo
                            print(f'{inimigo.nome} perdeu {dano_causado_player} pontos de vida!')
                            inimigo.HP -= dano_causado_player

                        #INIMIGO MORREU
                        if inimigo.HP <= 0:
                            print(f'{inimigo.nome} morreu. Você ganhou {inimigo.XP} de experiência!\n')                 
                            player.XP += inimigo.XP 

                            # *****************************************
                            # *****************************************
                            #
                            # FAZER FUNÇÃO PARA DROP DE ITENS DO INMIGO
                            #
                            # *****************************************
                            # *****************************************

                            if player.XP >= player.XPup:
                                #PASSOU LEVEL
                                print(f'Parabéns, você subiu para o level {player._level + 1}\n')
                                self.passou_level(nome_player)
                                player.HP = player.HPmax
                                player.MP = player.MPmax
                                # *****************************************
                                # *****************************************
                                # VERIFICAR CONTINUAÇÃO
                                # *****************************************
                                # *****************************************
                            
                            return INIMIGO_MORREU

                        else:
                            print(f'{inimigo.nome} está com {inimigo.HP} pontos de vida!')
                           
                            #INIMIGO ATACA
                            player.HP -= dano_causado_inimigo
                            print(f'{player.nome} perdeu {dano_causado_inimigo} pontos de vida!\n')
                            esperar_jogador()

                            if player.HP <= 0:
                                return PLAYER_MORREU
                            
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

    def update_dados(self, nome_personagem, first_update = False):
        str = 0
        int = 0
        def_escudo = 0
        cod_arma = self._equipamentos.retornar_arma_escudo(nome_personagem, ARMA)

        tipo_str_int = Itens._itens[nome_personagem][cod_arma]['tipo_bonus']
        bonus_str_int = Itens._itens[nome_personagem][cod_arma]['bonus']

        cod_escudo = self._equipamentos.retornar_arma_escudo(nome_personagem, ESCUDO)
        if cod_escudo != 0:
            def_escudo = Itens._itens[nome_personagem][cod_escudo]['bonus']        
        
        if tipo_str_int == 'str':
            str = bonus_str_int
        else:
            int = bonus_str_int
        
        vit = self._atributos.retornar_atributo(nome_personagem, VITALIDADE)

        for personagem in self.personagens:
            if personagem.nome == nome_personagem:
                personagem._atributos.adicionar_remover_ponto_atributo(nome_personagem, INTELIGENCIA, True, int)
                personagem._atributos.adicionar_remover_ponto_atributo(nome_personagem, FORCA, True, str)
                personagem._atributos.adicionar_remover_ponto_atributo(nome_personagem, DEFESA, True, def_escudo)

                personagem.HPmax = 100 + (personagem._level * 25) + (str * 2) + (vit * 10)
                personagem.MPmax = 80 + (personagem._level * 15) + (int * 10)
                
                if personagem.HP > personagem.HPmax:
                    personagem.HP = personagem.HPmax

                if personagem.MP > personagem.MPmax:
                    personagem.MP = personagem.MPmax

                if first_update:
                    personagem.HP = personagem.HPmax
                    personagem.MP = personagem.MPmax

    def passou_level(self, nome_personagem):
        for player in Personagem.personagens:
            if player.nome == nome_personagem:
                player._level += 1
                player.XP = 0
                player.XPup = (30 * player._level * 1.4)

        self.while_incluir_atributos(nome_personagem, PONTOS_LEVEL_UP)
        self.update_dados(nome_personagem)