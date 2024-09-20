from utils.constantes import DEFESA, FORCA, INTELIGENCIA, VITALIDADE, FORCA_EQUIPAMENTO, INTELIGENCIA_EQUIPAMENTO, DEFESA_EQUIPAMENTO, ADICIONAR
from DB.rpg_backend_DB import ler_tabela

class Atributos:
    _atributos = {}

    def __init__(self, nome_personagem):
        self.nome_personagem = nome_personagem

        if nome_personagem not in Atributos._atributos:
            Atributos._atributos[nome_personagem] = {
                FORCA: 1,
                FORCA_EQUIPAMENTO: 0,
                INTELIGENCIA: 1,
                INTELIGENCIA_EQUIPAMENTO: 0,
                VITALIDADE: 1,
                DEFESA: 1,
                DEFESA_EQUIPAMENTO: 0
            }
    
    def selecao_atributo(self):
        print ('1 - Força\n'
              +'2 - Inteligência\n'
              +'3 - Vitalidade\n'
              +'4 - Defesa\n')

    def listar_atributos(self, nome_personagem):
        print (f'\nPossui {self._atributos[nome_personagem][FORCA] + self._atributos[nome_personagem][FORCA_EQUIPAMENTO]} de força!\n'
               +f'Possui {self._atributos[nome_personagem][INTELIGENCIA] + self._atributos[nome_personagem][INTELIGENCIA_EQUIPAMENTO]} de inteligência!\n'
               +f'Possui {self._atributos[nome_personagem][VITALIDADE]} de vitalidade!\n'
               +f'Possui {self._atributos[nome_personagem][DEFESA] + self._atributos[nome_personagem][DEFESA_EQUIPAMENTO]} de defesa!\n')

    def retornar_atributo(self, nome_personagem, atributo):
        return self._atributos[nome_personagem][atributo]
    

    def adicionar_remover_ponto_atributo(self, nome_personagem, atributo, adicionar: bool, pontos = 1):
        if adicionar:
            self._atributos[nome_personagem][atributo] += pontos
        else:
            self._atributos[nome_personagem][atributo] -= pontos
    
    def zerar_atributo_equipamento(self, nome_personagem, atributo):
        self._atributos[nome_personagem][atributo] = 0

    def carregar_atributos(self, nome):
        where = f" where nome_player = '{nome}'"
        dados = ler_tabela('forca, inteligencia, vitalidade, defesa', 'ATRIBUTOS', where)
        self.adicionar_remover_ponto_atributo(nome, FORCA, ADICIONAR, dados[0])
        self.adicionar_remover_ponto_atributo(nome, INTELIGENCIA, ADICIONAR, dados[1])
        self.adicionar_remover_ponto_atributo(nome, VITALIDADE, ADICIONAR, dados[2])
        self.adicionar_remover_ponto_atributo(nome, DEFESA, ADICIONAR, dados[3])

        
    