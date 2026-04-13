import sys

def task_2():
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token

    tokens = get_tokens()
    
    try:
        n_str = next(tokens)
    except StopIteration:
        return
        
    n = int(n_str)
    m = int(next(tokens))
    k = int(next(tokens))
    
    pref = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            val = int(next(tokens))
            pref[i][j] = val + pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1]
            
    out = []
    
    for _ in range(k):
        y1 = int(next(tokens))
        x1 = int(next(tokens))
        y2 = int(next(tokens))
        x2 = int(next(tokens))
        ans = pref[y2][x2] - pref[y1-1][x2] - pref[y2][x1-1] + pref[y1-1][x1-1]
        out.append(str(ans))
        
    # Выводим все ответы единым блоком
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_2()