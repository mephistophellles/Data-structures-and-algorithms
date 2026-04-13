import sys

def task_1():
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token

    tokens = get_tokens()
    
    try:
        s = next(tokens)
    except StopIteration:
        return
        
    m = int(next(tokens))
    n = len(s)
    
    P = 257
    M = 10**9 + 7
    
    h = [0] * (n + 1)
    p = [1] * (n + 1)
    for i in range(n):
        h[i+1] = (h[i] * P + ord(s[i])) % M
        p[i+1] = (p[i] * P) % M
        
    out = []
    for _ in range(m):
        a = int(next(tokens))
        b = int(next(tokens))
        c = int(next(tokens))
        d = int(next(tokens))
        if b - a != d - c:
            out.append("No")
            continue
            
        length = b - a + 1
        hash1 = (h[b] - h[a-1] * p[length]) % M
        hash2 = (h[d] - h[c-1] * p[length]) % M
        if hash1 == hash2:
            out.append("Yes")
        else:
            out.append("No")
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_1()