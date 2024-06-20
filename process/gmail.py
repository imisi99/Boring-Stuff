import smtplib
import threading
import datetime

gmail = smtplib.SMTP('smtp.gmail.com', 587)

gmail.ehlo()

gmail.starttls()


sender = input('Enter your email address: ')
password = input('Enter the password for the account: ')
receiver = input('Enter the recipient email address: ')
birthday_year = int(input('Enter the year of the birthday(2000): '))
birthday_month = int(input('Enter the month of the birthday(01): '))
birthday_day = int(input('Enter the day of the birthday(01): '))


def send_email(user, passw, to):

    gmail.login(user, passw)

    gmail.sendmail(sender,
                   to,
                   f'Subject: Happy birthday.\n Hey man it\'s your birthday today.\nWish you all the good things '
                   f'in life!')

    gmail.quit()


send = threading.Thread(send_email, args=[sender, password, receiver])
birthday = datetime.datetime(year=birthday_year, month=birthday_month, day=birthday_day, hour=0, minute=0, second=0)
while datetime.datetime.now() <= birthday:
    text = 'Waiting for the day...'
    print(text, end='')
    print('\b' * len(text), end='')
if datetime.datetime.now() >= birthday:
    send.start()
