import sys

def task_4():
    data = sys.stdin.read().split()
    if not data:
        return
        
    L = int(data[0])
    N = int(data[1])
    cuts = [0] * (N + 2)
    cuts[0] = 0
    for i in range(1, N + 1):
        cuts[i] = int(data[i + 1])
    cuts[N + 1] = L
    
    M = N + 2
    INF = 10**18
    dp = [[0] * M for _ in range(M)]
    for length in range(2, M):
        for i in range(M - length):
            j = i + length
            
            min_cost = INF
            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j]
                if cost < min_cost:
                    min_cost = cost
            dp[i][j] = min_cost + cuts[j] - cuts[i]
            
    sys.stdout.write(str(dp[0][M - 1]) + '\n')

if __name__ == '__main__':
    task_4()