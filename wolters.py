

primeseries=[]

def addprimes(n):
    i=0
    adprime=0
    while i < len(n):
        adprime=adprime+n[i]
    return "Sum of prime numbers is",adprime


def find_prime(n):
    i=0


    while i< len(n):
        #print len(n)
       # print "Iteration ",i
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
    print addprimes(primeseries)



series=[1,23,3,4,56,7]
find_prime(series)



