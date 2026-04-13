import sys

def task_1():
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
    
    for _ in range(m):
        u = int(next(tokens))
        v = int(next(tokens))
        adj[u].append(v)
        adj[v].append(u)
        
    visited = [False] * (n + 1)
    components = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = True
            
            while stack:
                curr = stack.pop()
                comp.append(curr)
                
                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
                        
            comp.sort()
            components.append(comp)
            
    out = [str(len(components))]
    for comp in components:
        out.append(str(len(comp)))
        out.append(" ".join(map(str, comp)))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_1()