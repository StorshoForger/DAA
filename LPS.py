def LPS(X):
    Y = X[::-1]
    n = len(X)
    
    dp = [[0]*(n+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                
    lps = []
    i=j=n
    
    while i>0 and j>0:
        if X[i-1] == Y[j-1]:
            lps.append(X[i-1])
            i-=1
        elif dp[i-1][j] > dp[i][j-1]:
            i-=1
        else:
            j-=1
            
    lps = lps[::-1]
    max_len = len(lps)
    
    return max_len,lps
    
X = "character"
len,pal = LPS(X)
print(len,pal)