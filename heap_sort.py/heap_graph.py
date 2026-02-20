import time 
import random
import matplotlib.pyplot as plt

def heapify(arr,n,i): 
    largest=i
    left= 2*i+1
    right=2*i+2

    if left <n and arr[left] > arr[largest]:
        largest=left

    if right <n and arr[right] > arr[largest]:
        largest=right

    if largest !=i:
        arr[i],arr[largest] = arr[largest], arr[i]
        heapify (arr,n,largest)  



def heap_sort(arr):
    n=len(arr) 

    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)



arr=[12,11,13,5,6,7]

heap_sort(arr)
print("Sorted array",arr)     

n_list=[5000,6000,7000,8000,9000]
sort_time=[]
for n in n_list:
    arr=[random.randint(1,100) for _ in range(n)]
    start_time=time.time()
    heap_sort(arr)
    end_time=time.time()
    sort_time.append(end_time-start_time)

plt.plot(n_list,sort_time,marker='x')
plt.xlabel("number of elements(n)")
plt.ylabel("time taken (seconds)")
plt.title("insertion sort Sort: time complexity analysis ")
plt.grid(True)
plt.savefig("insertion_sort_time_complexity.png",dpi=300,bbox_inches='tight')
plt.show()