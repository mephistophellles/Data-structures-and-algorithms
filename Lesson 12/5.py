import sys

def task_5():
    s = sys.stdin.read().strip()
    if not s:
        return
        
    n = len(s)
    dp = [[""] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = s[i]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            best_str = s[i:j+1]
            for k in range(i, j):
                cand = dp[i][k] + dp[k+1][j]
                if len(cand) < len(best_str):
                    best_str = cand
            for L in range(1, length // 2 + 1):
                if length % L == 0:
                    repeats = length // L
                    if s[i:j+1] == s[i:i+L] * repeats:
                        cand = f"{repeats}({dp[i][i+L-1]})"
                        if len(cand) < len(best_str):
                            best_str = cand
                            
            dp[i][j] = best_str
            
    sys.stdout.write(dp[0][n-1] + '\n')

if __name__ == '__main__':
    task_5()