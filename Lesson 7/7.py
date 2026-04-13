import sys

def task_7():
    s = sys.stdin.read().strip()
    if not s:
        print()
        return
        
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    split = [[-1] * n for _ in range(n)]
    
    match = {'(': ')', '[': ']', '{': '}'}
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = dp[i + 1][j]
            split[i][j] = -1
            if s[i] in match:
                target = match[s[i]]
                
                for k in range(i + 1, j + 1):
                    if s[k] == target:
                        inside = dp[i + 1][k - 1] if k > i + 1 else 0
                        outside = dp[k + 1][j] if k < j else 0
                        
                        val = 2 + inside + outside
                        
                        if val > dp[i][j]:
                            dp[i][j] = val
                            split[i][j] = k
                            
    def build(i, j):
        if i > j:
            return ""
        
        k = split[i][j]
        
        if k == -1:
            return build(i + 1, j)
        else:
            return s[i] + build(i + 1, k - 1) + s[k] + build(k + 1, j)
            
    sys.stdout.write(build(0, n - 1) + '\n')

if __name__ == '__main__':
    task_7()