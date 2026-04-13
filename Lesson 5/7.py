import sys
import random

def task_7():
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token

    tokens = get_tokens()
    
    try:
        n = int(next(tokens))
    except StopIteration:
        return
        
    a = [int(next(tokens)) for _ in range(n)]
    
    m = int(next(tokens))
    b = [int(next(tokens)) for _ in range(m)]
    unique_vals = set(a) | set(b)
    rand_map = {val: random.getrandbits(128) for val in unique_vals}
    
    hash_a = [rand_map[x] for x in a]
    hash_b = [rand_map[x] for x in b]
    
    max_len = min(n, m)
    
    for length in range(max_len, 0, -1):
        seen_hashes = set()
        curr_hash = sum(hash_a[:length])
        seen_hashes.add(curr_hash)
        
        for i in range(length, n):
            curr_hash += hash_a[i] - hash_a[i - length]
            seen_hashes.add(curr_hash)
        curr_hash = sum(hash_b[:length])
        if curr_hash in seen_hashes:
            sys.stdout.write(str(length) + '\n')
            return
            
        for i in range(length, m):
            curr_hash += hash_b[i] - hash_b[i - length]
            if curr_hash in seen_hashes:
                sys.stdout.write(str(length) + '\n')
                return
    sys.stdout.write("0\n")

if __name__ == '__main__':
    task_7()