import sys

def task_1():
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
    tree = [0] * (2 * n)
    
    for i in range(n):
        tree[n + i] = int(next(tokens))
    for i in range(n - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]
        
    out = []
    for _ in range(m):
        op = next(tokens)
        
        if op == '1':
            idx = int(next(tokens))
            val = int(next(tokens))
            p = idx + n
            tree[p] = val
            p //= 2
            while p > 0:
                tree[p] = tree[2 * p] + tree[2 * p + 1]
                p //= 2
                
        else:
            l = int(next(tokens))
            r = int(next(tokens))
            
            res = 0
            l += n
            r += n
            while l < r:
                if l % 2 == 1:
                    res += tree[l]
                    l += 1
                if r % 2 == 1:
                    r -= 1
                    res += tree[r]
                    
                # уровень выше
                l //= 2
                r //= 2
                
            out.append(str(res))
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_1()