import pyautogui
import time as t


pyautogui.hotkey('win', 'r')
pyautogui.write('notepad')
pyautogui.hotkey('enter')
t.sleep(2)

frase = 'vc foi hackeado'


for i in range(len(frase)):
	pyautogui.write(frase[i])