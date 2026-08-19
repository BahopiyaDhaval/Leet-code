def merging(A, B):
    merge=[0]*(len(A)+len(B))
    i,j,k=0,0,0
    while i<len(A) and j<len(B):
        if A[i]<B[j]:
            merge[k]=A[i]
            i+=1
            k+=1
        else:
            merge[k]=B[j]
            j+=1
            k+=1

    while i<len(A):
        merge[k]=A[i]
        i+=1
        k+=1
    while j<len(B):
        merge[k]=B[j]
        j+=1
        k+=1
    return merge

A=[1,3,5,9,11,13]
B=[2,4,16,20,24]
Merged=merging(A,B)
print(Merged)