# Algoritmo Genético — Otimização da Função f6(x, y)

## O que é

Implementação de um algoritmo genético para maximizar a função de benchmark **f6(x, y)**:

```
f6(x,y) = 0.5 - ( sin(√(x²+y²))² - 0.5 ) / ( 1 + 0.001·(x²+y²) )²
```

O domínio de busca é `[-10, 10]` para ambas as variáveis.

## Arquivos

| Arquivo | Descrição |
|---|---|
| `Genetico.ipynb` | Notebook original com visualizações interativas (Plotly) |
| `Genetico.py` | Código Python extraído, executável diretamente |

## Visão geral do algoritmo

1. **Inicialização** — população de 1000 indivíduos com valores aleatórios em `[-10, 10]`
2. **Avaliação (fitness)** — calcula f6(x, y) para cada indivíduo
3. **Seleção** — roleta ponderada pelo somatório acumulado do fitness
4. **Cruzamento** — crossover aritmético com taxa de 70% e fator alpha aleatório
5. **Mutação** — perturbação gaussiana truncada com taxa de 20% e desvio padrão 3
6. **Iteração** — repete por 100 gerações

A cada geração são registrados o maior, a média e o menor valor de fitness da população.

## Como executar

```bash
# Instalar dependências
pip install numpy plotly

# Rodar o script
python Genetico.py
```

O script imprime os valores de fitness da geração final e salva o gráfico de evolução em `fitness_evolution.html`.

Para visualizar o notebook com os gráficos interativos:

```bash
pip install jupyter plotly
jupyter notebook Genetico.ipynb
```
