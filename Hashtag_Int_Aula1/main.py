import pyautogui
import pyperclip
import time
import pandas as pd

#parametro para aguardar e executar cada linha de código
pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=346, y=270, clicks = 2)

time.sleep(5)

pyautogui.click(x=346, y=270)

pyautogui.click(x=1711, y=162)

time.sleep(3)

pyautogui.click(x=1475, y=598)

time.sleep(10)

tabela = pd.read_excel(r"C:\Users\Victor\Downloads\Vendas - Dez.xlsx")

quantidade = tabela["Quantidade"].sum()

faturamento = tabela["Valor Final"].sum()

pyautogui.hotkey("ctrl", "t")

pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")

time.sleep(8)

pyautogui.click(x=94, y=175)

pyautogui.write("victor.silva.franca3@gmai.com")
pyautogui.press("tab")
pyautogui.press("tab")

pyautogui.write("Relatório de vendas")
pyautogui.press("tab")

conteudo = f"""
resultado das vendas:

faturamento = R${faturamento:,.2f} 
quantidade de produtos vendidos = {quantidade:,}

Victor França.

"""

pyautogui.write(conteudo)
pyautogui.hotkey("ctrl", "enter")




