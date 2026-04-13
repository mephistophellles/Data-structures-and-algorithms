import sys
from collections import deque

def task_4():
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
        x1 = int(next(tokens))
        y1 = int(next(tokens))
        x2 = int(next(tokens))
        y2 = int(next(tokens))
    except StopIteration:
        return
        
    if x1 == x2 and y1 == y2:
        sys.stdout.write("0\n")
        sys.stdout.write(f"{x1} {y1}\n")
        return
        
    moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    
    dist = [[-1] * (n + 1) for _ in range(n + 1)]
    parent = [[None] * (n + 1) for _ in range(n + 1)]
    
    queue = deque()
    queue.append((x1, y1))
    dist[x1][y1] = 0
    
    found = False
    
    while queue and not found:
        cx, cy = queue.popleft()
        
        for dx, dy in moves:
            nx, ny = cx + dx, cy + dy
            
            if 1 <= nx <= n and 1 <= ny <= n:
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[cx][cy] + 1
                    parent[nx][ny] = (cx, cy)
                    queue.append((nx, ny))
                    
                    if nx == x2 and ny == y2:
                        found = True
                        break
                        
    path = []
    curr = (x2, y2)
    
    while curr is not None:
        path.append(curr)
        curr = parent[curr[0]][curr[1]]
        
    path.reverse()
    
    out = [str(dist[x2][y2])]
    for px, py in path:
        out.append(f"{px} {py}")
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_4()