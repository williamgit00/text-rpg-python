from menu import menu
from jogador import MENU_JOGADOR
from combate import iniciar_combate
from dados import dados
from itens import ESPADAS, CAJADOS, POCOES, LIXOS
from narrativa import MOBS_POR_CIDADE

def rodar_teste():
    print("=== INICIANDO TESTE DO RPG ===")
    
   
    jogador = menu()
    
  
    if not jogador:
        print("\n[ERRO DE TESTE]: A função menu() não retornou os dados do jogador!")
        return

    print("\n[TESTE]: Classe criada com sucesso!")
    print(f"[TESTE]: Dados recebidos do menu.py -> {jogador}")
    
  
    print("\nAbrindo o Menu do Jogador...")
    MENU_JOGADOR(jogador)

if __name__ == "__main__":
    rodar_teste()