def merge(A, B):
    merge = [0] * (len(A) + len(B))
    i, j, k = 0, 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merge[k] = A[i]
            i += 1
            k += 1
        else:
            merge[k] = B[j]
            j += 1
            k += 1

    while i < len(A):
        merge[k] = A[i]
        i += 1
        k += 1
    while j < len(B):
        merge[k] = B[j]
        j += 1
        k += 1
    return merge

def divide(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = divide(arr[:mid])
    right = divide(arr[mid:])
    return merge(left, right) 

arr = [3,2,4,1,5,0]
print(divide(arr))