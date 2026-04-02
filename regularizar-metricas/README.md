# Regularização e Métricas — Regressão Logística Avançada

Extensão da prática de regressão logística, desenvolvida em conjunto com Jonathan Henrique. O foco é comparar diferentes tipos de regularização (L1 e L2) e avaliar os modelos com métricas completas de classificação.

Repositório anterior: [regressaologistica](https://github.com/afa7789/regressaologistica)

## O que o projeto faz

Usando o mesmo dataset de atividade humana com smartphones, o notebook:

1. Treina três modelos: sem regularização, L1 e L2
2. Compara os coeficientes dos modelos visualmente
3. Aplica seleção de features por variância (`VarianceThreshold`)
4. Testa diferentes solvers (lbfgs, newton-cg)
5. Calcula e compara métricas detalhadas entre todos os modelos

## Arquivos principais

| Arquivo | Descrição |
|---|---|
| `Regressao_Logistica_V2.ipynb` | Notebook com análise completa |
| `regressao_logistica_v2.py` | Código Python extraído do notebook |
| `Human_Activity_Recognition_Using_Smartphones_Data.csv` | Dataset com ~10.000 registros e 562 colunas |

## Algoritmo

1. Pré-processamento idêntico ao V1 (LabelEncoder + StratifiedShuffleSplit)
2. Treinamento de três modelos com `LogisticRegressionCV`:
   - `lr`: sem regularização explícita
   - `lr_l1`: regularização L1 (solver liblinear)
   - `lr_l2`: regularização L2 (solver lbfgs)
3. Comparação visual dos coeficientes por classe
4. Seleção de features com `VarianceThreshold(threshold=0.21)`
5. Retreino com features reduzidas e solver newton-cg
6. Métricas calculadas: precisão, recall, F-score, acurácia e AUC-ROC
7. Matrizes de confusão plotadas com heatmap

## Como executar

```bash
# Instale as dependências
pip install pandas numpy scikit-learn matplotlib seaborn

# Execute com o CSV na mesma pasta
python regressao_logistica_v2.py
```

Ou abra o notebook:

```bash
jupyter notebook Regressao_Logistica_V2.ipynb
```

## Dependências

- Python 3.x
- pandas, numpy, scikit-learn, matplotlib, seaborn
