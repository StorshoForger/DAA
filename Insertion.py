def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
            
        arr[j+1] = key
        
    return arr
    
arr = [11,7,56,90,38]
new_arr = insertion_sort(arr)
print(new_arr)