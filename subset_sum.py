def subset_sum(arr,target):
    n = len(arr)
    dp = [[False]*(target+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1,n+1):
        for j in range(1,target+1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                
    return dp[n][target]
    
arr = [3, 34, 4, 12, 5, 2]
target = 9

print(subset_sum(arr, target))