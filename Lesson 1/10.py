import sys
import math

def task_10():
    first_line = sys.stdin.readline()
    if not first_line:
        return
    t = int(first_line.strip())
    
    out = []
    
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        
        S_tot = n * m * (n * m + 1) // 2
        min_diff_V = float('inf')
        best_w = -1
        
        if m >= 2:
            B = 1 + m * (n - 1)
            C = m * (n * m + 1) // 2
            
            D = B * B + 4 * C
            w_base = (math.isqrt(D) - B) // 2
            for w in (w_base - 1, w_base, w_base + 1, w_base + 2):
                if 1 <= w < m:
                    val = n * w * (w + 1 + m * (n - 1)) // 2
                    diff = abs(S_tot - 2 * val)
                    if diff < min_diff_V:
                        min_diff_V = diff
                        best_w = w
        min_diff_H = float('inf')
        best_h = -1
        
        if n >= 2:
            D = 1 + 4 * S_tot
            x_base = (math.isqrt(D) - 1) // 2
            h_base = x_base // m
            
            for h in (h_base - 1, h_base, h_base + 1, h_base + 2):
                if 1 <= h < n:
                    val = h * m * (h * m + 1) // 2
                    diff = abs(S_tot - 2 * val)
                    if diff < min_diff_H:
                        min_diff_H = diff
                        best_h = h
        if min_diff_V <= min_diff_H:
            out.append(f"V {best_w + 1}")
        else:
            out.append(f"H {best_h + 1}")
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_10()