class Itens:
    _itens = {}

    def __init__(self, nome_personagem):
        self.nome_personagem = nome_personagem

        if nome_personagem not in Itens._itens:
            Itens._itens[nome_personagem] = {
                1: {'cod': 1, 'nome': 'Potion', 'quantidade': 1, 'cura': 30},
                2: {'cod': 2, 'nome': 'Hi Potion', 'quantidade': 1, 'cura': 80},
                3: {'cod': 3, 'nome': 'Mana Potion', 'quantidade': 1, 'cura': 50},
                4: {'cod': 4,'nome': 'Espada Inicial', 'quantidade': 1, 'dano_min': 8, 'dano_max': 12, 'maos': 1, 'tipo_bonus': 'str', 'bonus': 5},
                5: {'cod': 5, 'nome': 'Cetro Inicial', 'quantidade': 1, 'dano_min': 5, 'dano_max': 8, 'maos': 2, 'tipo_bonus': 'int', 'bonus': 20},
                6: {'cod': 6, 'nome': 'Escudo Básico', 'quantidade': 1, 'dano_min': 0, 'dano_max': 0, 'maos': 1,'tipo_bonus': 'def', 'bonus': 5},
                7: {'cod': 7, 'nome': 'Espada Longa', 'quantidade': 1, 'dano_min': 25, 'dano_max': 45, 'maos': 2, 'tipo_bonus': 'str', 'bonus': 15},
                8: {'cod': 8, 'nome': 'Cetro Mágico', 'quantidade': 1, 'dano_min': 10, 'dano_max': 15, 'maos': 2, 'tipo_bonus': 'int', 'bonus': 50, 'tipo_especial': 'restaura_mana', 'especial': 50, 'desc_esp': 'Restaura 50 de mana quando mata um inimigo'},
                9: {'cod': 9, 'nome': 'Espada Vampírica', 'quantidade': 1, 'dano_min': 5, 'dano_max': 25, 'maos': 1, 'tipo_bonus': 'str', 'bonus': 8, 'tipo_especial': 'roubo_vida', 'especial': 100, 'desc_esp': 'Restaura 100% do dano realizado'},
            }

    @classmethod
    def verificar_quantidade_item(cls, nome_personagem, cod):
        return cls._itens[nome_personagem][cod]['quantidade']

    @classmethod
    def verificar_pocoes(cls, nome_personagem):
        if nome_personagem in cls._itens:
            return (
                f"\nPossui: {cls._itens[nome_personagem][1]} Potions\n"
                f"{cls._itens[nome_personagem][2]} Hi Potions\n"
                f"{cls._itens[nome_personagem][3]} Mana Potions\n\n"
            )
        else:
            return f"Personagem '{nome_personagem}' não encontrado"
    
    @classmethod
    def verificar_armamentos(cls, nome_personagem, is_equipar = False):
        if nome_personagem in cls._itens:
            armamentos = []
            equip_char = cls._itens[nome_personagem]

            cls._itens[nome_personagem][4]['quantidade']
            
            if not is_equipar: 
                if equip_char[4].get('quantidade', 0) > 0: 
                    espada_ini = cls._itens[nome_personagem][4]
                    armamentos.append(f"{espada_ini['nome']}: qtd: {espada_ini['quantidade']} - Dano {espada_ini['dano_min']} - {espada_ini['dano_max']}"
                                    + f" - Bônus: {espada_ini['tipo_bonus']} + {espada_ini['bonus']} - ({espada_ini['maos']} mão)")
    
                if equip_char[5].get('quantidade', 0) > 0: 
                    cetro_ini = cls._itens[nome_personagem][5]
                    armamentos.append(f"{cetro_ini['nome']}: qtd: {cetro_ini['quantidade']} - Dano {cetro_ini['dano_min']} - {cetro_ini['dano_max']}"
                                    + f" - Bônus: {cetro_ini['tipo_bonus']} + {cetro_ini['bonus']} - ({cetro_ini['maos']} mão)")

                if equip_char[6].get('quantidade', 0) > 0: 
                    escudo_basico = cls._itens[nome_personagem][6]
                    armamentos.append(f"{escudo_basico['nome']}: qtd: {escudo_basico['quantidade']} - Dano {escudo_basico['dano_min']} - {escudo_basico['dano_max']}"
                                    + f" - Bônus: {escudo_basico['tipo_bonus']} + {escudo_basico['bonus']} - ({escudo_basico['maos']} mão)")

                if equip_char[7].get('quantidade', 0) > 0: 
                    espada_longa = cls._itens[nome_personagem][7]
                    armamentos.append(f"{espada_longa['nome']}: qtd: {espada_longa['quantidade']} - Dano {espada_longa['dano_min']} - {espada_longa['dano_max']}"
                                    + f" - Bônus: {espada_longa['tipo_bonus']} + {espada_longa['bonus']} - ({espada_longa['maos']} mão)")

                if equip_char[8].get('quantidade', 0) > 0: 
                    cetro_magico = cls._itens[nome_personagem][8]
                    armamentos.append(f"{cetro_magico['nome']}: qtd: {cetro_magico['quantidade']} - Dano {cetro_magico['dano_min']} - {cetro_magico['dano_max']}"
                                    + f" - Bônus: {cetro_magico['tipo_bonus']} + {cetro_magico['bonus']} - {cetro_magico['desc_esp']} - ({cetro_magico['maos']} mão)")

                if equip_char[9].get('quantidade', 0) > 0: 
                    espada_vamp = cls._itens[nome_personagem][9]
                    armamentos.append(f"{espada_vamp['nome']}: qtd: {espada_vamp['quantidade']} - Dano {espada_vamp['dano_min']} - {espada_vamp['dano_max']}"
                                    + f" - Bônus: {espada_vamp['tipo_bonus']} + {espada_vamp['bonus']} - {espada_vamp['desc_esp']} - ({espada_vamp['maos']} mão)")
            else:
                if equip_char[4].get('quantidade', 0) > 0: 
                    espada_ini = cls._itens[nome_personagem][4]
                    armamentos.append(f"Opção {espada_ini['cod']} -> {espada_ini['nome']}: Dano {espada_ini['dano_min']} - {espada_ini['dano_max']}"
                                    + f" - Bônus: {espada_ini['tipo_bonus']} + {espada_ini['bonus']} - ({espada_ini['maos']} mão)")
                 
                if equip_char[5].get('quantidade', 0) > 0: 
                    cetro_ini = cls._itens[nome_personagem][5]
                    armamentos.append(f"Opção {cetro_ini['cod']} -> {cetro_ini['nome']}: Dano {cetro_ini['dano_min']} - {cetro_ini['dano_max']}"
                                    + f" - Bônus: {cetro_ini['tipo_bonus']} + {cetro_ini['bonus']} - ({cetro_ini['maos']} mão)")

                if equip_char[6].get('quantidade', 0) > 0: 
                    escudo_basico = cls._itens[nome_personagem][6]
                    armamentos.append(f"Opção {escudo_basico['cod']} -> {escudo_basico['nome']}: Dano {escudo_basico['dano_min']} - {escudo_basico['dano_max']}"
                                    + f" - Bônus: {escudo_basico['tipo_bonus']} + {escudo_basico['bonus']} - ({escudo_basico['maos']} mão)")

                if equip_char[7].get('quantidade', 0) > 0: 
                    espada_longa = cls._itens[nome_personagem][7]
                    armamentos.append(f"Opção {espada_longa['cod']} -> {espada_longa['nome']}: Dano {espada_longa['dano_min']} - {espada_longa['dano_max']}"
                                    + f" - Bônus: {espada_longa['tipo_bonus']} + {espada_longa['bonus']} - ({espada_longa['maos']} mão)")

                if equip_char[8].get('quantidade', 0) > 0: 
                    cetro_magico = cls._itens[nome_personagem][8]
                    armamentos.append(f"Opção {cetro_magico['cod']} -> {cetro_magico['nome']}: Dano {cetro_magico['dano_min']} - {cetro_magico['dano_max']}"
                                    + f" - Bônus: {cetro_magico['tipo_bonus']} + {cetro_magico['bonus']} - {cetro_magico['desc_esp']} - ({cetro_magico['maos']} mão)")

                if equip_char[9].get('quantidade', 0) > 0: 
                    espada_vamp = cls._itens[nome_personagem][9]
                    armamentos.append(f"Opção {espada_vamp['cod']} -> {espada_vamp['nome']}:Dano {espada_vamp['dano_min']} - {espada_vamp['dano_max']}"
                                    + f" - Bônus: {espada_vamp['tipo_bonus']} + {espada_vamp['bonus']} - {espada_vamp['desc_esp']} - ({espada_vamp['maos']} mão)")

            if armamentos:                
                return "\n".join(armamentos)
            else:
                return "Nenhum equipamento no inventário"
        else:
            return f"Personagem '{nome_personagem}' não encontrado"
    
    @classmethod
    def adicionar_item(cls, nome_personagem, cod, quantidade):
        if nome_personagem in cls._itens:
            if cod in cls._itens[nome_personagem]:
                cls._itens[nome_personagem][cod]['quantidade'] += quantidade
                print(f"{quantidade} {cls._itens[nome_personagem][cod]['nome']}(s) adicionados para '{nome_personagem}'.")
                return True
            else:
                print("Item inválido")
                return False
        else:
            print(f"Personagem '{nome_personagem}' não encontrado")
            return False
    
    @classmethod
    def remover_item(cls, nome_personagem, cod, quantidade):
        if nome_personagem in cls._itens:
            if cod in cls._itens[nome_personagem]:
                cls._itens[nome_personagem][cod]['quantidade'] -= quantidade
                print(f"{quantidade} {cls._itens[nome_personagem][cod]['nome']}(s) removidos de '{nome_personagem}'.")
                return True
            else:
                print("Item inválido")
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