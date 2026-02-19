import time 
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        n = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > n:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = n
    return arr

n_list=[5000,6000,7000,8000,9000]
sort_time=[]
for n in n_list:
    arr=[random.randint(1,100) for _ in range(n)]
    start_time=time.time()
    insertion_sort(arr)
    end_time=time.time()
    sort_time.append(end_time-start_time)

plt.plot(n_list,sort_time,marker='x')
plt.xlabel("number of elements(n)")
plt.ylabel("time taken (seconds)")
plt.title("insertion sort Sort: time complexity analysis ")
plt.grid(True)
plt.savefig("insertion_sort_time_complexity.png",dpi=300,bbox_inches='tight')
plt.show()