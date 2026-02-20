def heapify(arr,n,i): # helps to find out the max heap
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


#heap sort 
def heap_sort(arr):
    n=len(arr) #length of the array, used to find last non leaf node

    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)


#Input array
arr=[12,11,13,5,6,7]
#call the heap sort
heap_sort(arr)
print("Sorted array",arr)                            