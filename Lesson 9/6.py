import sys

def task_6():
    tokens = []
    for line in sys.stdin:
        tokens.extend(line.split())
        if tokens and len(tokens) >= int(tokens[0]) + 1:
            break
    if not tokens:
        return
        
    n = int(tokens[0])
    a = [int(x) for x in tokens[1:n+1]]
    unique_vals = sorted(list(set(a)))
    m = len(unique_vals)
    rank = {val: i + 1 for i, val in enumerate(unique_vals)}
    bit_left = [0] * (m + 1)
    
    def add_left(x, val):
        while x <= m:
            bit_left[x] += val
            x += x & -x
            
    def query_left(x):
        res = 0
        while x > 0:
            res += bit_left[x]
            x -= x & -x
        return res
        
    greater_left = [0] * n
    for i in range(n):
        r = rank[a[i]]
        greater_left[i] = i - query_left(r)
        add_left(r, 1)
    bit_right = [0] * (m + 1)
    

    def add_right(x, val):
        while x <= m:
            bit_right[x] += val
            x += x & -x
            

    def query_right(x):
        res = 0
        while x > 0:
            res += bit_right[x]
            x -= x & -x
        return res
        

    smaller_right = [0] * n
    for i in range(n - 1, -1, -1):
        r = rank[a[i]]
        smaller_right[i] = query_right(r - 1)
        add_right(r, 1)
        
    total_triplets = 0
    for i in range(n):
        total_triplets += greater_left[i] * smaller_right[i]
        
    sys.stdout.write(str(total_triplets) + '\n')

if __name__ == '__main__':
    task_6()