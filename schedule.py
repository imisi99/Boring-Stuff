import threading
import time
import datetime


def print_name():
    time.sleep(5)
    print('My name is Imisioluwa')


thread = threading.Thread(target=print_name)
thread.start()
print('Done')

my_next_birthday = datetime.datetime(year=2025, month=1, day=24, hour=0, minute=0, second=0)

print(my_next_birthday - datetime.datetime.now())
