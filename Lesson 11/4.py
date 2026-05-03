import sys

def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    n = int(data[pos]); pos += 1
    a = [int(data[pos + i]) for i in range(n)]; pos += n
    d = [int(data[pos + i]) for i in range(n)]; pos += n
    
    prev_ = list(range(-1, n - 1))   
    next_ = list(range(1, n + 1))    

    for i in range(n):
        if next_[i] >= n:
            next_[i] = -1
    
    alive = [True] * n
    candidates = list(range(n))
    
    out = []
    
    for _ in range(n):
        to_die = []
        seen = set()

        for i in candidates:
            if not alive[i] or i in seen:
                continue
            seen.add(i)
            dmg = 0
            L = prev_[i]
            R = next_[i]
            if L != -1:
                dmg += a[L]
            if R != -1:
                dmg += a[R]
            if dmg > d[i]:
                to_die.append(i)
        
        out.append(str(len(to_die)))
        
        new_candidates = []
        for i in to_die:
            L = prev_[i]
            R = next_[i]
            if L != -1:
                next_[L] = R
                if alive[L]:
                    new_candidates.append(L)
            if R != -1:
                prev_[R] = L
                if alive[R]:
                    new_candidates.append(R)
            alive[i] = False
        
        candidates = new_candidates
        if not candidates:
            remaining = n - len(out)

            for _ in range(remaining):
                out.append('0')

            break
    
    sys.stdout.write(' '.join(out))
    sys.stdout.write('\n')

main()