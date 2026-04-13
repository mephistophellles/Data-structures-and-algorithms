import sys

def task_1():
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token

    tokens = get_tokens()
    
    try:
        n_str = next(tokens)
    except StopIteration:
        return
    n = int(n_str)
    
    a = [int(next(tokens)) for _ in range(n)]
    pref_sum = [0] * (n + 1)
    pref_xor = [0] * (n + 1)
    
    for i in range(n):
        pref_sum[i+1] = pref_sum[i] + a[i]
        pref_xor[i+1] = pref_xor[i] ^ a[i]
        
    m = int(next(tokens))
    out = []
    
    for _ in range(m):
        q_type = next(tokens)
        l = int(next(tokens))
        r = int(next(tokens))
        
        if q_type == '1':
            out.append(str(pref_sum[r] - pref_sum[l-1]))
        else:
            out.append(str(pref_xor[r] ^ pref_xor[l-1]))
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_1()