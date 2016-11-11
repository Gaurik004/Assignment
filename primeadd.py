import pdb

primeseries=[]
adprime=0

def find_prime(n):
    i=0
    global adprime
    while i< len(n):
        flag = 0
        j = 2
        while j<n[i]:
            if n[i]%j ==0:
                flag=1
            j+=1
        if flag==0:
                primeseries.append(n[i])

        i+=1
    print "prime numbers list from series is",primeseries
    #pdb.set_trace()
    addprimes(primeseries)
    print adprime

def addprimes(n):
    i=0
    global adprime
    #pdb.set_trace()
    print n
    while i < len(n):
        adprime=adprime+n[i]
        print "Sum of prime numbers is",adprime
        i+=1




series=[1,23,3,4,56,7,2,6,9,17]
find_prime(series)