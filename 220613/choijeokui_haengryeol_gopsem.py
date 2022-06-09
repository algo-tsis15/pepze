from collections import defaultdict

def solution(matrix_sizes):
    answer = 0
    sizes = []
    for item in matrix_sizes:
        sizes.append(item[0])
    sizes.append(item[1])
    
    dp = defaultdict(lambda: defaultdict(int))
    
    for n in range(2, len(sizes)):
        for i in range(len(sizes) - n):
            k = 1
            dp[i][n] = dp[i][k] + dp[i + k][n - k] + sizes[i] * sizes[i + k] * sizes[i + n]
            k += 1            
            while (k < n):
                dp[i][n] = min(dp[i][n], dp[i][k] + dp[i + k][n - k] + sizes[i] * sizes[i + k] * sizes[i + n])
                k += 1
                
    return dp[0][len(matrix_sizes)]
