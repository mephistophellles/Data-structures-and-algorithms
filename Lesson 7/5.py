import sys

def task_5():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\r\n'))
        if len(lines) == 2:
            break
    if len(lines) < 2:
        return
        
    s1 = lines[0]
    s2 = lines[1]
    
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        s1_char = s1[i - 1]
        s1_prev = s1[i - 2] if i > 1 else ''
        
        for j in range(1, m + 1):
            s2_char = s2[j - 1]
            
            cost = 0 if s1_char == s2_char else 1
            res = dp[i - 1][j] + 1
            ins = dp[i][j - 1] + 1
            if ins < res:
                res = ins
            sub = dp[i - 1][j - 1] + cost
            if sub < res:
                res = sub
            if i > 1 and j > 1 and s1_char == s2[j - 2] and s1_prev == s2_char:
                trans = dp[i - 2][j - 2] + 1
                if trans < res:
                    res = trans
                    
            dp[i][j] = res
    sys.stdout.write(str(dp[n][m]) + '\n')

if __name__ == '__main__':
    task_5()