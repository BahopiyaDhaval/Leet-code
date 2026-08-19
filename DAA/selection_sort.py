arr=[5,1,2,3,4]
def selectionsort(arr):
    n=len(arr)
    for i in range(0,n):
        min_index=i
        for j in range(i,n):
            if(arr[j]<arr[min_index]):
                min_index=j
        (arr[i],arr[min_index]) = (arr[min_index],arr[i])
selectionsort(arr)
print(arr)