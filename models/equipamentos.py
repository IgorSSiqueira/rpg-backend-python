from models.itens import Itens
class Equipamentos:
    _equipados = {}

    def __init__(self, nome_personagem):
        self.nome_personamem = nome_personagem
        if nome_personagem not in Equipamentos._equipados:
            Equipamentos._equipados= {
                'maos': {},
                'escudo': {},            
            }

    @classmethod
    def equipar(cls, nome_personagem, equipamento: Itens):
        if nome_personagem in cls._equipados:
            if equipamento._itens['escudo_basico']:
                cls._equipados[nome_personagem]['escudo'] = equipamento
            else:
                cls._equipados[nome_personagem]['maos'] = equipamento

    #TODO
    # PRECISA VERIFICAR A ARMA E O ESCUDO PARA CONFIRMAR SE PODE EQUIPAR OU NÃO

    @classmethod
    def verifica_equipamentos(cls, nome_personagem):
        if nome_personagem in cls._equipados:
            itens_equipados = []
            if itens_equipados['maos']:
                itens_equipados.append(f"{cls._equipados['maos']['nome']}")