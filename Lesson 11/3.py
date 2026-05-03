import sys

def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    N = int(data[pos]); pos += 1
    M = int(data[pos]); pos += 1
    
    # grid[i][j] — код связности
    grid = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            grid[i][j] = int(data[pos]); pos += 1
    
    # DSU
    total = N * M
    parent = list(range(total))
    rank_ = [0] * total
    
    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root
    
    def union(x, y):
        rx = find(x); ry = find(y)
        if rx == ry:
            return False
        if rank_[rx] < rank_[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank_[rx] == rank_[ry]:
            rank_[rx] += 1
        return True
    
    def node(i, j):
        return i * M + j
    vertical_candidates = [] 
    horizontal_candidates = [] 
    
    for i in range(N):
        for j in range(M):
            c = grid[i][j]
            has_down = (c == 1 or c == 3)  
            has_right = (c == 2 or c == 3)
            
            if i + 1 < N:
                if has_down:
                    union(node(i, j), node(i + 1, j))
                else:
                    vertical_candidates.append((i, j))
            
            if j + 1 < M:
                if has_right:
                    union(node(i, j), node(i, j + 1))
                else:
                    horizontal_candidates.append((i, j))
    
    added = []
    cost = 0
    
    for i, j in vertical_candidates:
        if union(node(i, j), node(i + 1, j)):
            added.append((i + 1, j + 1, 1))
            cost += 1
    
    for i, j in horizontal_candidates:
        if union(node(i, j), node(i, j + 1)):
            added.append((i + 1, j + 1, 2))
            cost += 2
    
    
    
    out = [f"{len(added)} {cost}"]
    for (i, j, d) in added:
        out.append(f"{i} {j} {d}")
    
    sys.stdout.write('\n'.join(out))
    sys.stdout.write('\n')

main()