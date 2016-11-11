import time
import pdb
import Queue
import threading
import thread
import time
j=0
fileno=1
def file_create(thread_name,delay):
    #pdb.set_trace()
    global fileno
    global j
    start_time = time.time()
    #while j < 5:
    for i in range(10):
        name = "File created2/File" + str(fileno) + ".txt"
        print "File "+name+"creating for thread" + thread_name
        f = open(name, "a")
        f.write("This is file " + str(fileno) + "\n")
        fileno+=1
        time.sleep(delay)

        #call_thread()
    j += 1
    elapsed = round(time.time() - start_time, 1)  # Stopwatch stop
    print elapsed


def call_thread():
    t=threading._start_new_thread(file_create("thread1", 1),2)
    #t.start_new_thread(file_create("thread1", 1))
    '''thread.start_new_thread(file_create("thread2", 1))
    thread.start_new_thread(file_create("thread3", 1))
    thread.start_new_thread(file_create("thread4", 1))
    thread.start_new_thread(file_create("thread5", 1))'''



call_thread()


