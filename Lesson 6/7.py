import sys

def task_7():
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
        
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dist[i][i] = 0
        
    for _ in range(m):
        u = int(next(tokens))
        v = int(next(tokens))
        w = int(next(tokens))
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    best_city = -1
    min_max_dist = INF
    for i in range(1, n + 1):
        current_max_dist = 0
        for j in range(1, n + 1):
            if dist[i][j] > current_max_dist:
                current_max_dist = dist[i][j]
        if current_max_dist < min_max_dist:
            min_max_dist = current_max_dist
            best_city = i
            
    sys.stdout.write(str(best_city) + '\n')

if __name__ == '__main__':
    task_7()