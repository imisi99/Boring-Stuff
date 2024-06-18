import smtplib
import threading

gmail = smtplib.SMTP('smtp.gmail.com', 587)

gmail.ehlo()

gmail.starttls()


sender = input('Enter your email address: ')
password = input('Enter the password for the account: ')
receiver = input('Enter the recipient email address: ')
subject = input('Enter the subject of the mail: ')
message = input('Enter the message you wish to deliver: ')


def send_email(sender, password, to, subject, msg):

    gmail.login(sender, password)

    gmail.sendmail(sender,
                   to,
                   f'Subject: {subject}\n {msg}')

    gmail.quit()


send = threading.Thread(send_email, args=[sender, password, receiver, subject, message])

send.start()
