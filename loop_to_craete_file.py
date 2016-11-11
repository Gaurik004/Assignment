import time
import pdb


def file_create():
    pdb.set_trace()
    start_time=time.time()
    for i in range(50):

        name= "File created/File"+str(i)+".txt"
        f = open(name, "a")
        f.write("This is file " + str(i) + "\n")
    elapsed = round(time.time() - start_time, 1)  # Stopwatch stop
    print elapsed


file_create()

