import random
from utils.constantes import FOGO, CURA, RESTAURAR
class Magias:
    def __init__(self):
        self._magias = {
            FOGO: {'mana': 15, 'min': 5, 'max': 20},
            CURA: {'mana': 20, 'min': 0.10, 'max': 0.30},
            RESTAURAR: {'mana': 70}
        }

    def custo_mana(self, magia):
        return self._magias[magia]['mana']

    def magia_ataque(self, magia, int_player, player_lvl):
        dano_magia = random.randint(self._magias[magia]['min'], int(self._magias[magia]['max'] * (player_lvl * 0.5)))
        return dano_magia + (int((int_player*3)/1.2))
    
    def cure(self, hp_max, int_player):
        perc = random.uniform(self._magias[CURA]['min'], self._magias[CURA]['max'])
        return round((hp_max * perc) + (int((int_player*3)/1.2)))
    
    def restore(self, hp_max):
        return hp_max