import random


enemys = {
    1:  {'nome': 'Goblin'               , 'level': 1 , 'chefe': False, 'cod_arma': 4 , 'gold_min': 5  , 'gold_max': 15  , 'area': 1},
    2:  {'nome': 'Rato Gigante'         , 'level': 2 , 'chefe': False, 'cod_arma': 4 , 'gold_min': 8  , 'gold_max': 20  , 'area': 1},
    3:  {'nome': 'Lobo Selvagem'        , 'level': 3 , 'chefe': False, 'cod_arma': 4 , 'gold_min': 12 , 'gold_max': 23  , 'area': 1},
    4:  {'nome': 'Esqueleto'            , 'level': 4 , 'chefe': False, 'cod_arma': 4 , 'gold_min': 15 , 'gold_max': 28  , 'area': 1},

    5:  {'nome': 'Gigante'              , 'level': 5 , 'chefe': True , 'cod_arma': 4 , 'gold_min': 35 , 'gold_max': 50  , 'area': 2},
    
    6:  {'nome': 'Orc'                  , 'level': 6 , 'chefe': False, 'cod_arma': 7 , 'gold_min': 23 , 'gold_max': 38  , 'area': 3},
    7:  {'nome': 'Troll'                , 'level': 7 , 'chefe': False, 'cod_arma': 4 , 'gold_min': 28 , 'gold_max': 45  , 'area': 3},

    8:  {'nome': 'Elemental de Fogo'    , 'level': 8 , 'chefe': False, 'cod_arma': 7 , 'gold_min': 35 , 'gold_max': 50  , 'area': 4},
    9:  {'nome': 'Necromante'           , 'level': 9 , 'chefe': False, 'cod_arma': 4 , 'gold_min': 40 , 'gold_max': 55  , 'area': 4},
    11: {'nome': 'Assassino Sombrio'    , 'level': 11, 'chefe': False, 'cod_arma': 7 , 'gold_min': 43 , 'gold_max': 62  , 'area': 4},
    
    10: {'nome': 'Dragão Bebê'          , 'level': 10, 'chefe': True , 'cod_arma': 7 , 'gold_min': 55 , 'gold_max': 95  , 'area': 5},
    
    12: {'nome': 'Gárgula'              , 'level': 12, 'chefe': False, 'cod_arma': 4 , 'gold_min': 45 , 'gold_max': 65  , 'area': 6},
    13: {'nome': 'Demônio Menor'        , 'level': 13, 'chefe': False, 'cod_arma': 8 , 'gold_min': 55 , 'gold_max': 75  , 'area': 6},
    15: {'nome': 'Lorde Vampiro'        , 'level': 15, 'chefe': True , 'cod_arma': 10, 'gold_min': 150, 'gold_max': 220 , 'area': 6},
    
    14: {'nome': 'Cavaleiro Corrompido' , 'level': 14, 'chefe': False, 'cod_arma': 4 , 'gold_min': 70 , 'gold_max': 100 , 'area': 7},
    16: {'nome': 'Hidra'                , 'level': 16, 'chefe': False, 'cod_arma': 10, 'gold_min': 100, 'gold_max': 130 , 'area': 7},
    17: {'nome': 'Fênix'                , 'level': 17, 'chefe': False, 'cod_arma': 8 , 'gold_min': 130, 'gold_max': 150 , 'area': 7},
    19: {'nome': 'Dragão Ancião'        , 'level': 20, 'chefe': True , 'cod_arma': 9 , 'gold_min': 250, 'gold_max': 360 , 'area': 7},

    18: {'nome': 'Demônio Maior'        , 'level': 18, 'chefe': False, 'cod_arma': 10, 'gold_min': 180, 'gold_max': 230 , 'area': 8},
    20: {'nome': 'Deus das Trevas'      , 'level': 30, 'chefe': True , 'cod_arma': 10, 'gold_min': 500, 'gold_max': 1000, 'area': 8}
}

def gerar_inimigo(area):
    inimigos_area = [inimigo for inimigo in enemys.values() if inimigo['area'] == area]
        
    return random.choice(inimigos_area)

def gerar_primeiro_inimigo():
    return enemys[1]