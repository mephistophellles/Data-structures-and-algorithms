import sys

def task_3():
    def get_tokens():
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            for token in line.split():
                yield token

    tokens = get_tokens()
    
    try:
        n = int(next(tokens))
        m = int(next(tokens))
    except StopIteration:
        return
        
    edges = []
    for _ in range(m):
        u = int(next(tokens))
        v = int(next(tokens))
        edges.append((u, v))
    permutation = [int(next(tokens)) for _ in range(n)]
    pos = [0] * (n + 1)
    for index, vertex in enumerate(permutation):
        pos[vertex] = index
        
    for u, v in edges:
        if pos[u] >= pos[v]:
            sys.stdout.write("NO\n")
            return
            
    sys.stdout.write("YES\n")

if __name__ == '__main__':
    task_3()