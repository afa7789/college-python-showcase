# A* Pathfinding — Busca com Informação

Implementação do algoritmo de busca A* (A-estrela) aplicado a um grafo de cidades romenas, clássico problema do livro *Inteligência Artificial: Uma Abordagem Moderna* (Russell & Norvig).

## Arquivos

| Arquivo | Descrição |
|---|---|
| `A_Star_Node.py` | Implementação principal e funcional do A*. Lê `estrutura.json`, define a classe `Node` e executa a busca de Lugoj até Bucharest. |
| `A_Star_testes.py` | Extraído de `A* testes.ipynb`. Mesmo algoritmo, com prints de depuração passo a passo das listas aberta e fechada. |
| `A_Star.py` | Versão alternativa do A* para strings (Python 2). Busca permutações de letras para atingir uma palavra-objetivo. |
| `A_Star_Node_Original.py` | Rascunho inicial do algoritmo com erros intencionais — versão de estudo. |
| `estrutura.json` | Grafo das cidades: cada cidade lista seus vizinhos com distâncias reais e a distância em linha reta até Bucharest (heurística h). |
| `A* testes.ipynb` | Notebook Jupyter com os experimentos e saídas da execução passo a passo. |

## Como o algoritmo funciona

O A* combina dois custos para escolher qual nó explorar a seguir:

- **g** — custo real acumulado do início até o nó atual
- **h** — heurística: distância em linha reta até o destino (admissível, nunca superestima)
- **f = g + h** — custo estimado total; o nó com menor f é sempre expandido primeiro

O algoritmo mantém uma **lista aberta** (candidatos) e uma **lista fechada** (já visitados). A cada passo, remove o nó de menor f da lista aberta, expande seus filhos e repete até encontrar o destino.

## Como executar

Requer Python 3 e o arquivo `estrutura.json` no mesmo diretório.

```bash
# Execução principal (Lugoj -> Bucharest)
python A_Star_Node.py

# Versão com depuração detalhada
python A_Star_testes.py
```

O resultado exibe o caminho encontrado com os valores g, h e f de cada cidade.
