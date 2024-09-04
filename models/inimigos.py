import random


enemys = {
    1: {'nome': 'Goblin', 'level': 1, 'cod_arma': 4},
    2: {'nome': 'Rato Gigante', 'level': 2, 'cod_arma': 4},
    3: {'nome': 'Lobo Selvagem', 'level': 3, 'cod_arma': 4},
    4: {'nome': 'Esqueleto', 'level': 4, 'cod_arma': 4},
    5: {'nome': 'Gigante', 'level': 5, 'chefe': True, 'cod_arma': 7},
    6: {'nome': 'Orc', 'level': 6, 'cod_arma': 4},
    7: {'nome': 'Troll', 'level': 7, 'cod_arma': 4},
    8: {'nome': 'Elemental de Fogo', 'level': 8, 'cod_arma': 7},
    9: {'nome': 'Necromante', 'level': 9, 'cod_arma': 7},
    10: {'nome': 'Dragão Bebê', 'level': 10, 'chefe': True, 'cod_arma': 7},
    11: {'nome': 'Assassino Sombrio', 'level': 11, 'cod_arma': 7},
    12: {'nome': 'Gárgula', 'level': 12, 'cod_arma': 4},
    13: {'nome': 'Demônio Menor', 'level': 13, 'cod_arma': 4},
    14: {'nome': 'Cavaleiro Corrompido', 'level': 14, 'cod_arma': 4},
    15: {'nome': 'Lorde Vampiro', 'level': 15, 'chefe': True, 'cod_arma': 9},
    16: {'nome': 'Hidra', 'level': 16, 'cod_arma': 7},
    17: {'nome': 'Fênix', 'level': 17, 'cod_arma': 7},
    18: {'nome': 'Demônio Maior', 'level': 18, 'cod_arma': 7},
    19: {'nome': 'Dragão Ancião', 'level': 19, 'chefe': True, 'cod_arma': 7},
    20: {'nome': 'Deus das Trevas', 'level': 20, 'chefe': True, 'cod_arma': 9}
}

def gerar_inimigo(level_jogador):
    if level_jogador == 1:
        inimigo_criado = 1
    elif 2 <= level_jogador <= 5:
        inimigo_criado = random.randint(1, level_jogador)
    else:
        inimigo_criado = random.randint(1, level_jogador + 2) if level_jogador <= 18 else random.randint(1, 20)
        
    return enemys[inimigo_criado]