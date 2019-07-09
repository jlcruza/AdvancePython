import threading


class MyThread:

    def NaturalNo(self):
        if threading.current_thread().getName()=="Thread-1":
            for x in range(10):
                print(x)
        else:
            print("Not Thread-1")


obj = MyThread()
t = threading.Thread(target=obj.NaturalNo)
t.start()