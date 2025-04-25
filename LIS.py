def LIS(arr):
    n = len(arr)

    dp = [1]*n
    prev = [-1]*n

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and dp[j]+1 >dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_len = max(dp)
    max_index = dp.index(max_len)
    lis = []

    while max_index != -1:
        lis.append(arr[max_index])
        max_index = prev[max_index]

    lis.reverse()
    return max_len,lis

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
result=[]
len,result = LIS(arr)

print(len,result)