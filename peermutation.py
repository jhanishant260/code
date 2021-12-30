"have to make it better"
a=["a","b","c"]
high=0
low=0
length=len(a)
d=set()
def permute(a,length,low,high):

    d.add(str(a))
    print("inside permute")
    print(a)
    if low==length:
        print("inside if ")
        low=low-1
        return a
    else:
        print("inside else")
        for i in range(length):
            print("low",low)
            print("i",i)
            print("before","a[low]=",a[low],"a[i]",a[i])
            a[low],a[i]=a[i],a[low]
            permute(a,length,low+1,high)
            print("after permute")
            print(a)
            a[i],a[low]=a[low],a[i]
permute(a,length,low,high)
print(d)
print(len(d))
