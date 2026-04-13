import sys
from collections import deque

def task_2():
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token

    tokens = get_tokens()
    
    try:
        t = next(tokens)
        q = int(next(tokens))
        queries = [next(tokens) for _ in range(q)]
    except StopIteration:
        return
    MAX_NODES = sum(len(s) for s in queries) + 2
    trie = [{} for _ in range(MAX_NODES)]
    term = [[] for _ in range(MAX_NODES)]
    
    node_count = 1
    
    for i, s in enumerate(queries):
        curr = 0
        for char in s:
            if char not in trie[curr]:
                trie[curr][char] = node_count
                node_count += 1
            curr = trie[curr][char]
        term[curr].append(i)
        
    fail = [0] * node_count
    out_link = [0] * node_count
    queue = deque()
    for char, nxt in trie[0].items():
        fail[nxt] = 0
        queue.append(nxt)
        
    while queue:
        u = queue.popleft()
        for char, v in trie[u].items():
            f = fail[u]
            while f > 0 and char not in trie[f]:
                f = fail[f]
            if char in trie[f]:
                fail[v] = trie[f][char]
            else:
                fail[v] = 0
            if term[fail[v]]:
                out_link[v] = fail[v]
            else:
                out_link[v] = out_link[fail[v]]
                
            queue.append(v)
    ans = [[] for _ in range(q)]
    lengths = [len(s) for s in queries]
    
    curr = 0
    for i, char in enumerate(t):
        while curr > 0 and char not in trie[curr]:
            curr = fail[curr]
        if char in trie[curr]:
            curr = trie[curr][char]
            
        temp = curr
        while temp > 0:
            for q_idx in term[temp]:
                ans[q_idx].append(i - lengths[q_idx] + 1)
            temp = out_link[temp]
            
    out = []
    for res in ans:
        if res:
            out.append(f"{len(res)} " + " ".join(map(str, res)))
        else:
            out.append("0")
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_2()