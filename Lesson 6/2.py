import sys
from collections import deque

def task_2():
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
        
    adj = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(tokens))
        v = int(next(tokens))
        adj[u].append(v)
        indegree[v] += 1
        
    queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])
    processed_count = 0
    
    while queue:
        u = queue.popleft()
        processed_count += 1
        
        for neighbor in adj[u]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    if processed_count == n:
        sys.stdout.write("0\n")
    else:
        sys.stdout.write("1\n")

if __name__ == '__main__':
    task_2()