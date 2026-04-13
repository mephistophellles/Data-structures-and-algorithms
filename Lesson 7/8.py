import sys

def task_8():
    tokens = []
    for line in sys.stdin:
        tokens.extend(line.split())
        if tokens and len(tokens) >= int(tokens[0]) + 1:
            break
            
    if not tokens:
        return
        
    n = int(tokens[0])
    a = [int(x) for x in tokens[1:n+1]]
    dp = [1] * n
    parent = [-1] * n
    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
        
    max_len = 0
    best_end = -1
    for i in range(n):
        if dp[i] > max_len:
            max_len = dp[i]
            best_end = i
    lis = []
    curr = best_end
    while curr != -1:
        lis.append(a[curr])
        curr = parent[curr]
        
    lis.reverse()
    
    sys.stdout.write(f"{max_len}\n")
    sys.stdout.write(" ".join(map(str, lis)) + "\n")

if __name__ == '__main__':
    task_8()