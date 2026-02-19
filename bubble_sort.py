import random
import time
#l = [4, 20, 12, 21, 1]
def bubble_sort(l):
    n=len(l)
    for i in range(n):
        for j in range(0,n-i-1):
            if l[j+1]<l[j]:
                l[j],l[j+1]=l[j+1],l[j]    
    return l

n=[random.randint(200,300)for _ in range(6)]
for i in n:
    l =[random.randint(1,20)for _ in range(i)]
    start_time=time.time()

    end_time=time.time()
    print(bubble_sort(l))
    print("execution time:",end_time - start_time,"seconds")