def heap(a,n,i):
    b=i
    l=2*i+1
    r=2*i+2
    if l<n and a[l]>a[b]: b=l
    if r<n and a[r]>a[b]: b=r
    if b!=i:
        a[i],a[b]=a[b],a[i]
        heap(a,n,b)

def sort(a):
    n=len(a)
    for i in range(n//2-1,-1,-1):
        heap(a,n,i)
    for i in range(n-1,0,-1):
        a[0],a[i]=a[i],a[0]
        heap(a,i,0)

a=[12,11,13,5,6,7]
print("Before:",a)
sort(a)
print("After:",a)
