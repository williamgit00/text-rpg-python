

MOBS_POR_CIDADE = {
   
    "Vila Inicial": [
        {"nome": "Goblin Ladrão", "vida": 8, "dano": 2, "tipo": "normal"},
        {"nome": "Esqueleto Decrépito", "vida": 10, "dano": 3, "tipo": "normal"},
        {"nome": "Lobo Selvagem", "vida": 12, "dano": 4, "tipo": "épico"}  # Mini-boss da cidade 1
    ],
    
    
    "Floresta Sombria": [
        {"nome": "Orc Guerreiro", "vida": 20, "dano": 5, "tipo": "normal"},
        {"nome": "Aranha Gigante", "vida": 18, "dano": 6, "tipo": "normal"},
        {"nome": "Orc Capitão", "vida": 28, "dano": 8, "tipo": "épico"}   # Mini-boss da cidade 2
    ],
    
    
    "Terras Desoladas": [
        {"nome": "Cavaleiro Amaldiçoado", "vida": 35, "dano": 9, "tipo": "normal"},
        {"nome": "Gargula de Pedra", "vida": 40, "dano": 10, "tipo": "normal"},
        {"nome": "Lich das Sombras", "vida": 50, "dano": 12, "tipo": "épico"}  # Chefão da cidade 3
    ],
    
   
    "rei_demonio": [
        {"nome": "Rei Demônio Abaddoth", "vida": 80, "dano": 16, "tipo": "lendário"}
    ]
}

def sortear_mob(cidade_atual):
   
    mobs_disponiveis = MOBS_POR_CIDADE.get(cidade_atual, MOBS_POR_CIDADE["Vila Inicial"])
    
    mob_sorteado = random.choice(mobs_disponiveis)
    return mob_sorteado.copy()