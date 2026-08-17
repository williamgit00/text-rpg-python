# ⚔️ RPG de Texto em Python

Um jogo de RPG jogável via terminal desenvolvido em Python, focado no aprendizado prático de **lógica de programação, modularização e estruturas de dados**.

---

## 🚀 Funcionalidades

- **Criação de Personagem:** Escolha de classes com atribuição dinâmica de atributos (Vida, Força, Magia).
- **Sistema de Eventos (Dado do Destino):** Rola dados dinâmicos para sorteio de itens, poções e falhas críticas.
- **Sistema de Combate:** Lógica de turnos contra mobs categorizados por dificuldade/cidade.
- **Gerenciamento de Inventário:** Coleta de armas (normais, épicas e lendárias) e consumíveis.
- **Tratamento de Estado:** Verificação de vitória, debuffs e mecânica de Game Over.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- Biblioteca nativa `random` para geração de probabilidades e encontros.

---

## 📂 Estrutura do Projeto

* `main.py`: Loop principal e fluxo do jogo.
* `menu.py`: Criação e seleção de classes do jogador.
* `combate.py`: Regras do turno de batalha e mecânica de dano/morte.
* `dados.py`: Lógica do Dado do Destino e distribuição de drops.
* `itens.py`: Base de dados de armas, poções e itens lixo.
* `mobs.py`: Atributos e características dos inimigos por região.

---
