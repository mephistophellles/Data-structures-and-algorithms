import sys

def task_5():
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
    unique_vals = sorted(list(set(a)))
    m = len(unique_vals)
    rank = {val: i + 1 for i, val in enumerate(unique_vals)}
    bit_max = [0] * (m + 1)
    bit_cnt = [0] * (m + 1)
    MOD = 10**9 + 7
    def query(x):
        ans_max = 0
        ans_cnt = 1
        while x > 0:
            if bit_max[x] > ans_max:
                ans_max = bit_max[x]
                ans_cnt = bit_cnt[x]
            elif bit_max[x] == ans_max:
                ans_cnt = (ans_cnt + bit_cnt[x]) % MOD
            x -= x & -x
        return ans_max, ans_cnt
    def update(x, v_max, v_cnt):
        while x <= m:
            if v_max > bit_max[x]:
                bit_max[x] = v_max
                bit_cnt[x] = v_cnt
            elif v_max == bit_max[x]:
                bit_cnt[x] = (bit_cnt[x] + v_cnt) % MOD
            x += x & -x
    for val in a:
        r = rank[val]
        q_max, q_cnt = query(r - 1)
        update(r, q_max + 1, q_cnt)
        
        
    final_max, final_cnt = query(m)
    
    if final_max == 0:
        sys.stdout.write("0\n")
    else:
        sys.stdout.write(str(final_cnt) + "\n")

if __name__ == '__main__':
    task_5()