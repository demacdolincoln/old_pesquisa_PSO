* metricas - análise de metricas que possam indicar a estagnação de partículas
             metricas utilizadas:
                - Evolutionary State Estimation; baseado no paper [adaptative pso](../papers/adaptative_pso.pdf)

---
os resultados dos exercícios estão no formato .csv, que pode ser aberto tanto em algum editor ou visualizador de planilha eletrônica quanto no Pandas, onde devolve um objeto DataFrame.

ex. de uso com o Pandas:

~~~python
%matplotlib inline # no jupyter qtconsole

import pandas as pd

data = pd.read_csv('out.csv')

>>> data.columns
Index(['best_part', 'omg', 'f', 'sum_veloc', 'c2', 'c1', 'mean_fit',
       'best_fit'],
      dtype='object')

>>> data.filter(['omg', 'f', 'c1', 'c2']).plot() # gráfico linha

>>> data.filter(['omg', 'f', 'c1', 'c2']).plot.kde() # gráfico de densidade

data.describe() 
.# ^ descrição do DataFrame com um resumo de cada coluna, como valores mínimos, médios, quantidade, etc.
~~~

---

>:footnote: olhar melhor -> from scipy.signal import gaussian, general_gaussian
