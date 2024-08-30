from models.atributos import Atributos
from models.itens import Itens
from models.magias import Magias
from models.equipamentos import Equipamentos

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

    def __str__(self):
        return f'{self._nome}'

    def atacar(self, nome_personagem):
        cod = self._equipamentos.retornar_arma_escudo(nome_personagem, 'arma')
        min = Itens._itens[nome_personagem][cod]['dano_min']
        max = Itens._itens[nome_personagem][cod]['dano_max']

        # min calculos -> forca
        # max calculos -> forca

        # dano_causado >= min e <= max

        return f'{min} - {max}'

    def usar_magia(self, nome_personagem, self_enemy: bool):
        pass