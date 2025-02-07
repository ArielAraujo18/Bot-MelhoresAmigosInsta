import pyautogui
import time
import pandas as pd
import random

contador = 0
limite_diario = random.randint(50, 100)  # Define um limite diário aleatório
pyautogui.PAUSE = random.uniform(1.5, 3)

def espera():
    time.sleep(random.uniform(2, 5))

def pausa_longas():
    time.sleep(random.uniform(120, 600))  # Pausa de 2 a 10 minutos

# Logica para abrir o Insta
pyautogui.press("win")
pyautogui.write("Instagram")
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=68, y=595)
time.sleep(3)
pyautogui.click(x=1384, y=75)
espera()
pyautogui.click(x=948, y=550)
espera()
pyautogui.click(x=445, y=811)
espera()
pyautogui.click(x=1110, y=197)

# Carregar seguidores
df = pd.read_csv(r"C:\Users\Ariel\PycharmProjects\Scripts\automacao-insta\seguidores.csv")
seguidores = df["Username"].dropna().tolist()

espera()

for nome in seguidores:
    contador += 1
    if contador >= limite_diario:
        print("Limite diário atingido. Pausando execução.")
        break
    
    print(contador)
    pyautogui.write(nome)
    time.sleep(random.uniform(1, 2))
    pyautogui.click(x=1566, y=257)
    time.sleep(random.uniform(1.5, 3))
    pyautogui.click(x=1111, y=193)
    time.sleep(random.uniform(1, 2))
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    time.sleep(random.uniform(1, 2.5))
    
    if contador % random.randint(5, 10) == 0:
        print("Fazendo uma pausa longa para parecer mais humano...")
        pausa_longas()