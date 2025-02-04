#Passo 1; Abrir o sistema da empresa 
#pip install pyautogui
#pyautogui.click -> clicar
#pyautogui.press -> pressionar uma tecla
#pyautogui.write -> escrever
#pyautogui.hotkey("ctrl","c") -> dois botões copiar
#sistema https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

pyautogui.PAUSE = 0.5

# aperta a tecla windows
pyautogui.press("win")
# digitar o texto chrome
pyautogui.write("chrome")
# apertar enter
pyautogui.press("enter")
# entrar no usuário
pyautogui.click(x=947, y=617)
# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
#Passo 2; Fazer login
time.sleep(3)
pyautogui.click(x=695, y=462)
pyautogui.write(clecio590@gmail.com)
pyautogui.press("Tab")
pyautogui.write("minha senha aqui")
pyautogui.press("Tab")
pyautogui.press("enter")
#Passo 3; Importa a base de dados dos produstos
#pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")

time.sleep(2)

#Passo 4; Cadestrar 1 produto

for linha in tabela.index:
        
    pyautogui.click(x=657, y=332)

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("Tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("Tab")

    #Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("Tab")

    #Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("Tab")

    #Preço
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("Tab")

    #Custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("Tab")

    #Obs
    obs = tabela.loc[linha, "obs"]
    if obs != "nan":
        pyautogui.write(str(obs))
    pyautogui.press("Tab")

    #aperta botão de enviar
    pyautogui.press("enter")
    #voltar a tela
    pyautogui.scroll(10000)

#Passo 5; Repetir o passo 4 até acabar todos os produtos

