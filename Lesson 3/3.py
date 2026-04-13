import sys

def task_3():
    def next_token():
        while True:
            if next_token.buffer:
                return next_token.buffer.pop(0)
            line = sys.stdin.readline()
            if not line:
                return None
            next_token.buffer.extend(line.split())
            
    next_token.buffer = []

    n_str = next_token()
    if not n_str:
        return
    n = int(n_str)
    p = [0] * n
    for i in range(1, n):
        p[i] = int(next_token())
    depth = [0] * n
    for i in range(1, n):
        depth[i] = depth[p[i]] + 1
    m = int(next_token())
    out = []
    for _ in range(m):
        u = int(next_token())
        v = int(next_token())
        while depth[u] > depth[v]:
            u = p[u]
        while depth[v] > depth[u]:
            v = p[v]
        while u != v:
            u = p[u]
            v = p[v]
        out.append(str(u))

    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_3()