import time 
import random

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


print(sort_time)

#nums = [5, 2, 9, 1, 5, 6]

#a = input("Enter numbers separated by spaces: ")
#nums = list(map(int, a.split()))

print(insertion_sort(n_list))

