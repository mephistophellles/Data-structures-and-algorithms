import sys

def task_1():
    data = sys.stdin.read().split()
    if not data:
        return
        
    data = list(map(int, data))
    it = iter(data)
    
    n = next(it)
    parents = [0] * n
    for i in range(1, n):
        parents[i] = next(it)
        
    m = next(it)
    K = 18
    up = [[0] * K for _ in range(n)]
    depth = [0] * n
    for i in range(1, n):
        p = parents[i]
        depth[i] = depth[p] + 1
        up[i][0] = p
        for j in range(1, K):
            up[i][j] = up[up[i][j-1]][j-1]
            
    out = []
    app = out.append
    for _ in range(m):
        u = next(it)
        v = next(it)

        if depth[u] < depth[v]:
            u, v = v, u
            
        diff = depth[u] - depth[v]
        for j in range(K):
            if (diff >> j) & 1:
                u = up[u][j]
                
        if u == v:
            app(str(u))
            continue
        for j in range(K - 1, -1, -1):
            if up[u][j] != up[v][j]:
                u = up[u][j]
                v = up[v][j]
        app(str(up[u][0]))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_1()