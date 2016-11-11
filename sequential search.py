def Seq_search(alist,val):
    pos=0
    found=False
    while pos < len(alist) and not found:
        if alist[pos]==val:
            found=True

        else:
            pos+=1
    if found==True:
        print "Found",val,"in the sequence"
        print alist
    else :
        print "Not Found" , val,"in the sequence"

alist=[49,4,89,56,47]
Seq_search(alist,8)

