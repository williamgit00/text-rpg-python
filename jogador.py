
from dados import dados

def MENU_JOGADOR(jogador):
    
    

    while True:

        print("\n==========================================")
        print(f" MENU DO JOGADOR - {jogador.get('classe', 'Desconhecida')}")
        print("(1) Ver Status")
        print("(2) Inventário ")
        print("(3) Rolar Dado do Destino")
        print("(4) FUGIR")    

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- STATUS DO JOGADOR ---")
            print(f"Classe: {jogador.get('classe', 'Desconhecida')}")
            print(f"Vida: {jogador.get('vida', 0)}")
            print(f"Força: {jogador.get('forca', 0)}")
            print(f"Magia: {jogador.get('magia', 0)}")
            print(f"Debuff: {'Ativo' if jogador.get('debuff', False) else 'Nenhum'}")
            print("==========================\n")
            input("Pressione ENTER para continuar...")

        elif opcao == "2":
            gerenciar_inventario(jogador)

        elif opcao == "3":
            print("\n--- ROLAR DADO DO DESTINO ---")
            dados(jogador)  
            input("\nPressione ENTER para continuar...")

        elif opcao == "4":
            print("\n--- FUGIR ---")
            print("Você nao pode fugir do combate! Prepare-se para lutar!")
            input("Pressione ENTER para continuar...")

        else:
            print("Opção inválida. Tente novamente.")

def gerenciar_inventario(jogador):
            inventario = jogador.get("inventario", [])

            print("\n--- INVENTÁRIO DO JOGADOR ---")
            if not inventario:
               print("Seu inventário está vazio no momento!")
               print("==========================\n")
               input("Pressione ENTER para voltar...")
               return

            for indice, item in enumerate(inventario, start=1):
                print(f"({indice}) {item}")
                print("(0) Voltar")
                print("==========================\n")
            escolha = input("Digite o número do item para usá-lo: ").strip()

            if escolha == "0" or not escolha.isdigit():
                return
             
            posicao = int(escolha) - 1

            if 0 <= posicao < len(inventario):
               item_escolhido = inventario[posicao]

               if "poção" in item_escolhido.lower():
                vida_max = jogador.get("vida_maxima", 10)
                jogador["vida"] = min(jogador.get("vida", 0) + 5, vida_max)
                inventario.pop(posicao)  # Consome a poção
                print(f"\n Você usou '{item_escolhido}'! Sua vida atual é: {jogador['vida']}/{vida_max}")

               elif "espada" in item_escolhido.lower():
                   print(f"\nVocê equipou a {item_escolhido}!")

               elif "escudo" in item_escolhido.lower():    
                   print(f"\nVocê equipou o {item_escolhido}!")

               else:
                print(f"\nVocê usou ou examinou o item: {item_escolhido}")

               input("\nPressione ENTER para continuar...")

            else:
                 print("\nNúmero de item inválido!")
                 input("Pressione ENTER para continuar...")     

# itens

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
    "lendaria": [
        {"nome": "Cajado do Arquimago", "magia": 10}
    ]
}

# --- CONSUMÍVEIS ---
POCOES = [
    {"nome": "Poção de Cura", "tipo": "cura", "valor": 5},
    {"nome": "Poção de Mana", "tipo": "mana", "valor": 5}
]

# --- ITENS LIXO ---
LIXOS = [
    "Graveto Seco",
    "Pedra Redonda",
    "Bota Furada",
    "Osso Roído"
]