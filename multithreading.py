import threading
import time
import Queue

exitFlag=0
#j=0
fileno=1
threadList=[]
nameList=[]
class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        global fileno
        #global j
        #start_time = time.time()
        # while j < 5:
        for i in range(10):
            name = "File created2/File" + str(fileno) + ".txt"
            print "File " + name + "creating for thread" + str(threadID)
            f = open(name, "a")
            f.write("This is file " + str(fileno) + "\n")
            fileno += 1
            time.sleep(1)
        elapsed = round(time.time() - start_time, 1)  # Stopwatch stop
        print elapsed

def process_data(threadName, q):
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                data = q.get()
                queueLock.release()
                print "%s processing %s" % (threadName, data)
            else:
                queueLock.release()
            time.sleep(1)

for i in range(5):
    start_time = time.time()
    threadname="thread "+str(i)
    threadList.append(threadname)
    #threadList = ["Thread-1", "Thread-2", "Thread-3"]
    namel=str(i)
    nameList.append(namel)
    #nameList = ["One", "Two", "Three", "Four", "Five"]
    queueLock = threading.Lock()
    workQueue = Queue.Queue(10)
    threads = []
    threadID = 1


# Create new threads
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1
# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread"

