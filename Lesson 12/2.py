import sys

def task_2():
    data = sys.stdin.read().split()
    if not data:
        return
        
    data = list(map(int, data))
    it = iter(data)
    
    n = next(it)
    
    parents = [0] * n
    weights = [0] * n
    
    for i in range(1, n):
        parents[i] = next(it)
        weights[i] = next(it)
        
    try:
        m = next(it)
    except StopIteration:
        return
        
    K = 18 
    INF = 10**18
    up = [[0] * K for _ in range(n)]
    mine = [[INF] * K for _ in range(n)]
    depth = [0] * n
    
    for i in range(1, n):
        p = parents[i]
        w = weights[i]
        
        depth[i] = depth[p] + 1
        up[i][0] = p
        mine[i][0] = w
        for j in range(1, K):
            half_p = up[i][j-1]
            up[i][j] = up[half_p][j-1]
            val1 = mine[i][j-1]
            val2 = mine[half_p][j-1]
            mine[i][j] = val1 if val1 < val2 else val2
            
    out = []
    app = out.append
    for _ in range(m):
        u = next(it)
        v = next(it)
        
        res = INF
        
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for j in range(K):
            if (diff >> j) & 1:
                if mine[u][j] < res:
                    res = mine[u][j]
                u = up[u][j]
                
        if u == v:
            app(str(res))
            continue
        for j in range(K - 1, -1, -1):
            if up[u][j] != up[v][j]:
                if mine[u][j] < res: res = mine[u][j]
                if mine[v][j] < res: res = mine[v][j]
                u = up[u][j]
                v = up[v][j]
                
        if mine[u][0] < res: res = mine[u][0]
        if mine[v][0] < res: res = mine[v][0]
        
        app(str(res))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_2()