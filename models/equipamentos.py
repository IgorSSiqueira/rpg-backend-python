from models.itens import Itens
from models.atributos import Atributos
from utils.constantes import ARMA, ESCUDO, FORCA_EQUIPAMENTO, INTELIGENCIA_EQUIPAMENTO, DEFESA_EQUIPAMENTO, ADICIONAR

class Equipamentos:
    _equipados = {}

    def __init__(self, nome_personagem):
        self.nome_personagem = nome_personagem

        if nome_personagem not in Equipamentos._equipados:
            Equipamentos._equipados[nome_personagem] = {
                ARMA: {},
                ESCUDO: {},            
            }
    
    def equipar_item(nome_personagem, cod, espaco):
        Equipamentos._equipados[nome_personagem][espaco] = Itens._itens[nome_personagem][cod]
        Itens.remover_item(nome_personagem, cod, 1)

        if Itens._itens[nome_personagem][cod]['tipo_bonus'] == 'str':
            Atributos.adicionar_remover_ponto_atributo(Atributos, nome_personagem, FORCA_EQUIPAMENTO, ADICIONAR, Itens._itens[nome_personagem][cod]['bonus'])
        elif Itens._itens[nome_personagem][cod]['tipo_bonus'] == 'int':
            Atributos.adicionar_remover_ponto_atributo(Atributos, nome_personagem, INTELIGENCIA_EQUIPAMENTO, ADICIONAR, Itens._itens[nome_personagem][cod]['bonus'])
        else:
            Atributos.adicionar_remover_ponto_atributo(Atributos, nome_personagem, DEFESA_EQUIPAMENTO, ADICIONAR, Itens._itens[nome_personagem][cod]['bonus'])

        print(f'{Itens._itens[nome_personagem][cod]['nome']} equipado(a)!')
    
    def desequipar_item(nome_personagem, espaco):
        cod_equipamento = Equipamentos._equipados[nome_personagem][espaco]['cod']
        Itens.adicionar_item(nome_personagem, cod_equipamento, 1)
        Equipamentos._equipados[nome_personagem][espaco] = {}

        if Itens._itens[nome_personagem][cod_equipamento]['tipo_bonus'] == 'str':
            Atributos.zerar_atributo_equipamento(Atributos, nome_personagem, FORCA_EQUIPAMENTO)
        elif Itens._itens[nome_personagem][cod_equipamento]['tipo_bonus'] == 'int':
            Atributos.zerar_atributo_equipamento(Atributos, nome_personagem, INTELIGENCIA_EQUIPAMENTO)
        else:
            Atributos.zerar_atributo_equipamento(Atributos, nome_personagem, DEFESA_EQUIPAMENTO)

        print(f'{espaco} desequipado(a)!')

    def while_escolha(texto, nome_personagem, pergunta = False):
        while True:
            try:
                opcao_selecionada = int(input(texto))
                if not pergunta and opcao_selecionada > 3 and Itens._itens[nome_personagem][opcao_selecionada].get('quantidade', 0) > 0:
                    break
                elif pergunta and opcao_selecionada > 0 and opcao_selecionada < 3:
                    break
                else:
                    print('Opção não existente')
            except ValueError:
                print('Entrada inválida! Por favor, digite um número')
            except KeyError:
                print('Item não encontrado para a opção escolhida')
        
        return opcao_selecionada

    @classmethod
    def equipar_primeiro_item(cls, nome_personagem, cod_item):
        cls.equipar_item(nome_personagem, cod_item, ARMA)

    @classmethod
    def equipar(cls, nome_personagem):
        
        item_inventario = Itens.verificar_armamentos_no_inventario(nome_personagem, True)
        
        if item_inventario == 0:
            print('\nNão possui itens no inventário!\n\n')
            return False

        print('Selecione o equipamento que deseja equipar:')
        print(item_inventario + '\n')
        equip = cls.while_escolha('Digite o número do equipamento escolhido: ', nome_personagem)
        
        if Itens._itens[nome_personagem][equip]['tipo_bonus'] == 'def':
            if cls._equipados[nome_personagem][ESCUDO]:
                print('\nJá possui um escudo equipado. Deseja desequipar e equipar o escudo selecionado?')
                opcao = cls.while_escolha('1 - Sim. 2 - Não: ', nome_personagem, True)
                
                if opcao == 1:
                    cls.desequipar_item(nome_personagem, ESCUDO)
                    cls.equipar_item(nome_personagem, equip, ESCUDO)
                    print('\nEscudo alterado!\n\n')
                    return True
                else:
                    print('\nNão foi feito nenhuma alteração nos equipamentos.\n\n')
                    return False
                
            elif cls._equipados[nome_personagem][ARMA]['maos'] == 2:
                print('Sua arma equipada é de 2 mãos, deseja desequipar ela para equipar o escudo?')
                opcao = cls.while_escolha('1 - Sim. 2 - Não: ', nome_personagem, True)

                if opcao == 1:
                    cls.desequipar_item(nome_personagem, ARMA)
                    cls.equipar_item(nome_personagem, equip, ESCUDO)
                    print('\nArma de 2 mãos desequipada para equipar o escudo!\n\n')
                    return True
                else:
                    print('\nNão foi feito nenhuma alteração nos equipamentos.\n\n')
                    return False
            else:
                cls.equipar_item(nome_personagem, equip, ESCUDO)
                print('\nEscudo equipado\n\n')
                return True
        else:
            if cls._equipados[nome_personagem][ARMA]:
                if Itens._itens[nome_personagem][equip]['maos'] == 2 and cls._equipados[nome_personagem][ESCUDO]:
                    print('Você possui uma arma e um escudo equipados. Deseja remover os dois para equipar a arma de duas mãos?\n')
                    opcao = cls.while_escolha('1 - Sim. 2 - Não: ', nome_personagem, True)

                    if opcao == 1:
                        cls.desequipar_item(nome_personagem, ARMA)
                        cls.desequipar_item(nome_personagem, ESCUDO)
                        cls.equipar_item(nome_personagem, equip, ARMA)
                        print('\nArma e escudo desequipados para equipar a arma de 2 mãos\n\n')
                        return True
                    else:
                        print('\nNão foi feito nenhuma alteração nos equipamentos.\n\n')
                        return False
                    
                else:
                    print('já possui uma arma equipada, deseja alterar para a arma selecionada?\n')
                    opcao = cls.while_escolha('1 - Sim. 2 - Não: ', nome_personagem, True)

                    if opcao == 1:
                        cls.desequipar_item(nome_personagem, ARMA)
                        cls.equipar_item(nome_personagem, equip, ARMA) 
                        print('\nArma desequipada para equipar o novo equipamento\n\n')
                        return True
                    else:
                        print('\nNão foiu feito nenhuma alteração nois equipamentos.\n\n')
                        return False        

            elif Itens._itens[nome_personagem][equip]['maos'] == 2 and cls._equipados[nome_personagem][ESCUDO]:
                print('arma equipada é de 2 mãos e possui um escudo equipado. Deseja desequipar o escudo para equipar a arma de duas mãos?\n')
                opcao = cls.while_escolha('1 - Sim. 2 - Não: ', nome_personagem, True)

                if opcao == 1:
                    cls.desequipar_item(nome_personagem, ESCUDO)
                    cls.equipar_item(nome_personagem, equip, ARMA)
                    print('\nArma desequipada para equipar a nova arma\n\n')
                    return True
                else:
                    print('\nNão foi feito nenhuma alteração nos equipamentos.\n\n')
                    return False
                
            else:
                cls.equipar_item(nome_personagem, equip, ARMA)
                print('\nArma equipada!\n\n')
                return True

    @classmethod
    def verificar_equipamentos(cls, nome_personagem):
        if nome_personagem in cls._equipados:
            itens_equipados = []

            if cls._equipados[nome_personagem][ARMA]:
                arma = cls._equipados[nome_personagem][ARMA]
                itens_equipados.append(f"{arma['nome']} - Dano: {arma['dano_min']} - {arma['dano_max']}")
            
            if cls._equipados[nome_personagem][ESCUDO]:
                escudo = cls._equipados[nome_personagem][ESCUDO]
                itens_equipados.append(f"{escudo['nome']} - Defesa {escudo['bonus']}")
            
            return "\n".join(itens_equipados)
    
    @classmethod
    def retornar_arma_escudo(cls, nome_personagem, equipamento):
        if cls._equipados[nome_personagem][equipamento]:
            return cls._equipados[nome_personagem][equipamento]['cod'] 
        else:
            return 0