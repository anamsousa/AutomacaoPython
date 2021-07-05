import pyautogui as p

def Botrobo01():
    p.FAILSAFE = False
    p.hotkey('win','r')
    p.sleep(1)
    p.typewrite('notepad')
    p.sleep(2)
    p.press('enter')
    p.sleep(2)
    p.typewrite('Hello, im a bot')
    p.sleep(2)
    valor = p.getActiveWindow()
    valor.close()
    p.press('right')
    p.sleep(2)
    p.press('enter')

#robo01()

#p.sleep(2)
#print(p.position())