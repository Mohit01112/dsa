## finding a smallest element in an array 

def find_smallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index
## sorting the array
def selectionsort(arr):
    new_arr=[]
    copyarr=list(arr)
    for i in range (len(arr)):
        smallest_index=find_smallest(copyarr)
        new_arr.append(copyarr.pop(smallest_index))
    return new_arr

arr=[5,3,6,2,10]
print(find_smallest(arr))
print(selectionsort(arr))