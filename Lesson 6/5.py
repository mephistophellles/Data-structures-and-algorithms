import sys
from collections import deque

def task_5():
    line = sys.stdin.readline()
    if not line:
        return
    k = int(line.strip())
    dist = [float('inf')] * k
    queue = deque()
    start = 1 % k
    dist[start] = 1
    queue.append(start)
    
    while queue:
        u = queue.popleft()
        if u == 0:
            sys.stdout.write(str(dist[u]) + '\n')
            return
        nxt_mul = (u * 10) % k
        if dist[u] < dist[nxt_mul]:
            dist[nxt_mul] = dist[u]
            queue.appendleft(nxt_mul)
        nxt_add = (u + 1) % k
        if dist[u] + 1 < dist[nxt_add]:
            dist[nxt_add] = dist[u] + 1
            queue.append(nxt_add)

if __name__ == '__main__':
    task_5()