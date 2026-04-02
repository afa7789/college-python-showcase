# Redução de Dimensionalidade com PCA

Exercícios de redução de dimensionalidade aplicados a dados de clientes de um distribuidor atacadista português.

## O que é

Aplicação de **PCA (Análise de Componentes Principais)** para reduzir a dimensionalidade de dados de gastos anuais em categorias de produtos (Fresh, Milk, Grocery, Frozen, Detergents_Paper, Delicassen). O projeto também avalia como PCA em pipeline com Regressão Logística afeta a acurácia na classificação de atividades humanas.

## Arquivos

| Arquivo | Descrição |
|---|---|
| `Dimensionality_Reduction_Exercises.ipynb` | Notebook com exercícios e saídas |
| `dimensionality_reduction.py` | Código Python extraído do notebook |
| `data/Wholesale_Customers_Data.csv` | Dados de clientes atacadistas |
| `data/Human_Activity_Recognition_Using_Smartphones_Data.csv` | Dados de reconhecimento de atividade |

## Algoritmo

1. **Pre-processamento**: remoção de colunas categóricas, log transform (skew > 0.75), escalonamento MinMaxScaler
2. **Pipeline sklearn**: `FunctionTransformer(log1p)` + `MinMaxScaler` encadeados
3. **PCA**: testado com 1 a 5 componentes; variância explicada e importância das features por dimensão
4. **KernelPCA (RBF)**: otimizado via `GridSearchCV` com scorer customizado (RMSE da transformação inversa)
5. **Avaliação em classificação**: pipeline `Scaler -> PCA -> LogisticRegression` com `StratifiedShuffleSplit` (3 folds), comparando StandardScaler, MinMaxScaler e RobustScaler

## Como executar

```bash
pip install pandas numpy scikit-learn seaborn matplotlib

# Executar o script extraído
python dimensionality_reduction.py

# Ou abrir o notebook
jupyter notebook Dimensionality_Reduction_Exercises.ipynb
```

Os arquivos de dados devem estar em `data/` relativo ao diretório de execução.
