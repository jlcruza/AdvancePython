import threading

t = threading.current_thread().getName()
print(t)    # output MainThread

threading.current_thread().name = "Another"
print(threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    for x in range(10):
        if x%2==0:
            print(x)

else:
    print("Not Main Thread")
