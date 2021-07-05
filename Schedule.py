import schedule
import time
import smtplib
from Robo01 import Botrobo01
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


try:
    print('Iniciou...')

    schedule.every().day.at("06:43").do(Botrobo01)


    while True:
        schedule.run_pending()
        time.sleep(1)

except IndexError as e:
    # enviando dado por email

    # texto do email
    texto_email = 'O bot notepad falhou, por gentileza, verificar.'
                  f'Erro:{e}'

    # email remetente, senha, destinatário
    de = 'p.anamsousa@gmail.com'
    senha = '****'
    para = 'p.anamsousa@gmail.com'
    # para02 = ''

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = de
    message['To'] = para
    # message['To'] = para02
    message['Subject'] = 'Cotação do dolar'  # Título do e-mail

    # Corpo do E-mail com anexos
    message.attach(MIMEText(texto_email, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # Usuário do Gmail com porta
    session.starttls()  # Habilita a segurança
    session.login(de, senha)  # Login e senha de quem envia o e-mail
    texto = message.as_string()
    session.sendmail(de, para, texto)
    session.quit()
