import threading

shared_var_without_lock = 0
shared_var_with_lock = 0
COUNT = 10000

shared_var_lock = threading.Lock()

def increment_with_lock():
    global shared_var_with_lock
    for i in range(COUNT):
        shared_var_lock.acquire()
        shared_var_with_lock += 1
        shared_var_lock.release()

def decrement_with_lock():
    global shared_var_with_lock
    for i in range(COUNT):
        shared_var_lock.acquire()
        shared_var_with_lock -= 1
        shared_var_lock.release()

def increment_without_lock():
    global shared_var_without_lock
    for i in range(COUNT):
        shared_var_without_lock += 1

def decrement_without_lock():
    global shared_var_without_lock
    for i in range(COUNT):
        shared_var_without_lock -= 1

t1 = threading.Thread(target = increment_with_lock)
t2 = threading.Thread(target = decrement_with_lock)

t3 = threading.Thread(target = increment_without_lock)
t4 = threading.Thread(target = decrement_without_lock)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print("Shared var with lock",shared_var_with_lock)
print("Shared var without lock",shared_var_without_lock)
