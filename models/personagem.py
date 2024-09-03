import random
from models.atributos import Atributos
from models.itens import Itens
from models.magias import Magias
from models.equipamentos import Equipamentos
from models.constantes import ARMA, DEFESA, FORCA, INTELIGENCIA, VITALIDADE, ESCUDO, USAR_ITEM, ATACAR, USAR_MAGIA
import os

class Personagem:
    personagens = []

    def __init__(self, nome, player:bool, level = 1):
        self._nome = nome 
        self._player = player
        self._inventario = Itens(nome)  
        self._atributos = Atributos(nome)      
        
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
        else:
            self._level = level
            self.HPmax = 40 * level
            self.HP = self.HPmax
            self.XP = 10 + (10 * round(level/1.3))
            # self.dano = etc

        print(f'HP {nome} = {self.HP}')

        Personagem.personagens.append(self)

    @property
    def nome(self):
        return self._nome
    
    def iniciar_rpg(self, nome_personagem):
        qtd_atributo_inicial = 3
        while qtd_atributo_inicial > 0:
            os.system('cls')
            try:
                print(f'Você possui {qtd_atributo_inicial} de pontos de atributo para distribuir\n')  
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

                    qtd_atributo_inicial -= 1                    
                else:
                    print('Opção não existente')
            except ValueError:
                print('Entrada inválida! Por favor, digite um número')
            except KeyError:
                    print('Item não encontrado para a opção escolhida')

        espada_ini = self._inventario._itens[nome_personagem][4]
        cetro_ini = self._inventario._itens[nome_personagem][5]

        os.system('cls')
        print('Escolha qual equipamento deseja iniciar a sua campanha!!')
        while True:
            try:
                opc_equip = int(input(print(f'{espada_ini['cod']} - {espada_ini['nome']} - Dano: {espada_ini['dano_min']} - {espada_ini['dano_max']} - {espada_ini['bonus']} pontos de bônus em {espada_ini['tipo_bonus']}\n'
                                           +f'{cetro_ini['cod']} - {cetro_ini['nome']} - Dano: {cetro_ini['dano_min']} - {cetro_ini['dano_max']} - {cetro_ini['bonus']} pontos de bônus em {cetro_ini['tipo_bonus']}\n: ')))
                if opc_equip >= 4 and opc_equip <= 5:
                    self._inventario.adicionar_item(nome_personagem, opc_equip)
                    self._equipamentos.equipar_primeiro_item(nome_personagem, opc_equip)
                    self.update_dados(nome_personagem)
                    break
                else:
                    print('\nOpção Inválida! Selecione uma opção válida\n')

            except ValueError:
                print('Entrada inválida! Por favor, digite um número')
            except KeyError:
                    print('Item não encontrado para a opção escolhida')
                
    
    def usar_magia(self, nome_personagem, self_enemy: bool):
        pass

    def acao_turno(self, player, inimigo, acao, cod_item = 0, cod_magia = ''):  
        dano_causado_player = 0      
        defesa_inimigo = self._atributos.retornar_atributo(inimigo, DEFESA)

        if acao == ATACAR:
            cod_arma_player = self._equipamentos.retornar_arma_escudo(player, ARMA)
            dano_min_player = Itens._itens[player][cod_arma_player]['dano_min']
            dano_max_player = Itens._itens[player][cod_arma_player]['dano_max']

            str_player = self._atributos.retornar_atributo(player, FORCA)
            dano_causado_player = random.randint(dano_min_player, dano_max_player) + (str_player * 3)
            
            dano_causado_player -= defesa_inimigo
        
        elif acao == USAR_MAGIA:
            if cod_magia not in ['cure', 'restore']:
                dano_causado_player = self._magias.magia_ataque(cod_magia, self._atributos.retornar_atributo(player, INTELIGENCIA))
                dano_causado_player -= defesa_inimigo      
        

        cod_arma_inimigo = self._equipamentos.retornar_arma_escudo(player, ARMA)
        dano_min_inimigo = Itens._itens[player][cod_arma_inimigo]['dano_min']
        dano_max_inimigo = Itens._itens[player][cod_arma_inimigo]['dano_max']

        str_inimigo = self._atributos.retornar_atributo(player, FORCA)
        dano_causado_inimigo = random.randint(dano_min_inimigo, dano_max_inimigo) + (str_inimigo * 3)

        defesa_player = self._atributos.retornar_atributo(player, DEFESA)
        dano_causado_inimigo -= defesa_player        
        
        for player in Personagem.personagens:
            if player.nome == player:
                hp_player = player.HP
                xp_level_up = player.XPup
                xp_atual_player = player.XP

                if acao == USAR_ITEM:
                    player._inventario.usar_pocao(player.nome, cod_item)
                    
                    if cod_item == 1 or cod_item == 2:
                        player.HP += Itens._itens[player][cod_item]['cura']
                        if player.HP > player.HPmax:
                            player.HP = player.HPmax
                    else:
                        player.MP += Itens._itens[player][cod_item]['cura']
                        if player.MP > player.MPmax:
                            player.MP = player.MPmax
                
                elif acao == USAR_MAGIA and cod_magia in ['cure', 'restore']:
                    if cod_magia == 'cure':
                        player.HP += player._magias.cure(player.HPmax, self._atributos.retornar_atributo(player, INTELIGENCIA))
                        if player.HP > player.HPmax:
                            player.HP = player.HPmax
                    else:
                        player.HP = player._magias.restore(player.HPmax)

                for inimigo in Personagem.personagens:
                    if inimigo.nome == inimigo:
                        hp_inimigo = inimigo.HP
                        xp_inimigo = inimigo.XP    

                hp_inimigo -= dano_causado_player
                if hp_inimigo <= 0:
                    #inimigo morreu
                    xp_atual_player = xp_inimigo

                    if xp_atual_player >= xp_level_up:
                        #passou de level
                        pass
                    
                else:
                    #inimigo ataca
                    hp_player -= dano_causado_inimigo
                    pass

        
        return 0 

    def equipar(self, nome_personagem):
        if self._equipamentos.equipar(nome_personagem):
            self.update_dados(nome_personagem)

    def update_dados(self, nome_personagem):
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
                self.HPmax = 100 + (self._level * 25) + (str * 2) + (vit * 10)
                self.MPmax = 80 + (self._level * 15) + (int * 10)
                self._atributos.adicionar_remover_ponto_atributo(nome_personagem, INTELIGENCIA, True, int)
                self._atributos.adicionar_remover_ponto_atributo(nome_personagem, FORCA, True, str)
                self._atributos.adicionar_remover_ponto_atributo(nome_personagem, DEFESA, True, def_escudo)

    def final_batalha(self, nome_personagem, nome_inimigo):
        pass

    def passou_level(self, nome_personagem):
        for personagem in Personagem.personagens:
            if personagem.nome == nome_personagem:
                pass