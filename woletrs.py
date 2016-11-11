import pdb
primeseries = []

def findprime(n):
    i=0
    while i<len(n):
       j =2
       flag=0
       while j < n[i]:
           if n[i]%j==0:
               flag=1
               break
           j += 1
       if flag == 0:
            primeseries.append(n[i])
       i += 1
    # print "prime numbers series is",primeseries
       addprime(primeseries)


def addprime(n):
    pdb
    i=0
    adprime = 0
    while i< len(n):
        adprime+=n[i]
    print adprime

def Main():
    pdb
    series = [1, 2, 4, 56, 78, 79, 23]
    findprime(series)

if __name__ == '__main__':
    Main()

