## binary search

def binary_search(arr,item):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(high+low)//2
        guess=arr[mid]
        if guess==item:
            return item
        elif guess<item:
            low=mid+1
        else:
            high=mid-1
    return None

my_list=[1,2,5,7,9]
print(binary_search(my_list, 3))
print(binary_search(my_list, 7))