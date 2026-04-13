import sys

def task_6():
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token

    tokens = get_tokens()
    
    try:
        n_str = next(tokens)
        m_str = next(tokens)
    except StopIteration:
        return
        
    n = int(n_str)
    m = int(m_str)
    grid = [next(tokens) for _ in range(n * m)]
    dp = [0] * (m + 1)
    
    max_size = 0
    best_r = 1
    best_c = 1
    for i in range(n - 1, -1, -1):
        next_diag = 0
        for j in range(m - 1, -1, -1):
            temp = dp[j]
            if grid[i * m + j] == '1':
                val = dp[j]
                if dp[j+1] < val: 
                    val = dp[j+1]
                if next_diag < val: 
                    val = next_diag
                    
                val += 1
                dp[j] = val
                if val > max_size:
                    max_size = val
                    best_r = i + 1
                    best_c = j + 1
            else:
                dp[j] = 0
            next_diag = temp
            
    sys.stdout.write(f"{max_size}\n{best_r} {best_c}\n")

if __name__ == '__main__':
    task_6()