import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    n = int(data[pos]); pos += 1
    m = int(data[pos]); pos += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[pos]); pos += 1
        v = int(data[pos]); pos += 1
        w = int(data[pos]); pos += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0
    
    heap = [(0, 1)]
    
    while heap:
        d, v = heapq.heappop(heap)
        if d > dist[v]:
            continue

        for u, w in adj[v]:
            nd = d + w
            if nd < dist[u]:
                dist[u] = nd
                heapq.heappush(heap, (nd, u))
    
    out = ' '.join(str(dist[i]) for i in range(1, n + 1))
    sys.stdout.write(out + '\n')

main()