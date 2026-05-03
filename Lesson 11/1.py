import sys

def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    n = int(data[pos]); pos += 1
    m = int(data[pos]); pos += 1
    
    

    parent = list(range(n + 1))
    rank_ = [0] * (n + 1)
    min_val = list(range(n + 1))
    max_val = list(range(n + 1))

    size = [1] * (n + 1)
    
    def find(x):
        root = x
        
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root
    
    out = []
    
    for _ in range(m):
        op = data[pos]; pos += 1
        if op == b'union':
            x = int(data[pos]); pos += 1
            y = int(data[pos]); pos += 1
            rx = find(x)
            ry = find(y)
            if rx != ry:
                if rank_[rx] < rank_[ry]:
                    rx, ry = ry, rx
                parent[ry] = rx
                if rank_[rx] == rank_[ry]:
                    rank_[rx] += 1
                if min_val[ry] < min_val[rx]:
                    min_val[rx] = min_val[ry]
                if max_val[ry] > max_val[rx]:
                    max_val[rx] = max_val[ry]
                size[rx] += size[ry]
        else:
            x = int(data[pos]); pos += 1
            r = find(x)
            out.append(f"{min_val[r]} {max_val[r]} {size[r]}")
    
    sys.stdout.write('\n'.join(out))
    if out:
        sys.stdout.write('\n')

main()