import sys

def task_4():
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
    sz = 1
    while sz < n:
        sz *= 2
    tree = [-1] * (2 * sz)
    
    for i in range(n):
        tree[sz + i] = int(next(tokens))


    for i in range(sz - 1, 0, -1):
        left = tree[2 * i]
        right = tree[2 * i + 1]
        tree[i] = left if left > right else right
        
    out = []
    
    for _ in range(m):
        op = next(tokens)
        
        if op == '1':
            idx = int(next(tokens))
            val = int(next(tokens))
            p = sz + idx
            tree[p] = val
            p //= 2
            
            while p > 0:
                left = tree[2 * p]
                right = tree[2 * p + 1]
                tree[p] = left if left > right else right
                p //= 2
                
        else:
            x = int(next(tokens))
            l = int(next(tokens))
            
            p = sz + l
            if tree[p] >= x:
                out.append(str(l))
                continue
                
            found = False
            while p > 1:
                if p % 2 == 0:
                    if tree[p + 1] >= x:
                        p += 1
                        found = True
                        break
                p //= 2
                
            if not found:
                out.append("-1")
            else:
                while p < sz:
                    p *= 2
                    if tree[p] < x:
                        p += 1
                        
                ans = p - sz
                if ans < n:
                    out.append(str(ans))
                else:
                    out.append("-1")
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_4()