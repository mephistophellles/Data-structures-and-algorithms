import sys

def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    n = int(data[pos]); pos += 1
    m = int(data[pos]); pos += 1
    edges = []
    for _ in range(m):
        u = int(data[pos]); pos += 1
        v = int(data[pos]); pos += 1
        w = int(data[pos]); pos += 1
        edges.append((w, u, v))
    
    edges.sort()
    
    
    parent = list(range(n + 1))
    rank_ = [0] * (n + 1)
    
    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root
    
    total = 0
    edges_used = 0
    
    for w, u, v in edges:
        ru = find(u)
        rv = find(v)
        if ru != rv:
            if rank_[ru] < rank_[rv]:
                ru, rv = rv, ru
            parent[rv] = ru
            if rank_[ru] == rank_[rv]:
                rank_[ru] += 1
            total += w
            edges_used += 1
            if edges_used == n - 1:
                break
    
    sys.stdout.write(str(total) + '\n')

main()