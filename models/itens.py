class Itens:
    _itens = {}

    def __init__(self, nome_personagem):
        self.nome_personagem = nome_personagem
        if nome_personagem not in Itens._itens:
            Itens._itens[nome_personagem] = {
                'potion': 0,
                'hipotion': 0,
                'mana_potion': 0,
                'espada_inicial': 1,
                'cetro_inicial': 1,
                'escudo_basico': 0,
                'espada_longa': 0,
                'cetro_magico': 0,
                'espada_vampirica': 0
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
            equipamentos = []
            equip_char = cls._itens[nome_personagem]

            if equip_char.get('espada_inicial', 0) > 0: 
                equipamentos.append(f"Espada inicial {cls._itens[nome_personagem]['espada_inicial']} - Dano 8 - 12 (1 mão)")                
            if equip_char.get('cetro_inicial', 0) > 0: 
                equipamentos.append(f"Cetro inicial {cls._itens[nome_personagem]['cetro_inicial']} - dano 5-8. Int + 20 (2 mãos)")
            if equip_char.get('escudo_basico', 0) > 0: 
                equipamentos.append(f"Escudo basico {cls._itens[nome_personagem]['escudo_basico']} - +5 Defesa")
            if equip_char.get('espada_longa', 0) > 0: 
                equipamentos.append(f"Espada longa {cls._itens[nome_personagem]['espada_longa']} - Dano 25 - 40 (2 mãos)")
            if equip_char.get('cetro_magico', 0) > 0: 
                equipamentos.append(f"Cetro mágico {cls._itens[nome_personagem]['cetro_magico']} - Dano 10. Int + 50. Restaura 30 mana quando mata um inimigo (2 mãos)")
            if equip_char.get('espada_vampirica', 0) > 0: 
                equipamentos.append(f"Espada vampírica {cls._itens[nome_personagem]['espada_vampirica']} - Dano 5-25. Cura 100% do dano feito (1 mão)")

            if equipamentos:                
                return "\n".join(equipamentos)
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