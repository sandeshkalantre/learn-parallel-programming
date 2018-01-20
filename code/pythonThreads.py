# Introduction to threads in Python
import time, threading

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.message = "Hello from a Thread!"

    def print_message(self):
        print(self.message)

    def run(self):
        print("Thread has started.") 
        for i in range(10):
            self.print_message()
            time.sleep(2)
        print("Thread has ended.")

print("Process started")
my_thread = MyThread()
my_thread.run()
print("Process ended") 
        

