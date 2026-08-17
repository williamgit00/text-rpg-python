import random

# --- ESPADAS (Guerreiro) ---
ESPADAS = {
    "normal": [
        {"nome": "Espada de Madeira", "forca": 1},
        {"nome": "Espada de Ferro", "forca": 2},
        {"nome": "Adaga Amolada", "forca": 3}
    ],
    "epica": [
        {"nome": "Espada Rúnica", "forca": 5},
        {"nome": "Lamina Sombria", "forca": 6}
    ],
    "lendaria": [
        {"nome": "Excalibur do Destino", "forca": 10}
    ]
}

# --- CAJADOS (Mago) ---
CAJADOS = {
    "normal": [
        {"nome": "Cajado Aprendiz", "magia": 1},
        {"nome": "Cajado de Carvalho", "magia": 2},
        {"nome": "Orbe de Vidro", "magia": 3}
    ],
    "epica": [
        {"nome": "Cajado Astral", "magia": 5},
        {"nome": "Cajado Elemental", "magia": 6}
    ],
    "lendaria":[
        {"nome": "Cajado do Arquimago", "magia": 10}
    ]

}

# --- ITENS LIXO ---
LIXOS = [
    "Graveto Seco",
    "Pedra Redonda",
    "Bota Furada",
    "Osso Roído"
]

# Poções utilizadas no sorteio
POCOES = [
    {"nome": "Poção de Cura"},
    {"nome": "Poção de Mana"}
]
