import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    N = int(data[pos]); pos += 1
    M = int(data[pos]); pos += 1
    
    edges = []
    adj = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u = int(data[pos]); pos += 1
        v = int(data[pos]); pos += 1
        t = int(data[pos]); pos += 1
        w = int(data[pos]); pos += 1
        adj[u].append((v, t, w))
        adj[v].append((u, t, w))
    
    EMPTY_TRUCK = 3_000_000  
    CUP_WEIGHT = 100         
    MAX_TIME = 1440           
    
    def can_deliver(num_cups):
        truck_weight = EMPTY_TRUCK + CUP_WEIGHT * num_cups
        INF = float('inf')
        dist = [INF] * (N + 1)
        dist[1] = 0
        heap = [(0, 1)]
        
        while heap:
            d, v = heapq.heappop(heap)
            if d > dist[v]:
                continue
            if v == N:
                return d <= MAX_TIME
            for u, t, w in adj[v]:
                if w >= truck_weight:
                    nd = d + t
                    if nd < dist[u]:
                        dist[u] = nd
                        heapq.heappush(heap, (nd, u))
        
        return dist[N] <= MAX_TIME
    if not can_deliver(0):
        print(0)
        return
    max_road_weight = 0
    for u_list in adj:
        for _, _, w in u_list:
            if w > max_road_weight:
                max_road_weight = w
    max_cups = max(0, (max_road_weight - EMPTY_TRUCK) // CUP_WEIGHT)
    
    lo, hi = 0, max_cups
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can_deliver(mid):
            lo = mid
        else:
            hi = mid - 1
    
    print(lo)

main()