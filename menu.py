def menu():

    while True:

           print("bem vindo ao meu RPG\n""escolha uma opcao:\n(1)comecar...\n(2)creditos...\n(3)sair...")
           op= input("op:")


           if op == "1":
              print("comecaondo boa aventura!")
              break
           elif op == "2":
               print("criado por william, obrigado por jogar!")
               break
           else:
               print("saindo...")
               exit()

    atributos_classes = {
        "guerreiro": {"vida": 10, "forca": 10, "magia": 5},
        "mago": {"vida": 10, "forca": 5, "magia": 10}
    }

    jogador = {}

    while True:
        # 1. A pergunta e o input ficam AQUI DENTRO para rodarem a cada tentativa!
        print("\nescolha uma classe:\n(a) guerreiro\n(b) mago")
        classe = input("classe: ")

        # 2. Verifica a escolha e mostra os status
        if classe == "a":
            classe_chave = "guerreiro"
            print("\nstatus do guerreiro:\n vida: 10\n forca: 10\n magia: 5")
        elif classe == "b":
            classe_chave = "mago"
            print("\nstatus do mago:\n vida: 10\n forca: 5\n magia: 10")
        else:
            print("\nOpção inválida! Tente novamente.")
            continue  # Volta para o começo do loop e pede a classe de novo

        # 3. Sub-menu de confirmação
        confirmar = input("\nDeseja confirmar essa classe?\n(a) Sim, começar jogo\n(b) Voltar e escolher outra\nOpção: ").lower().strip()

        if confirmar == "a":
            # Se confirmar, salva os dados no jogador e quebra o loop
            jogador = atributos_classes[classe_chave].copy()
            jogador["classe"] = classe_chave.capitalize()
            print(f"\nClasse {jogador['classe']} confirmada! Boa aventura!")
            return jogador  
        else:
            # Se escolher (b) ou qualquer outra coisa, avisa e DEIXA o loop recomeçar!
            print("\nVoltando para a escolha de classe...")