# College Python Showcase

Repositório com projetos de Machine Learning, IA e Ciência da Computação desenvolvidos durante a faculdade. Cada pasta contém um algoritmo ou técnica diferente, com notebooks Jupyter e scripts Python extraídos.

## Sumário

| Pasta | Tema | Algoritmo/Técnica |
|-------|------|-------------------|
| [Astart-nodes](./Astart-nodes) | Busca em Grafos | A* (A-Star) para pathfinding em cidades da Romênia |
| [college-task](./college-task) | Otimização | Algoritmo Genético + Sistema Imunológico Artificial |
| [genetico](./genetico) | Otimização | Algoritmo Genético na função benchmark F6(x,y) |
| [neural-network](./neural-network) | Deep Learning | Backpropagation manual, MNIST com Keras, predição de diabetes |
| [pca-ic-cefet](./pca-ic-cefet) | Redução de Dimensionalidade | PCA em dados de clientes wholesale |
| [regressaologistica](./regressaologistica) | Classificação | Regressão Logística para reconhecimento de atividades humanas |
| [regularizar-metricas](./regularizar-metricas) | Classificação | Regressão Logística com regularização L1/L2 e métricas |
| [sistema-imunologico](./sistema-imunologico) | Otimização | Sistema Imunológico Artificial para otimização multimodal |
| [svm-ic-cefet](./svm-ic-cefet) | Classificação | SVM com kernels (Linear, RBF, Polinomial) em qualidade de vinho |
| [tic-tac-toe-min-max](./tic-tac-toe-min-max) | Teoria dos Jogos | MinMax para jogo da velha ótimo |

## Estrutura

Cada projeto contém:
- **Notebook Jupyter** (`.ipynb`) — versão original interativa
- **Script Python** (`.py`) — código extraído do notebook para execução direta
- **README.md** — explicação do algoritmo, arquivos e como executar

## Como usar

```bash
# Instalar dependências comuns
pip install numpy pandas matplotlib scikit-learn

# Entrar em qualquer projeto e rodar
cd neural-network
python Backprop_Exercise_HW.py

# Ou abrir o notebook
jupyter notebook Backprop_Exercise_HW.ipynb
```
