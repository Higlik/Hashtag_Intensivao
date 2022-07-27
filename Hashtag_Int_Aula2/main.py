#passo 1: Importar base de dados
import pandas as pd
import plotly.express as px

table = pd.read_csv(r"C:\Users\Victor\Downloads\telecom_users.csv")


#Passo 2: Visualizar a base dados
#excluindo dados inúteis
table = table.drop("Unnamed: 0", axis=1)
table = table.drop("IDCliente", axis=1)



#Passo 3: tratamento de dados
#Verifica os informações da tabela
print(table.info())

#Transforma a coluna TotalGasto para valor númerico(Int) e "coerce" forca a virar númerico caso ocorra erro.
table["TotalGasto"] = pd.to_numeric(table["TotalGasto"], errors="coerce")
print(table.info())

#Excluindo informações vazias
#axis 0 = linha
#axis 1 = coluna
table = table.dropna(how="all",axis=1)
table = table.dropna(how="any",axis=0)

print(table.info())



#Passo 4: Análise Inicial dos dados
#visualizando os cancelamentos
print(table["Churn"].value_counts())

#Visualização com formatação
print(table["Churn"].value_counts(normalize=True).map("{:.1%}".format))

#Passo 5: Descobrir os motivos do cancelamento
#analisando os dados e fazendo comparações

for column in table.columns:
    #cria o grafico
    graphic = px.histogram(table, x=column, color="Churn", text_auto=True)
    #Printa grafico
    graphic.show()

