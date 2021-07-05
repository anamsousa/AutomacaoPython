import rpa as r
import pyautogui as p

r.init()
r.url('http://www.google.com')
janela = p.getActiveWindow()
janela.maximize()
r.wait(2.0)
r.type('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input','RPA[enter]')
r.wait(2.0)
r.snap('page', 'rpa_page.png')
r.wait(2.0)
r.close()
