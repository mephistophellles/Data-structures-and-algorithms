import sys

def task_1():
    first_line = sys.stdin.readline()
    if not first_line:
        return
    n = int(first_line.strip())
    p = []
    while len(p) < n - 1:
        line = sys.stdin.readline()
        if not line:
            break
        p.extend(int(x) for x in line.split())
    depth = [0] * n
    for i in range(1, n):
        depth[i] = depth[p[i-1]] + 1
        
    height = max(depth)
    
    max_down = [0] * n
    diameter = 0
    for i in range(n - 1, 0, -1):
        parent = p[i-1]
        cand = max_down[parent] + max_down[i] + 1
        if cand > diameter:
            diameter = cand
        if max_down[i] + 1 > max_down[parent]:
            max_down[parent] = max_down[i] + 1
    sys.stdout.write(f"{height} {diameter}\n")
    sys.stdout.write(" ".join(map(str, depth)) + "\n")

if __name__ == '__main__':
    task_1()