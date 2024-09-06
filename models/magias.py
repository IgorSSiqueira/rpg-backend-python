from utils.constantes import FOGO, CURA, RESTAURAR
class Magias:
    def __init__(self):
        self._magias = {
            FOGO: {'mana': 5, 'dano_base': 15},
            CURA: {'mana': 20, 'procentagem_cura': 0.20},
            RESTAURAR: {'mana': 70}
        }

    def custo_mana(self, magia):
        return self._magias[magia]['mana']

    def magia_ataque(self, magia, int):
        return self._magias[magia]['dano_base'] + (round((int*5)/1.2))
    
    def cure(self, hp_max, int):
        return (hp_max * self._magias['cure']['procentagem_cura']) + (round((int*5)/1.2))
    
    def restore(self, hp_max):
        return hp_max