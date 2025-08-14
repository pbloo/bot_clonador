import pyautogui
import time

from functions import *
from coordinates import (x, y, x_user, y_user, x_entrar, y_entrar, x_numeroPDV, y_numeroPDV, 
                         x_filtro, y_filtro, x_pontodevenda, y_pontodevenda, x_PDVs, y_PDVs, 
                         x_engrenagem, y_engrenagem, x_clonar, y_clonar, x_novoPDV, y_novoPDV)

openbrowser()
esperar()
selectprofile()
esperar()
newtab()
esperar()
openMpbank()
esperar()
loginMpbank()
enterPDV()
pdvNumber()
clonepdv()
filldata()