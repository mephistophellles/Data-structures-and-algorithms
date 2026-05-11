import sys

def task_3():
    s = sys.stdin.read().strip()
    if not s:
        return
        
    n = len(s)
    
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
        
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i+1][j-1] + 2
            else:
                val1 = dp[i+1][j]
                val2 = dp[i][j-1]
                dp[i][j] = val1 if val1 > val2 else val2
                
    res_len = dp[0][n-1]
    
    ans = [''] * res_len
    left_ptr = 0
    right_ptr = res_len - 1
    
    i = 0
    j = n - 1
    
    while i <= j:
        if i == j:
            ans[left_ptr] = s[i]
            break
            
        if s[i] == s[j]:
            ans[left_ptr] = s[i]
            ans[right_ptr] = s[j]
            left_ptr += 1
            right_ptr -= 1
            i += 1
            j -= 1
        elif dp[i+1][j] >= dp[i][j-1]:
            i += 1
        else:
            j -= 1
            
    sys.stdout.write(f"{res_len}\n")
    sys.stdout.write("".join(ans) + "\n")

if __name__ == '__main__':
    task_3()