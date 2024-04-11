def selection_sort(A,key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1    
data = [5,3,8,4,9,1,6,2,7]
print("Original : ", data)
print(selection_sort(data,7))
print("Selection : ", data)