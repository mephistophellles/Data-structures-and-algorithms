import sys
from collections import deque

def task_6():
    def get_lines():
        for line in sys.stdin:
            stripped = line.strip()
            if stripped:
                yield stripped

    lines = get_lines()
    
    try:
        m_str = next(lines)
    except StopIteration:
        return
        
    m = int(m_str)
    
    adj = {}
    
    for _ in range(m):
        parts = next(lines).split()
        u = parts[0]
        v = parts[2]
        
        if u not in adj:
            adj[u] = []
        adj[u].append(v)
        
    start_substance = next(lines)
    target_substance = next(lines)
    if start_substance == target_substance:
        sys.stdout.write("0\n")
        return
    queue = deque([start_substance])
    dist = {start_substance: 0}
    
    while queue:
        curr = queue.popleft()
        if curr == target_substance:
            sys.stdout.write(str(dist[curr]) + '\n')
            return
        for neighbor in adj.get(curr, []):
            if neighbor not in dist:
                dist[neighbor] = dist[curr] + 1
                queue.append(neighbor)
    sys.stdout.write("-1\n")

if __name__ == '__main__':
    task_6()