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
        print(f'{espaco} equipado(a)!')
    
    def desequipar_item(nome_personagem, espaco):
        Itens.adicionar_item(nome_personagem, Equipamentos._equipados[nome_personagem][espaco]['cod'], 1)
        Equipamentos._equipados[nome_personagem][espaco] = {}
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
    def equipar(cls, nome_personagem):
        print('Selecione o equipamento que deseja equipar:')
        
        print(Itens.verificar_armamentos(nome_personagem, True) + '\n')
        equip = cls.while_escolha('Digite o número do equipamento escolhido: ', nome_personagem)
        
        #VERIFICANDO SE É ESCUDO OU ARMA
        if Itens._itens[nome_personagem][equip]['tipo_bonus'] == 'def':
            if cls._equipados[nome_personagem][ESCUDO]:
                print('\nJá possui um escudo equipado. Deseja desequipar e equipar o escudo selecionado?')
                opcao = cls.while_escolha('1 - Sim. 2 - Não: ', nome_personagem, True)
                
                if opcao == 1:
                    cls.desequipar_item(nome_personagem, ESCUDO)
                    cls.equipar_item(nome_personagem, equip, ESCUDO)
                    return '\nEscudo alterado!\n\n'
                else:
                    return '\nNão foi feito nenhuma alteração nos equipamentos.\n\n'
                
            elif cls._equipados[nome_personagem][ARMA]['maos'] == 2:
                print('Sua arma equipada é de 2 mãos, deseja desequipar ela para equipar o escudo?')
                opcao = cls.while_escolha('1 - Sim. 2 - Não: ', nome_personagem, True)

                if opcao == 1:
                    cls.desequipar_item(nome_personagem, ARMA)
                    cls.equipar_item(nome_personagem, equip, ESCUDO)
                    return '\nArma de 2 mãos desequipada para equipar o escudo!\n\n'
                else:
                    return '\nNão foi feito nenhuma alteração nos equipamentos.\n\n'

            else:
                cls.equipar_item(nome_personagem, equip, ESCUDO)
                return '\nEscudo equipado\n\n'
        else:
            if cls._equipados[nome_personagem][ARMA]:
                if Itens._itens[nome_personagem][equip]['maos'] == 2 and cls._equipados[nome_personagem][ESCUDO]:
                    print('Você possui uma arma e um escudo equipados. Deseja remover os dois para equipar a arma de duas mãos?\n')
                    opcao = cls.while_escolha('1 - Sim. 2 - Não: ', nome_personagem, True)

                    if opcao == 1:
                        cls.desequipar_item(nome_personagem, ARMA)
                        cls.desequipar_item(nome_personagem, ESCUDO)
                        cls.equipar_item(nome_personagem, equip, ARMA)
                        return '\nArma e escudo desequipados para equipar a arma de 2 mãos\n\n'
                    else:
                        return '\nNão foi feito nenhuma alteração nos equipamentos.\n\n'
                    
                else:
                    print('já possui uma arma equipada, deseja alterar para a arma selecionada?\n')
                    opcao = cls.while_escolha('1 - Sim. 2 - Não: ', nome_personagem, True)

                    if opcao == 1:
                        cls.desequipar_item(nome_personagem, ARMA)
                        cls.equipar_item(nome_personagem, equip, ARMA) 
                        return '\nArma desequipada para equipar o novo equipamento\n\n'  
                    else:
                        return '\nNão foiu feito nenhuma alteração nois equipamentos.\n\n'         

            elif Itens._itens[nome_personagem][equip]['maos'] == 2 and cls._equipados[nome_personagem][ESCUDO]:
                print('arma equipada é de 2 mãos e possui um escudo equipado. Deseja desequipar o escudo para equipar a arma de duas mãos?\n')
                opcao = cls.while_escolha('1 - Sim. 2 - Não: ', nome_personagem, True)

                if opcao == 1:
                    cls.desequipar_item(nome_personagem, ESCUDO)
                    cls.equipar_item(nome_personagem, equip, ARMA)
                    return '\nArma desequipada para equipar a nova arma\n\n'
                else:
                    return '\nNão foi feito nenhuma alteração nos equipamentos.\n\n'
                
            else:
                cls.equipar_item(nome_personagem, equip, ARMA)
                return '\nArma equipada!\n\n'

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