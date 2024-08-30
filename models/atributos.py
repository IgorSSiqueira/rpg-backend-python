
VITALIDADE = 'vitalidade'
FORCA = 'forca'
INTELIGENCIA = 'inteligencia'

class Atributos:
    _atributos = {}

    def __init__(self, nome_personagem):
        self.nome_personagem = nome_personagem

        if nome_personagem not in Atributos._atributos:
            Atributos._atributos[nome_personagem] = {            
                'vitalidade': 1,
                'forca': 1,
                'inteligencia': 1
            }
    
    def listar_atributos(self, nome_personagem):
        return (f'\nPossui {self._atributos[nome_personagem][FORCA]} de força!\n'
               +f'Possui {self._atributos[nome_personagem][INTELIGENCIA]} de inteligência!\n'
               +f'Possui {self._atributos[nome_personagem][VITALIDADE]} de vitalidade!\n')

    def _verificar_atributo(self, nome_personagem, atributo):
        return self._atributos[nome_personagem][atributo]
    

    def adicionar_remover_ponto_atributo(self, nome_personagem, atributo, adicionar: bool, pontos = 1):
        if adicionar:
            self._atributos[nome_personagem][atributo] += pontos
        else:
            self._atributos[nome_personagem][atributo] -= pontos
    