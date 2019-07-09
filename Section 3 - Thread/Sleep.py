from threading import Thread
import threading
from time import sleep


def natural():
    print(threading.current_thread().getName(), " Has Started")
    sleep(2)
    for x in range(10):
        print(x)

    print(threading.current_thread().getName(), " Has Ended")


t1 = Thread(target=natural())
t2 = Thread(target=natural())
t1.start()
t2.start()