# SVM com Kernels — Classificação de Qualidade de Vinho

Prática de Machine Learning do CEFET utilizando Support Vector Machine (SVM) para classificar vinhos como tinto ou branco com base em características físico-químicas.

## O que o projeto faz

1. Carrega o dataset `Wine_Quality_Data.csv` com atributos como acidez, pH, teor alcoólico etc.
2. Calcula a correlação de Pearson entre cada atributo e a cor do vinho.
3. Seleciona as duas features de maior correlação e normaliza com `MinMaxScaler`.
4. Treina e compara três abordagens de SVM:
   - **LinearSVC** — fronteira de decisão linear.
   - **SVC (kernel RBF)** — fronteira não-linear; explora diferentes valores de `gamma` (0.5, 1, 2, 10) e `C` (0.1, 1, 10).
   - **Nystroem + SGDClassifier** — aproximação de kernel para datasets maiores, comparando custo computacional com SVC completo.
5. Plota a fronteira de decisão para cada modelo.

## Arquivos principais

| Arquivo | Descrição |
|---|---|
| `SVM_Kernels_HW.ipynb` | Notebook original com código e visualizações |
| `svm_kernels.py` | Código Python extraído do notebook |
| `Wine_Quality_Data.csv` | Dataset com ~6500 amostras de vinho |

## Algoritmo

O SVM encontra o hiperplano de máxima margem entre classes. O kernel RBF mapeia os dados para um espaço de maior dimensão, permitindo fronteiras não-lineares. O parâmetro `gamma` controla o raio de influência de cada ponto; `C` controla a penalidade por erros de classificação. A aproximação de Nystroem reduz o custo de O(n³) para O(n) ao aproximar a matriz de kernel.

## Como executar

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
jupyter notebook SVM_Kernels_HW.ipynb
# ou diretamente:
python svm_kernels.py
```
