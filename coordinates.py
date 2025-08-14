import pyautogui
import time

print("Mova o mouse para o ícone do navegador e aguarde 5 segundos...")
time.sleep(5)  # Tempo para você mover o mouse até o ícone

x, y = pyautogui.position()  # Captura a posição atual do mouse
print(f"As coordenadas do ícone do navegador são: x={x}, y={y}")



# Coordenadas
x, y = 43, 313  # Coordenadas do ícone do navegador (Substitua com as coordenadas reais do ícone)
x_user, y_user = 762, 594 # Coordenadas para escolher o usuário
x_entrar, y_entrar = 1330, 652 # Coordenadas do botão "entrar"
x_numeroPDV, y_numeroPDV = 942, 299 # Coordenadas para o campo "Nº do PDV"
x_filtro, y_filtro = 1743, 353 # Coordenadas para o botão "Filtro"
x_pontodevenda, y_pontodevenda = 111, 286 # Coordenadas para o botão "Ponto de Venda"
x_PDVs, y_PDVs = 86, 367 # Coordenadas para o botão "PDVs"
x_engrenagem, y_engrenagem = 316, 506 # Coordenadas para as configurações do PDV
x_clonar, y_clonar = 369, 593 # Coordenadas para "Clonar"
x_novoPDV, y_novoPDV = 648, 364 # Coordenadas para o campo "Novo Pdv"