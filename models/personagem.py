import random
from models.atributos import Atributos
from models.itens import Itens
from models.magias import Magias
from models.equipamentos import Equipamentos
from models.constantes import ARMA, DEFESA, FORCA, INTELIGENCIA, VITALIDADE#, ESCUDO
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
            self.HP = 100
            self.MPmax = 80
            self.MP = 80
            self.XP = 0
            self.XPup = 30
            self._magias = Magias()
            self._equipamentos = Equipamentos(nome)
        else:
            self._level = level
            self.HPmax = 40 * level
            self.HP = 40 * level
            self.XP = 10 + (10 * round(level/1.3))

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

    def atacar(self, atacante, defensor):
        cod_arma = self._equipamentos.retornar_arma_escudo(atacante, ARMA)
        min = Itens._itens[atacante][cod_arma]['dano_min']
        max = Itens._itens[atacante][cod_arma]['dano_max']

        str = self._atributos.retornar_atributo(atacante, FORCA)
        dano_causado = random.randint(min, max) + (str * 3)

        defesa = self._atributos.retornar_atributo(defensor, DEFESA)        
        cod_escudo = self._equipamentos.retornar_arma_escudo(defensor, DEFESA)        
        if cod_escudo:
            defesa += Itens._itens[defensor][cod_escudo]['bonus']

        # PRECISAMOS PENSAR EM UM JEITO BACANA DE RECEBER MENOS DANO
        # NÃO SEI SE DIMINUIR A DEFESA DIRETAMENTE FICARÁ LEGAL
        dano_causado -= defesa

        return dano_causado 

    def equipar(self, nome_personagem):
        if self._equipamentos.equipar(nome_personagem):
            self.update_dados(nome_personagem)


    #
    # Precisamos fazer um update nos dados do personagem 
    # sempre que forem adicionados novos atributos ou lvl up
    #
    def update_dados(self, nome_personagem):
        str = 0
        int = 0
        cod_arma = self._equipamentos.retornar_arma_escudo(nome_personagem, ARMA)

        print(f'arma: {cod_arma}')

        tipo_str_int = Itens._itens[nome_personagem][cod_arma]['tipo_bonus']
        bonus_str_int = Itens._itens[nome_personagem][cod_arma]['bonus']

        print(f'Tipo e bonus: {tipo_str_int} {bonus_str_int}')

        # cod_escudo = self._equipamentos.retornar_arma_escudo(nome_personagem, ESCUDO)
        # def_escudo = Itens._itens[nome_personagem][cod_escudo]['bonus']        
        
        if tipo_str_int == 'str':
            str = bonus_str_int
        else:
            print('entrou no else do atributo INT')
            int = bonus_str_int
        
        print(f'STR : {str} INT: {int}')

        vit = self._atributos.retornar_atributo(nome_personagem, VITALIDADE)

        for personagem in self.personagens:
            if personagem.nome == nome_personagem:
                print('entrou no for')
                self.HPmax = 100 + (self._level * 25) + (str * 2) + (vit * 10)
                self.MPmax = 80 + (self._level * 15) + (int * 10)
                self._atributos.adicionar_remover_ponto_atributo(nome_personagem, INTELIGENCIA, True, int)
                self._atributos.adicionar_remover_ponto_atributo(nome_personagem, FORCA, True, str)

    def passou_level(self, nome_personagem):
        for personagem in Personagem.personagens:
            if personagem.nome == nome_personagem:
                pass