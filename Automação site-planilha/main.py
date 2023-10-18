from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import time

# Acessar o site
navegador = webdriver.Chrome()
navegador.get("https://www.terabyteshop.com.br/pc-gamer")
time.sleep(5)

# extrair os titulos e preços por xpath //tag[@atributo='valor']
titulos = navegador.find_elements(By.XPATH, "//a[@class='prod-name']")
precos = navegador.find_elements(By.XPATH, "//div[@class='prod-juros']")

# criar planilha
workbook = openpyxl.Workbook()
workbook.create_sheet("produtos")
pagina_produtos = workbook['produtos']
pagina_produtos['A1'].value = 'Produto'
pagina_produtos['B1'].value = 'Preço'
workbook.save('produtos.xlsx')

# colocar os dados na planilha
for titulo, preco in zip(titulos, precos):
    pagina_produtos.append([titulo.text, preco.text])

workbook.save('produtos.xlsx')
