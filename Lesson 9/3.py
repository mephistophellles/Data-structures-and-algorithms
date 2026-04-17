import sys

def task_3():
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token

    tokens = get_tokens()
    
    try:
        n = int(next(tokens))
        m = int(next(tokens))
    except StopIteration:
        return
    sz = 1
    while sz < n:
        sz *= 2
        
    tree = [0] * (2 * sz)
    for i in range(n):
        tree[sz + i] = int(next(tokens))
        
    for i in range(sz - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]
        
    out = []
    
    for _ in range(m):
        op = next(tokens)
        arg = int(next(tokens))
        
        if op == '1':

            p = sz + arg
            tree[p] = 1 - tree[p]
            p //= 2
            while p > 0:
                tree[p] = tree[2 * p] + tree[2 * p + 1]
                p //= 2
                
        else:
            k = arg
            p = 1
            while p < sz:
                left_ones = tree[2 * p]
                if left_ones > k:
                    p = 2 * p
                else:
                    k -= left_ones
                    p = 2 * p + 1
            out.append(str(p - sz))
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_3()