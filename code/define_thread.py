import threading

def func(i):
    print("func called by thread" + str(i))

thread_list = []
for i in range(20):
    t = threading.Thread(target=func,args=(i,))
    thread_list.append(t)
    t.start()
    t.join()
