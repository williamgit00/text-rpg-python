import random

from itens import ESPADAS, CAJADOS, POCOES, LIXOS

def dados(jogador):

    resultado = random.randint(0, 7)
    print(f"\nVocê rolou o dado do destino e obteve: {resultado}")

    # Garantir que o inventário existe
    if "inventario" not in jogador:
        jogador["inventario"] = []

    # (0) FALHA CRÍTICA
    if resultado == 0:
        print("Falha crítica! Você tropeçou e recebeu um debuff (-1 de vida).")
        jogador["debuff"] = True
        jogador["vida"] = max(0, jogador.get("vida", 0) - 1)

    # (1 e 2) ACHA ITEM LIXO
    elif resultado in [1, 2]:
        lixo = random.choice(LIXOS)
        print(f"Que azar... Você só encontrou um: {lixo}")
        jogador["inventario"].append(lixo)

    # (3 e 4) ACHA POÇÕES (CURA OU MANA)
    elif resultado in [3, 4]:
        pocao = random.choice(POCOES)
        print(f"Você encontrou uma {pocao['nome']}!")
        jogador["inventario"].append(pocao['nome'])

    # (5) ARMA NORMAL
    elif resultado == 5:
        classe = jogador.get("classe", "Guerreiro").lower()
        if classe == "mago":
            cajado = random.choice(CAJADOS["normal"])
            print(f"Você encontrou um cajado: {cajado['nome']} (+{cajado['magia']} Magia)!")
            jogador["inventario"].append(cajado['nome'])
            jogador["magia"] = jogador.get("magia", 0) + cajado['magia']  # Soma o status!
        else:
            espada = random.choice(ESPADAS["normal"])
            print(f"Você encontrou uma espada: {espada['nome']} (+{espada['forca']} Força)!")
            jogador["inventario"].append(espada['nome'])
            jogador["forca"] = jogador.get("forca", 0) + espada['forca']  # Soma o status!

    # (6) ARMA ÉPICA
    elif resultado == 6:
        classe = jogador.get("classe", "Guerreiro").lower()
        if classe == "mago":
            cajado = random.choice(CAJADOS["epica"])
            print(f"ÉPICO! Você encontrou um {cajado['nome']} (+{cajado['magia']} Magia)!")
            jogador["inventario"].append(cajado['nome'])
            jogador["magia"] = jogador.get("magia", 0) + cajado['magia']  # Soma o status!
        else:
            espada = random.choice(ESPADAS["epica"])
            print(f"ÉPICO! Você encontrou uma {espada['nome']} (+{espada['forca']} Força)!")
            jogador["inventario"].append(espada['nome'])
            jogador["forca"] = jogador.get("forca", 0) + espada['forca']  # Soma o status!

    # (7) ACERTO CRÍTICO: ARMA LENDÁRIA + RESTAURA VIDA
    elif resultado == 7:
        classe = jogador.get("classe", "Guerreiro").lower()
        print("🌟 ACERTO CRÍTICO! Os deuses te abençoaram!")
        
        if classe == "mago":
            lendaria = CAJADOS["lendaria"][0]
            print(f"LENDÁRIO! Você ganhou o {lendaria['nome']} (+{lendaria['magia']} Magia)!")
            jogador["inventario"].append(lendaria['nome'])
            jogador["magia"] = jogador.get("magia", 0) + lendaria['magia']  # Soma o status!
        else:
            lendaria = ESPADAS["lendaria"][0]
            print(f"LENDÁRIO! Você ganhou a {lendaria['nome']} (+{lendaria['forca']} Força)!")
            jogador["inventario"].append(lendaria['nome'])
            jogador["forca"] = jogador.get("forca", 0) + lendaria['forca']  # Soma o status!
            
        # Restaura vida
        vida_max = jogador.get("vida_maxima", 10)
        jogador["vida"] = vida_max
        print(f"Sua vida foi totalmente restaurada: {jogador['vida']}/{vida_max}")