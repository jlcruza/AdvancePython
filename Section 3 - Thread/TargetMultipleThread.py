from threading import Thread
import threading


def even_odd():
    evenNo()
    print(threading.current_thread().getName())
    oddNo()


def evenNo():
    for x in range(10):
        if(x%2 is 0):
            print(x)


def oddNo():
    for x in range(10):
        if(x%2 is not 0):
            print(x)


t = Thread(name="EvenOddThread", target= even_odd)
t.start()