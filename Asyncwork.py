import threading
import time

class Asyncwork(threading.Thread):
    def __init__(self,text,out):
        threading.Thread.__init__(self,text,out)
        self.text=text
        self.out=out
    def __run__(self):
        f=open(self.out,"a")
        f.write(self.text+"\n")
        f.close()
        time.sleep(2)
        print "Finished background file write to "+self.out


def Main():
    message = raw_input("enter a string to store")
    background = Asyncwork(message, "out.txt")
    background.start()
    print "The program can contbue to run until it writes in another thread"
    print 100 + 400 + 500
    background.join()
    print "waited until thread finished"

if __name__=='__main__':
    Main()