def quick_sort(arr):
    if len(arr) <=1:
        return arr
    
    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x>pivot]

    return quick_sort(left) + middle +quick_sort(right)

arr = [10,15,67,90,40,59]
new_arr = quick_sort(arr)
print(new_arr)