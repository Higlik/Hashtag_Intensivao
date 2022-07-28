from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import openpyxl
import numpy


##### Passo 1: Pegar a cotação do dólar
nav = webdriver.Chrome()

#Entrando no google
nav.get("https://www.google.com.br/")

#Encontrando um elemento xpath e inserindo o texto
nav.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação dolar")
nav.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#Pegando informação do elemento
cot_dollar = nav.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cot_dollar)

##### Passo 2: Pegar a cotação do euro
nav.get("https://www.google.com.br/")

#Encontrando um elemento xpath e inserindo o texto
nav.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação euro")
nav.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#Pegando informação do elemento
cot_euro = nav.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cot_euro)

##### Passo 3: Pegar a cotação do ouro
nav.get("https://www.melhorcambio.com/ouro-hoje#:~:text=O%20valor%20do%20grama%20do,em%20R%24%20292%2C87.")
#Pegando informação do elemento
cot_gold = nav.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
#Trocando a virgula por ponto
cot_gold = cot_gold.replace(",",".")
print(cot_gold)

#fechando o navegador
nav.quit()

##### Passo 4: Atualizar a base de dados
table = pd.read_excel(r"C:\Users\Victor\Downloads\Produtos.xlsx")
#Visualizar base de dados
print(table)


##### Passo 5: Recalcular os preços
#Atualizar cotação
table.loc[table["Moeda"]=="Dolár", "Cotação"] = float(cot_dollar)
table.loc[table["Moeda"]=="Euro", "Cotação"] = float(cot_euro)
table.loc[table["Moeda"]=="Ouro", "Cotação"] = float(cot_gold)

print(table)

#Preço de compra = preço original * cotação

table["Preço de Compra"] = table["Preço Original"] * table["Cotação"]

#Preço de venda = preço de compra * margem
table["Preço de Venda"] = table["Preço de Compra"] * table["Margem"]

print(table)

##### Passo 6: Exportar a base de dados
table.to_excel("Produtos Novos.xlsx", index=False)