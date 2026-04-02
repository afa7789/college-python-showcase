# Jogo da Velha com MinMax

Implementação do algoritmo MinMax para jogar Jogo da Velha de forma ótima. O computador nunca perde — ou vence ou empata.

## O que o projeto faz

1. Constrói a árvore completa de todas as partidas possíveis (até ~255.168 estados).
2. Aplica o algoritmo MinMax de baixo para cima: nós pares maximizam o valor; nós ímpares minimizam.
3. Permite uma partida interativa: o jogador entra com as coordenadas (linha, coluna) e o computador responde com a jogada de maior valor.

## Arquivos principais

| Arquivo | Descrição |
|---|---|
| `Jogo da Velha.ipynb` | Notebook principal com a implementação completa |
| `jogo_da_velha.py` | Código Python extraído do notebook |
| `testes.ipynb` | Experimentos auxiliares de estrutura de dados |

## Algoritmo MinMax

- **`CamposJogoDaVelha`** — representa uma célula do tabuleiro (quem marcou: 1=O, 2=X).
- **`JogoDaVelha`** — estado do jogo; gera filhos (jogadas possíveis) e verifica vitória.
- **`MinMax`**
  - `construirEstrutura()` — expande toda a árvore em profundidade.
  - `GerarValoresDasPartidas()` — propaga valores (+1 computador vence, -1 jogador vence, 0 empate).
  - `partida()` — loop de jogo; chama `jogadaAlgoritmo()` e `jogadaJogador()` alternadamente.

## Como executar

```bash
pip install jupyter
jupyter notebook "Jogo da Velha.ipynb"
# ou diretamente (requer entrada no terminal):
python jogo_da_velha.py
```

A construção da árvore demora alguns segundos. Quando aparecer o tabuleiro, informe a posição desejada como dois números separados por espaço (ex: `0 2`).
