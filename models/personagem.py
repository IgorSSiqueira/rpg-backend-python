from models.itens import Itens
# from models.magias import Magias
from models.equipamentos import Equipamentos

class Personagem:
    personagens = []

    def __init__(self, nome, player:bool, level = 1):
        self._nome = nome 
        self._player = player
        self._inventario = Itens(nome)        
        
        if player:
            self._level = 1
            self.HPmax = 100
            self.HP = 100
            self.MPmax = 80
            self.MP = 80
            self.XP = 0
            self.XPup = 30
            self._vitalidade = 1
            self._forca = 1
            self._inteligencia = 1
            # self._magias = Magias()
            self._equipamentos = Equipamentos(nome)
        else:
            self._level = level
            self.HPmax = 40 * level
            self.HP = 40 * level
            self.XP = 10 + (10 * round(level/1.3))

        Personagem.personagens.append(self)

    def __str__(self):
        return f'{self._nome}'
