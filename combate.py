import random

def iniciar_combate(jogador, mob):
    print(f"\n UM INIMIGO APARECEU! Um {mob['nome']} surgiu da névoa!")
    
    vida_mob = mob["vida"]
    
    while vida_mob > 0 and jogador["vida"] > 0:
        print(f"\n--- {mob['nome']} (HP: {vida_mob}) vs {jogador['nome']} (HP: {jogador['vida']}) ---")
        opcao = input("Escolha uma ação: [1] Atacar | [2] Tentar Fugir: ")
        
        if opcao == "1":
            # Dano do jogador baseado na Força ou Magia
            dano_jogador = jogador.get("forca", 2)
            vida_mob -= dano_jogador
            print(f"Você atacou o {mob['nome']} e causou {dano_jogador} de dano!")
            
            if vida_mob <= 0:
                print(f"🎉 Você derrotou o {mob['nome']}!")
                break
                
            # Mob ataca de volta se ainda estiver vivo
            dano_mob = mob["ataque"]
            jogador["vida"] -= dano_mob
            print(f"O {mob['nome']} te atacou e causou {dano_mob} de dano!")
            
        elif opcao == "2":
            print("Você tentou fugir...")
            if random.random() > 0.5:
               return

            else:
                print(" Falha ao fugir! O inimigo te acertou pelas costas!")
                jogador["vida"] -= mob["ataque"]
        
        if jogador["vida"] <= 0:
            print("\n Você foi derrotado...")
            break