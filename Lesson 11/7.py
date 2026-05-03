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
    
    a = int(data[pos]); pos += 1
    b = int(data[pos]); pos += 1
    c = int(data[pos]); pos += 1
    
    INF = float('inf')
    
    def dijkstra(src):
        dist = [INF] * (n + 1)
        dist[src] = 0
        heap = [(0, src)]
        while heap:
            d, v = heapq.heappop(heap)
            if d > dist[v]:
                continue
            for u, w in adj[v]:
                nd = d + w
                if nd < dist[u]:
                    dist[u] = nd
                    heapq.heappush(heap, (nd, u))
        return dist
    
    da = dijkstra(a)
    db = dijkstra(b)
    dc = dijkstra(c)
    dab = da[b]
    dbc = db[c]
    dac = da[c]
    
    ans = INF
    if dab < INF and dbc < INF:
        ans = min(ans, dab + dbc)
    if dac < INF and dbc < INF:
        ans = min(ans, dac + dbc)
    if dab < INF and dac < INF:
        ans = min(ans, dab + dac)
    
    if ans == INF:
        print(-1)
    else:
        print(ans)

main()