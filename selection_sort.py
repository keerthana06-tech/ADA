l = [4, 20, 12, 21, 1] 

#l=int(input("enter a no:"))
#print("enter",l,"elements")
#l.append(int(input))

def selection_sort(l):
    n = len(l)
    for i in range(n):
        min= i
        for j in range(i + 1, n):
            if l[j] < l[min]:
                min = j
        l[i], l[min] = l[min], l[i]
    return l

print(selection_sort(l))

