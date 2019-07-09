from threading import Thread


class MyThread(Thread):
    def run(self):
        print("Pyramid Quest")
        for x in range(0,5):
            for j in range(0,x+1):
                print("*", end=" ")
            print("\r")


obj = MyThread()
obj.start()