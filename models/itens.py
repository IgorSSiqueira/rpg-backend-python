class Itens:
    _itens = {}

    def __init__(self, nome_personagem):
        self.nome_personagem = nome_personagem
        if nome_personagem not in Itens._itens:
            Itens._itens[nome_personagem] = {
                'potion': {'nome': 'Potion', 'quantidade': 0, 'cura': 30},
                'hipotion': {'nome': 'Hi Potion', 'quantidade': 0, 'cura': 80},
                'mana_potion': {'nome': 'Mana Potion', 'quantidade': 0, 'cura': 50},
                'espada_inicial': {'nome': 'Espada Inicial', 'quantidade': 1, 'dano_min': 8, 'dano_max': 12, 'hand': 1, 'bonus': {'str': 5}},
                'cetro_inicial': {'nome': 'Cetro Inicial', 'quantidade': 1, 'dano_min': 5, 'dano_max': 8, 'hand': 2, 'bonus': {'int': 20}},
                'escudo_basico': {'nome': 'Escudo Básico', 'quantidade': 0, 'dano_min': 0, 'dano_max': 0, 'hand': 1,'bonus': {'def': 5}},
                'espada_longa': {'nome': 'Espada Longa', 'quantidade': 0, 'dano_min': 25, 'dano_max': 45, 'hand': 2, 'bonus': {'str': 15}},
                'cetro_magico': {'nome': 'Cetro Mágico', 'quantidade': 0, 'dano_min': 10, 'dano_max': 15, 'hand': 2, 'bonus': {'int': 50}, 'especial': {'cura': 50}},
                'espada_vampirica': {'nome': 'Espada Vampírica', 'quantidade': 0, 'dano_min': 5, 'dano_max': 25, 'hand': 1, 'bonus': {'str': 8}, 'especial': {'cura': 100}},
            }

    @classmethod
    def verificar_pocoes(cls, nome_personagem):
        if nome_personagem in cls._itens:
            return (
                f"\nPossui: {cls._itens[nome_personagem]['potion']} Potions\n"
                f"{cls._itens[nome_personagem]['hipotion']} Hi Potions\n"
                f"{cls._itens[nome_personagem]['mana_potion']} Mana Potions\n\n"
            )
        else:
            return f"Personagem '{nome_personagem}' não encontrado"
    
    @classmethod
    def verificar_armamentos(cls, nome_personagem):
        if nome_personagem in cls._itens:
            armamentos = []
            equip_char = cls._itens[nome_personagem]

            cls._itens[nome_personagem]['espada_inicial']['dano_min']            
            cls._itens[nome_personagem]['espada_inicial']['dano_max']

            if equip_char['espada_inicial'].get('quantidade', 0) > 0: 
                espada_ini = cls._itens[nome_personagem]['espada_inicial']
                armamentos.append(f"{espada_ini['nome']}: qtd: {espada_ini['quantidade']} - Dano {espada_ini['dano_min']} - {espada_ini['dano_max']}"
                                 + f" - Bônus: Str + {espada_ini['bonus']['str']} - ({espada_ini['hand']} mão)")
 
            if equip_char['cetro_inicial'].get('quantidade', 0) > 0: 
                cetro_ini = cls._itens[nome_personagem]['cetro_inicial']
                armamentos.append(f"{cetro_ini['nome']}: qtd: {cetro_ini['quantidade']} - Dano {cetro_ini['dano_min']} - {cetro_ini['dano_max']}"
                                 + f" - Bônus: Int + {cetro_ini['bonus']['int']} - ({cetro_ini['hand']} mão)")

            if equip_char['escudo_basico'].get('quantidade', 0) > 0: 
                escudo_basico = cls._itens[nome_personagem]['escudo_basico']
                armamentos.append(f"{escudo_basico['nome']}: qtd: {escudo_basico['quantidade']} - Dano {escudo_basico['dano_min']} - {escudo_basico['dano_max']}"
                                 + f" - Bônus: Def + {escudo_basico['bonus']['def']} - ({escudo_basico['hand']} mão)")

            if equip_char['espada_longa'].get('quantidade', 0) > 0: 
                espada_longa = cls._itens[nome_personagem]['espada_longa']
                armamentos.append(f"{espada_longa['nome']}: qtd: {espada_longa['quantidade']} - Dano {espada_longa['dano_min']} - {espada_longa['dano_max']}"
                                 + f" - Bônus: Str + {espada_longa['bonus']['str']} - ({espada_longa['hand']} mão)")

            if equip_char['cetro_magico'].get('quantidade', 0) > 0: 
                cetro_magico = cls._itens[nome_personagem]['cetro_magico']
                armamentos.append(f"{cetro_magico['nome']}: qtd: {cetro_magico['quantidade']} - Dano {cetro_magico['dano_min']} - {cetro_magico['dano_max']}"
                                 + f" - Bônus: Int + {cetro_magico['bonus']['int']} - Restaura {cetro_magico['especial']['cura']} de mana quando mata um inimigo - ({cetro_magico['hand']} mão)")

            if equip_char['espada_vampirica'].get('quantidade', 0) > 0: 
                espada_vamp = cls._itens[nome_personagem]['espada_vampirica']
                armamentos.append(f"{espada_vamp['nome']}: qtd: {espada_vamp['quantidade']} - Dano {espada_vamp['dano_min']} - {espada_vamp['dano_max']}"
                                 + f" - Bônus: Str + {espada_vamp['bonus']['str']} - Restaura {espada_vamp['especial']['cura']}% do dano realizado - ({espada_vamp['hand']} mão)")

            if armamentos:                
                return "\n".join(armamentos)
            else:
                return "Nenhum equipamento no inventário"
        else:
            return f"Personagem '{nome_personagem}' não encontrado"
    
    @classmethod
    def adicionar_item(cls, nome_personagem, tipo_item, quantidade):
        if nome_personagem in cls._itens:
            if tipo_item in cls._itens[nome_personagem]:
                cls._itens[nome_personagem][tipo_item] += quantidade
                print(f"{quantidade} {tipo_item}(s) adicionados para '{nome_personagem}'.")
                return True
            else:
                print(f"Tipo de item '{tipo_item}' inválido")
                return False
        else:
            print(f"Personagem '{nome_personagem}' não encontrado")
            return False

    @classmethod
    def usar_pocao(cls, nome_personagem, tipo_item):
        if tipo_item not in ['potion', 'hipotion', 'mana_potion']:
            print(f"Tipo de item '{tipo_item}' inválido")
            return False

        if nome_personagem in cls._itens:
            if tipo_item[nome_personagem].get(tipo_item, 0) > 0:
                cls._itens[nome_personagem][tipo_item] -= 1
                return True
            else:
                print(f"Quantidade de '{tipo_item}' insuficiente")
                return False
        else:
            print(f"Personagem '{nome_personagem}' não encontrado")
            return False