from models.itens import Itens


ESCUDO = 'escudo'
ARMA = 'arma'

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
        print(f'{espaco} equipado!')
    
    def desequipar_item(nome_personagem, espaco):
        Itens.adicionar_item(nome_personagem, Equipamentos._equipados[nome_personagem][espaco]['cod'], 1)
        Equipamentos._equipados[nome_personagem][espaco] = {}
        print(f'{espaco} desequipado!')

    def while_escolha(texto, nome_personagem):
        while True:
            try:
                opcao_selecionada = int(input(texto))
                if opcao_selecionada > 3 and Itens._itens[nome_personagem][opcao_selecionada].get('quantidade', 0) > 0:
                    break
                else:
                    print('Opção não existente')
            except ValueError:
                print('Entrada inválida! Por favor, digite um número')
            except KeyError:
                print('Item não encontrado para a opção escolhida')
        
        return opcao_selecionada


    @classmethod
    def equipar(cls, nome_personagem):
        print('Selecione o equipamento que deseja equipar:')
        print(Itens.verificar_armamentos(nome_personagem, True) + '\n')

        equip = cls.while_escolha('Digite o número do equipamento escolhido: ', nome_personagem)
        
        #VERIFICANDO SE É ESCUDO OU ARMA
        if Itens._itens[nome_personagem][equip]['tipo_bonus'] == 'def':
            if cls._equipados[ESCUDO]:
                print('\nJá possui um escudo equipado. Deseja desequipar e equipar o escudo selecionado?')
                opcao = cls.while_escolha('1 - Sim. 2 - Não: ')
                
                if opcao == 1:
                    cls.desequipar_item(nome_personagem, ESCUDO)
                    cls.equipar_item(nome_personagem, equip, ESCUDO)
                    return '\nEscudo alterado!\n'
                else:
                    return '\nNão foi feito nenhuma alteração nos equipamentos.\n'
                
            elif cls._equipados['arma'][equip]['maos'] == 2:
                print('Sua arma equipada é de 2 mãos, deseja desequipar ela para equipar o escudo?')
                opcao = cls.while_escolha('1 - Sim. 2 - Não: ')

                if opcao == 1:
                    cls.desequipar_item(nome_personagem, ARMA)
                    cls.equipar_item(nome_personagem, equip, ESCUDO)
                    return '\nArma retirada para equipar o estudo!\n'
                else:
                    return '\nNão foi feito nenhuma alteração nos equipamentos.\n'

            else:
                cls.equipar_item(nome_personagem, equip, ESCUDO)
                return f'Item equipado: {Itens._itens[nome_personagem][equip]['nome']}'
        else:
            if cls._equipados[nome_personagem][ARMA]:
                if cls._equipados[nome_personagem][ESCUDO] and Itens._itens[nome_personagem][equip]['maos'] == 2:
                    print('Você possui uma arma e um escudo equipados. Deseja remover os dois para equipar a arma de duas mãos?')
                    #TODO

                print('já possui uma arma equipada, deseja alterar para a arma selecionada?')
                #TODO                

            elif cls._equipados[nome_personagem][ESCUDO] and Itens._itens[nome_personagem][equip]['maos'] == 2:
                print('arma equipada é de 2 mãos e possui um escudo equipado. Deseja desequipar o escudo para equipar a arma de duas mãos?')
                #TODO
                
            else:
                cls.equipar_item(nome_personagem, equip, ARMA)
                return f'Item equipado: {Itens._itens[nome_personagem][equip]['nome']}'

    @classmethod
    def verifica_equipamentos(cls, nome_personagem):
        if nome_personagem in cls._equipados:
            itens_equipados = []

            if cls._equipados[nome_personagem][ARMA]:
                arma = cls._equipados[nome_personagem][ARMA]
                itens_equipados.append(f"{arma['nome']} - Dano: {arma['dano_min']} - {arma['dano_max']}")
            
            return "\n".join(itens_equipados)