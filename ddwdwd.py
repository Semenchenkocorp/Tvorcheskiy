import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def process_csv_file(path):
    # Чтение файла и группировка данных
    df = pd.read_csv(path, delimiter=';', encoding='utf-8') # Добавлен параметр encoding
    fff1 = df[df['event'] == 'view']
    fff2 = df[df['event'] == 'click']
    fff3 = pd.DataFrame()
    fff3['view'] = fff1['platform'].value_counts()
    fff3['click'] = fff2['platform'].value_counts()
    fff3 = fff3.reset_index()
    fff3.rename(columns={'index': 'platform'}, inplace = True )
    grouped = fff3
    return grouped

def send_email(email, password, recipient, data):
    # Создание сообщения
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient
    msg['Subject'] = 'Отчет о взаимодействии с сервисом'
    html_data = data.to_html()
    msg.attach(MIMEText(html_data, 'html'))

    # Отправка сообщения
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, recipient, msg.as_string())
    server.quit()

path = 'C:/Users/amtal/PycharmProjects/tp2/ttt.csv'
email = 'ngusev071@gmail.com'
password = 'zrcgjifbpgojohyk'
recipient = 'semenchenkocorp@mail.ru'
grouped_data = process_csv_file(path)
send_email(email, password, recipient, grouped_data)

