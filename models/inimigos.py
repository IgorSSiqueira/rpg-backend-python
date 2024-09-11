import random


enemys = {
    1:  {'nome': 'Goblin'               , 'level': 1 , 'chefe': False, 'cod_arma': 4 , 'gold_min': 5  , 'gold_max': 15  , 'area': 1, 'cod_drop': 6},
    2:  {'nome': 'Rato Gigante'         , 'level': 2 , 'chefe': False, 'cod_arma': 4 , 'gold_min': 8  , 'gold_max': 20  , 'area': 1, 'cod_drop': 5},
    3:  {'nome': 'Lobo Selvagem'        , 'level': 3 , 'chefe': False, 'cod_arma': 4 , 'gold_min': 12 , 'gold_max': 23  , 'area': 1, 'cod_drop': 6},
    4:  {'nome': 'Esqueleto'            , 'level': 4 , 'chefe': False, 'cod_arma': 4 , 'gold_min': 15 , 'gold_max': 28  , 'area': 1, 'cod_drop': 4},

    5:  {'nome': 'Gigante'              , 'level': 5 , 'chefe': True , 'cod_arma': 4 , 'gold_min': 35 , 'gold_max': 50  , 'area': 2, 'cod_drop': 7},
    
    6:  {'nome': 'Orc'                  , 'level': 13, 'chefe': False, 'cod_arma': 7 , 'gold_min': 23 , 'gold_max': 38  , 'area': 3, 'cod_drop': 8},
    7:  {'nome': 'Troll'                , 'level': 15, 'chefe': False, 'cod_arma': 4 , 'gold_min': 28 , 'gold_max': 45  , 'area': 3, 'cod_drop': 7},
    
    8:  {'nome': 'Elemental de Fogo'    , 'level': 20, 'chefe': False, 'cod_arma': 7 , 'gold_min': 35 , 'gold_max': 50  , 'area': 4, 'cod_drop': 7},
    9:  {'nome': 'Necromante'           , 'level': 22, 'chefe': False, 'cod_arma': 4 , 'gold_min': 40 , 'gold_max': 55  , 'area': 4, 'cod_drop': 8},
    11: {'nome': 'Assassino Sombrio'    , 'level': 26, 'chefe': False, 'cod_arma': 7 , 'gold_min': 43 , 'gold_max': 62  , 'area': 4, 'cod_drop': 7},
    
    10: {'nome': 'Dragão Bebê'          , 'level': 15, 'chefe': True , 'cod_arma': 7 , 'gold_min': 55 , 'gold_max': 95  , 'area': 5, 'cod_drop': 8},
    
    12: {'nome': 'Gárgula'              , 'level': 32, 'chefe': False, 'cod_arma': 4 , 'gold_min': 45 , 'gold_max': 65  , 'area': 6, 'cod_drop': 9},
    13: {'nome': 'Demônio Menor'        , 'level': 38, 'chefe': False, 'cod_arma': 8 , 'gold_min': 55 , 'gold_max': 75  , 'area': 6, 'cod_drop': 10},
    
    15: {'nome': 'Lorde Vampiro'        , 'level': 22, 'chefe': True , 'cod_arma': 10, 'gold_min': 150, 'gold_max': 220 , 'area': 6, 'cod_drop': 10},
    
    14: {'nome': 'Cavaleiro Corrompido' , 'level': 42, 'chefe': False, 'cod_arma': 4 , 'gold_min': 70 , 'gold_max': 100 , 'area': 7, 'cod_drop': 9},
    16: {'nome': 'Hidra'                , 'level': 45, 'chefe': False, 'cod_arma': 10, 'gold_min': 100, 'gold_max': 130 , 'area': 7, 'cod_drop': 9},
    17: {'nome': 'Fênix'                , 'level': 50, 'chefe': False, 'cod_arma': 8 , 'gold_min': 130, 'gold_max': 150 , 'area': 7, 'cod_drop': 10},
    
    19: {'nome': 'Dragão Ancião'        , 'level': 30, 'chefe': True , 'cod_arma': 9 , 'gold_min': 250, 'gold_max': 360 , 'area': 7, 'cod_drop': 9},

    18: {'nome': 'Demônio Maior'        , 'level': 60, 'chefe': False, 'cod_arma': 10, 'gold_min': 180, 'gold_max': 230 , 'area': 8, 'cod_drop': 9},
    20: {'nome': 'Deus das Trevas'      , 'level': 40, 'chefe': True , 'cod_arma': 10, 'gold_min': 500, 'gold_max': 1000, 'area': 8, 'cod_drop': 10},
}

def gerar_inimigo(area):
    inimigos_area = [inimigo for inimigo in enemys.values() if inimigo['area'] == area]
        
    return random.choice(inimigos_area)

def gerar_primeiro_inimigo():
    return enemys[1]