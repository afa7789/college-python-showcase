# Algoritmos de Computação Natural

Coleção de dois algoritmos bioinspirados implementados em Python para otimização de funções matemáticas.

## Algoritmos

### Algoritmo Genético (`genetico.py`)
Otimiza a função `f6(x, y) = sqrt(x)*sin(x)*sqrt(y)*sin(y)` usando operadores evolutivos:
- **Seleção por roleta**: indivíduos com maior fitness têm maior chance de reprodução
- **Cruzamento aritmético**: filhos gerados por combinação linear dos pais (taxa: 60%)
- **Mutação gaussiana**: perturbação aleatória com distribuição normal truncada (taxa: 10%)
- 1000 indivíduos, 100 gerações

### Sistema Imunológico Artificial (`sistema-imunologico.py`)
Baseado no algoritmo CLONALG, também otimiza `f6(x, y)`:
- **Clonagem**: cada anticorpo gera clones proporcionais ao tamanho da população (Beta = 10%)
- **Hipermutação**: clones com fitness baixo sofrem mutação gaussiana
- **Seleção do melhor clone**: substitui o anticorpo original pelo melhor resultado
- 500 indivíduos, 50 iterações

## Arquivos

| Arquivo | Descrição |
|---|---|
| `genetico.py` | Algoritmo Genético extraído de `Genetico.ipynb` |
| `sistema-imunologico.py` | Sistema Imunológico extraído de `sistema-imunologico.ipynb` |
| `Genetico.ipynb` | Notebook original com visualizações Plotly |
| `sistema-imunologico.ipynb` | Notebook original com visualizações Matplotlib |

## Como Executar

Instale as dependências:
```bash
pip install numpy matplotlib
```

Execute cada algoritmo:
```bash
python genetico.py
python sistema-imunologico.py
```

Ambos convergem para o máximo global da função em torno de `(7.9, 7.9)`.
O sistema imunológico exibe gráficos de contorno a cada 5 iterações mostrando a convergência.
