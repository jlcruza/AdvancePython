import threading
from threading import Thread

def evenNumber():
    for x in range(20):
        if x%2 == 0:
            print(x)
    a = threading.current_thread().getName()
    print(a)

t = Thread(target=evenNumber)
t.start()