import pandas as pd
import pyautogui as p
import rpa as r


#Abrindo Sistema
r.init()
r.url('')
janela = p.getActiveWindow()
janela.maximize()
p.sleep(5)
#Logando ambiente
p.click(-386, 270, duration=0.25)
p.write('380.smega')
p.sleep(2)
p.hotkey('tab')
p.write(#senha)
p.click(-449, 466, duration=0.25)
p.sleep(15)
#Logando no Sistema
p.click(-1517, 334, duration=0.25)
p.sleep(10)
p.click(-657, 275, duration=0.25)
p.write(#usuario)
p.sleep(1)
p.hotkey('tab')
p.write(#senha)
p.hotkey('enter')
p.sleep(10)
#Selecionando Filial
p.write('100')
p.hotkey('enter')
p.sleep(5)
#Abrindo tela para envio dos dados 
p.click(-1500,2, duration=0.25)
p.write('Orcamentos')
p.sleep(1)
p.click(-1510, 213, duration=0.25)
p.sleep(15)
p.click(-1139, 259, duration=0.25)
p.sleep(2)
p.click(-583, 49, duration=0.25)
p.click(-489, 99, duration=0.25)
p.sleep(5)
p.click(-1087, 28, duration=0.25)
p.sleep(5)
p.click(-1157, 400, duration=0.25)
p.sleep(5)
p.click(-358, 1, duration=0.25)
p.sleep(2)
p.click(-439, 206, duration=0.25)
p.sleep(2)
p.click(1090, 369, duration=0.25)



#trabalhando os dados
dados = pd.read_excel('teste.xlsx', sheet_name='Sheet1')
df = pd.DataFrame(dados, columns=["colunaenvio"])

#Inserindo dados na tabela do sistema

for i in range(df.shape[0]):
     if (i % 3 == 0) & (i != 0):
          p.click(1090, 348)
          p.sleep(3)
          p.scroll(-1)
          p.sleep(5)
          p.click(1091, 365, duration=0.25)
     p.write(str(df.iloc[i,0]))
     p.hotkey('enter')
     p.sleep(3)
     p.hotkey('down')










