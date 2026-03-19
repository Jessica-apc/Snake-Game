# 🐍 Snake Game (Pygame)

Um jogo estilo arcade desenvolvido em Python utilizando a biblioteca Pygame.
O objetivo é controlar a cobra/nave, desviar dos inimigos e sobreviver o máximo possível.

---

## Funcionalidades

* Menu interativo
* Sistema de movimentação do jogador
* Sistema de disparo (tiros)
* Inimigos gerados automaticamente
* Colisão entre entidades
* Sistema de vida do jogador
* Retorno ao menu após derrota
* Interface com instruções na tela

---

## Controles

* ↑ ↓ → ← : movimentação
* SPACE : atirar
* ENTER : selecionar opções do menu

---

## Conceitos aplicados

Este projeto utiliza conceitos importantes de programação:

* Padrão de Projeto Factory
* Padrão de Projeto Mediator
* Programação Orientada a Objetos (POO)
* Loop de jogo (Game Loop)
* Manipulação de eventos com Pygame

---

## Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/Jessica-apc/Snake-Game.git
```

2. Acesse a pasta do projeto:

```bash
cd Snake-Game
```

3. Instale as dependências:

```bash
pip install pygame
```

4. Execute o jogo:

```bash
python main.py
```

---

## Estrutura do projeto

```
Code/
│── Game.py
│── Menu.py
│── Level.py
│── Entity.py
│── EntityFactory.py
│── EntityMediator.py
│── Player.py
│── Enemy.py
│── PlayerShot.py
│── Background.py
│── Const.py

asset/
│── imagens
│── sons
```

---

## Melhorias futuras

* Sistema de pontuação
* Efeitos sonoros
* Animações de explosão
* Tela de Game Over mais elaborada
* Ranking de jogadores

---

## Autora

Jessica Aparecida

---

## Observação

Este projeto foi desenvolvido para fins de estudo e prática de desenvolvimento de jogos com Python.
