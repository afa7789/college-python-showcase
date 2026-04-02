# Regressão Logística — Classificação de Atividade Humana

Prática acadêmica de Inteligência Computacional. Utiliza regressão logística para classificar atividades humanas a partir de dados de sensores inerciais de smartphones.

## O que o projeto faz

Dado um conjunto de 561 features extraídas de acelerômetro e giroscópio, o modelo aprende a distinguir seis atividades:

- Caminhando
- Subindo escadas
- Descendo escadas
- Sentado
- Em pé
- Deitado

Acurácia obtida: ~98% no conjunto de teste.

## Arquivos principais

| Arquivo | Descrição |
|---|---|
| `Regressao_Logistica_V1.ipynb` | Notebook principal com análise exploratória e modelo |
| `regressao_logistica_v1.py` | Código Python extraído do notebook |
| `Human_Activity_Recognition_Using_Smartphones_Data.csv` | Dataset com ~10.000 registros e 562 colunas |

## Algoritmo

1. Carrega o CSV e codifica a coluna `Activity` com `LabelEncoder`
2. Calcula correlações entre features e gera histograma
3. Divide os dados com `StratifiedShuffleSplit` (70% treino / 30% teste)
4. Treina `LogisticRegression` padrão (regularização L2, solver lbfgs)
5. Avalia acurácia em treino e teste com `.score()`

## Como executar

```bash
# Instale as dependências
pip install pandas numpy scikit-learn matplotlib seaborn

# Coloque o CSV na mesma pasta e execute
python regressao_logistica_v1.py
```

Ou abra o notebook no VS Code / Jupyter:

```bash
jupyter notebook Regressao_Logistica_V1.ipynb
```

## Dependências

- Python 3.x
- pandas, numpy, scikit-learn, matplotlib, seaborn
