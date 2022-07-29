import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

##### Passo 1: Entendimento do Desafio
table = pd.read_csv(r"C:\Users\Victor\Downloads\advertising.csv")


#####  Passo 2: Entendimento da Área/Empresa
##### Passo 3: Extração/Obtenção de Dados

##### Passo 4: Ajuste de Dados (Tratamento/Limpeza)
#print(table.info())
#print(table.corr())

sns.heatmap(table.corr(), cmap="Wistia", annot=True)

plt.show()

##### Passo 5: Análise Exploratória
#y = quem você quer prever (vendas)
#x = é o resto total (quem você vai usar  para fazer a previsão)

y = table["Vendas"]
x = table[["TV","Radio","Jornal"]]

##### Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)
x_tr, x_ts, y_tr, y_ts = train_test_split(x,y)

#Cria inteligencia artifical
modelRegression = LinearRegression()
modelTreeDecision = RandomForestRegressor()

#Treina a inteligencia artifical
modelRegression.fit(x_tr,y_tr)
modelTreeDecision.fit(x_tr,y_tr)

##### Passo 7: Interpretação de Resultados

#fazer previsão
previsonRegression = modelRegression.predict(x_ts)
previsonTreeDecision = modelTreeDecision.predict(x_ts)

print(r2_score(y_ts, previsonRegression))
print(r2_score(y_ts,previsonTreeDecision))

new = pd.read_csv(r"C:\Users\Victor\Downloads\novos.csv")

print(modelTreeDecision.predict(new))