from models.itens import Itens
class Equipamentos:
    _equipados = {}

    def __init__(self, nome_personagem):
        self.nome_personagem = nome_personagem

        if nome_personagem not in Equipamentos._equipados:
            Equipamentos._equipados[nome_personagem] = {
                'arma': {},
                'escudo': {},            
            }
    
    def equipar_item(nome_personagem, cod, espaco):
        Equipamentos._equipados[nome_personagem][espaco] = Itens._itens[nome_personagem][cod]
        Itens.remover_item(nome_personagem, cod, 1)

    @classmethod
    def equipar(cls, nome_personagem):
        print('Selecione o equipamento que deseja equipar:')
        print(Itens.verificar_armamentos(nome_personagem, True) + '\n')

        while True:
            try:
                opcao = int(input('Digite o número da opção escolhida: '))
                if opcao > 3 and Itens._itens[nome_personagem][opcao].get('quantidade', 0) > 0:
                    break
                else:
                    print('Entrada inválida')
            except:
                print('Entrada inválida')
        
        #VERIFICANDO SE É ESCUDO OU ARMA
        if Itens._itens[nome_personagem][opcao]['tipo_bonus'] == 'def':
            if cls._equipados['escudo']:
                print('já possui um escudo equipado')
            elif cls._equipados['arma'][opcao]['maos'] == 2:
                print('arma equipada é de 2 mãos')
            else:
                cls.equipar_item(nome_personagem, opcao, 'escudo')
        else:
            if cls._equipados[nome_personagem]['arma']:
                print('já possui uma arma equipada')
            elif cls._equipados[nome_personagem]['escudo'] and  Itens._itens[nome_personagem][opcao]['maos'] == 2:
                print('arma equipada é de 2 mãos e possui um escudo equipado.')
            else:
                cls.equipar_item(nome_personagem, opcao, 'arma')

    @classmethod
    def verifica_equipamentos(cls, nome_personagem):
        if nome_personagem in cls._equipados:
            itens_equipados = []

            if cls._equipados[nome_personagem]['arma']:
                arma = cls._equipados[nome_personagem]['arma']
                itens_equipados.append(f"{arma['nome']} - Dano: {arma['dano_min']} - {arma['dano_max']}")
            
            return "\n".join(itens_equipados)