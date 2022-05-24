from email.mime.text import MIMEText
import smtplib

from .keys import sender ,password

def send_email(name,email,subject,messege):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

    messege = f'My name is {name}\n {messege}'


    try:
        server.login(sender,password)
        msg=MIMEText(messege)
        msg['Subject']=subject
        msg['From']=sender
        msg['To']=email
        server.sendmail(sender,email,msg.as_string())


    except Exception as ex :
        return f'{ex}\nCheck your login or password!'

