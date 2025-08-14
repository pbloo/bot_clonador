import time
import pyautogui
from coordinates import (x, y, x_user, y_user, x_entrar, y_entrar, x_numeroPDV, y_numeroPDV, 
                         x_filtro, y_filtro, x_pontodevenda, y_pontodevenda, x_PDVs, y_PDVs, 
                         x_engrenagem, y_engrenagem, x_clonar, y_clonar, x_novoPDV, y_novoPDV)

# Tempo de espera entre ações
def esperar():
    time.sleep(2)

# Move o mouse até o Google Chrome e clica duas vezes
def openbrowser():
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.doubleClick()

# Move o mouse para selecionar perfil
def selectprofile():
    pyautogui.moveTo(x_user, y_user, duration=1)
    pyautogui.click()

# Abre uma nova aba usando Ctrl + T
def newtab():
    print("Abrindo uma nova aba...")
    pyautogui.hotkey('ctrl', 't')

# Digita o endereço da URL e pressiona Enter
def openMpbank():
    url = 'https://app-mpagos-bank-front-prd.azurewebsites.net/app/pdv/listar'
    print(f"Digitar o endereço: {url}")
    pyautogui.typewrite(url)
    pyautogui.press('enter')
    print("Bank acessado.")

# Move o mouse para o botão "Entrar" e clica
def loginMpbank():
    pyautogui.moveTo(x_entrar, y_entrar, duration=1)
    esperar()
    pyautogui.click()
    esperar()
    pyautogui.click()
    esperar()

# Move o mouse para o campo "Nº do PDV" e clica.
def enterPDV():
    pyautogui.moveTo(x_pontodevenda, y_pontodevenda, duration=1)
    pyautogui.click()
    esperar()
    pyautogui.moveTo(x_PDVs, y_PDVs, duration=1)
    pyautogui.click()
    esperar()
    pyautogui.moveTo(x_numeroPDV, y_numeroPDV, duration=1)
    pyautogui.click()
    esperar()

# Digita o PDV e clica em "Filtro"
def pdvNumber():
    PDV = '3997'
    print(f"Digitar o PDV: {PDV}")
    pyautogui.typewrite(PDV)
    esperar()
    pyautogui.moveTo(x_filtro, y_filtro, duration=1)
    pyautogui.click()
    esperar()

#Começar a clonar o PDV"
def clonepdv():
    pyautogui.moveTo(x_engrenagem, y_engrenagem, duration=1)
    pyautogui.click()
    esperar()
    pyautogui.moveTo(x_clonar, y_clonar, duration=1)
    pyautogui.click()
    esperar()
    pyautogui.moveTo(x_novoPDV, y_novoPDV, duration=1)
    pyautogui.click()

# Preenche os campos do formulário e navega com TAB
def filldata():
    campos = [
        '3998',
        'LojaTerc_Claro_AAMCN__ILHÉUS_5EO2_3998',
        'PB000000000',
        'Claro',
        'CL4R0'
    ]

    for campo in campos:
        print(f"Preenchendo o campo: {campo}")
        pyautogui.typewrite(campo)  # Digita o valor no campo atual
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
    print("PDV clonado com sucesso!")