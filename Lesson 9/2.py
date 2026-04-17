import sys

def task_2():
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
    m = int(next(tokens))
    tree_min = [0] * (2 * n)
    tree_cnt = [0] * (2 * n)
    for i in range(n):
        tree_min[n + i] = int(next(tokens))
        tree_cnt[n + i] = 1
    for i in range(n - 1, 0, -1):
        left_m, left_c = tree_min[2 * i], tree_cnt[2 * i]
        right_m, right_c = tree_min[2 * i + 1], tree_cnt[2 * i + 1]
        
        if left_m < right_m:
            tree_min[i] = left_m
            tree_cnt[i] = left_c
        elif right_m < left_m:
            tree_min[i] = right_m
            tree_cnt[i] = right_c
        else:
            tree_min[i] = left_m
            tree_cnt[i] = left_c + right_c
            
    out = []
    INF = float('inf')
    
    for _ in range(m):
        op = next(tokens)
        
        if op == '1':
            idx = int(next(tokens))
            val = int(next(tokens))
            
            p = idx + n
            tree_min[p] = val
            p //= 2
            while p > 0:
                left_m, left_c = tree_min[2 * p], tree_cnt[2 * p]
                right_m, right_c = tree_min[2 * p + 1], tree_cnt[2 * p + 1]
                
                if left_m < right_m:
                    tree_min[p] = left_m
                    tree_cnt[p] = left_c
                elif right_m < left_m:
                    tree_min[p] = right_m
                    tree_cnt[p] = right_c
                else:
                    tree_min[p] = left_m
                    tree_cnt[p] = left_c + right_c
                p //= 2
                
        else:
            l = int(next(tokens))
            r = int(next(tokens))
            
            l += n
            r += n
            
            res_min = INF
            res_cnt = 0
            
            while l < r:
                if l % 2 == 1:
                    if tree_min[l] < res_min:
                        res_min = tree_min[l]
                        res_cnt = tree_cnt[l]
                    elif tree_min[l] == res_min:
                        res_cnt += tree_cnt[l]
                    l += 1
                    
                if r % 2 == 1:
                    r -= 1
                    if tree_min[r] < res_min:
                        res_min = tree_min[r]
                        res_cnt = tree_cnt[r]
                    elif tree_min[r] == res_min:
                        res_cnt += tree_cnt[r]
                        
                l //= 2
                r //= 2
                
            out.append(f"{res_min} {res_cnt}")
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_2()