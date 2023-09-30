import pyautogui
import time
import pandas

"""
STEP 01: Abir o chrome
STEP 02: Fazer login
STEP 03: Importar a base de dados do produto
STEP 04: Cadastrar produtos
"""
# Abrir o navegador (chrome)
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# STEP 1-2 Entrar no sistema e Fazer Login
pyautogui.click(x=1359, y=393)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha aqui")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# STEP 3: Importar CSV com Pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4:Cadastrar Pordutos
for linha in tabela.index:
    pyautogui.click(x=987, y=279)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    # Apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
