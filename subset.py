def subset_sum(arr,target):
    n=len(arr)

    for i in range(1<<n):
        subset=[]
        total=0

        for j in range(n):
            if i & (1<<j):
                subset.append(arr[j])
                total+=arr[j]

        if total==target:
            print("subset found:",subset)
            return
        print("subset not found")

arr=[2,6,8,9,5,3]
target=10
subset_sum(arr,target)
