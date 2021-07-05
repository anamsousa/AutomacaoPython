import pyautogui as p


#Nao funcionou

p.doubleClick(x=25, y=656)
p.sleep(5)
janela = p.getActiveWindow()
janela.maximize()
p.write('www.udemy.com')
p.press('enter')
p.sleep(3)

localPesq = p.locateAllOnScreen('Pesquisa.PNG', confidence=0.9)
localPesquisa = p.center(localPesq)
xPesquisa, yPesquisa = localPesquisa
p.moveTo(xPesquisa, yPesquisa)
p.click(xPesquisa, yPesquisa)
p.sleep(1)
p.write('Charles Lima')
p.press('enter')
# p.sleep(2)
# print(p.position())
