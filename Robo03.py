import rpa as r
import pyautogui as p
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#capturando informação do site
r.init()
r.url('https://www.melhorcambio.com/dolar-hoje')
p.sleep(10)
janela = p.getActiveWindow()
janela.maximize()
dolar_comercial = r.read('//*[@id="comercial"]')
r.close()

#enviando dado por email

#texto do email
texto_email = dolar_comercial + ' Hoje: ' + str(pd.Timestamp('today'))

# email remetente, senha, destinatário
de = 'p.anamsousa@gmail.com'
senha = '*******'
para = 'p.anamsousa@gmail.com'
#para02 = ''

# Setup the MIME
message = MIMEMultipart()
message['From'] = de
message['To'] = para
#message['To'] = para02
message['Subject'] = 'Cotação do dolar'   #Título do e-mail

# Corpo do E-mail com anexos
message.attach(MIMEText(texto_email, 'plain'))

# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  # Usuário do Gmail com porta
session.starttls()  # Habilita a segurança
session.login(de, senha)  # Login e senha de quem envia o e-mail
texto = message.as_string()
session.sendmail(de, para, texto)
session.quit()




