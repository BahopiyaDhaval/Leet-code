def partition(arr, start, end):
    p_index = start
    pivot = arr[end]
    
    for i in range(start, end):
        if(arr[i]<=pivot):
            arr[i],arr[p_index] = arr[p_index],arr[i]
            p_index += 1
    arr[p_index],arr[end] = arr[p_index],arr[end]
    return p_index

def quicksort()
    
arr = [3,2,5,7,4,1,9,6]
print quicksort(arr,0,len(arr)-1)