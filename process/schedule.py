import threading
import time
import datetime


def print_days(birthday):
    time.sleep(5)
    if birthday is None:
        print('Your birthday has passed, let\'s calculate the time before the next one')
    else:
        print(f'You have {birthday} till your next birthday')


year = int(input('Enter the year: '))
month = int(input('Enter the month: '))
days = int(input('Enter the day: '))

next_birthday = datetime.datetime(year=year, month=month, day=days, hour=0, minute=0, second=0)
if datetime.datetime.now() > next_birthday:
    day = None
else:
    day = next_birthday - datetime.datetime.now()

thread = threading.Thread(target=print_days, args=[day])
thread.start()
print('Processing...')
