import random
from utils.constantes import FOGO, CURA, RESTAURAR, REGEN
class Magias:
    def __init__(self):
        self._magias = {
            FOGO: {'mana': 15, 'min': 5, 'max': 25},
            CURA: {'mana': 20, 'min': 0.15, 'max': 0.40},
            RESTAURAR: {'mana': 90},
            REGEN: {'mana': 150}
        }

    def custo_mana(self, magia):
        return self._magias[magia]['mana']

    def magia_ataque(self, magia, int_player, player_lvl):
        dano_magia = random.randint(self._magias[magia]['min'], int(self._magias[magia]['max'] * (player_lvl * 0.5)))
        return dano_magia + (int((int_player*3.5)))
    
    def cure(self, hp_max, int_player):
        perc = random.uniform(self._magias[CURA]['min'], self._magias[CURA]['max'])
        return round((hp_max * perc) + (int(int_player*3.5)))
    
    def regen(self, hp_max, int_player):
        regen_total = (hp_max * 0.15) + (int_player * 0.5)
        return int(regen_total)


    def restore(self, hp_max):
        return hp_max