import sys

def task_4():
    tokens = []
    for line in sys.stdin:
        tokens.extend(line.split())
        if len(tokens) >= 2:
            break
            
    if len(tokens) < 2:
        return
        
    n = int(tokens[0])
    m = int(tokens[1])
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for s in range(2, n + m + 1):
        for i in range(1, n + 1):
            j = s - i
            if 1 <= j <= m:
                if dp[i][j] > 0:
                    if i - 1 >= 1 and j + 2 <= m:
                        dp[i - 1][j + 2] += dp[i][j]
                    if i + 1 <= n and j + 2 <= m:
                        dp[i + 1][j + 2] += dp[i][j]
                    if i + 2 <= n and j + 1 <= m:
                        dp[i + 2][j + 1] += dp[i][j]
                    if i + 2 <= n and j - 1 >= 1:
                        dp[i + 2][j - 1] += dp[i][j]
    sys.stdout.write(str(dp[n][m]) + '\n')

if __name__ == '__main__':
    task_4()