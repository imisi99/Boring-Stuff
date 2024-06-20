# this is a timer program that alerts you by opening a file when done
import subprocess
import sys
import time

if len(sys.argv) < 2:
    print('No input for timer, add timer in command line arg')
    sys.exit()

else:
    timer = int(sys.argv[1])

    while timer > 0:
        print(timer)
        time.sleep(1)
        timer -= 1

    text = open('timer.txt', 'w')
    text.write('Get to work!')
    subprocess.Popen(['start', 'timer.txt'], shell=True)
