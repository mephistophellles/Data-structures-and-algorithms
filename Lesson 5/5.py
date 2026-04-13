import sys

def task_5():
    p = sys.stdin.readline().strip()
    if not p:
        return
    t = sys.stdin.readline().strip()
    
    m = len(p)
    n = len(t)
    
    if m > n:
        sys.stdout.write("0\n\n")
        return
    X = 313
    M = 10**18 + 9
    pow_X = [1] * (max(n, m) + 1)
    for i in range(1, len(pow_X)):
        pow_X[i] = (pow_X[i-1] * X) % M
    hT = [0] * (n + 1)
    for i in range(n):
        hT[i+1] = (hT[i] * X + ord(t[i])) % M
    hP = [0] * (m + 1)
    for i in range(m):
        hP[i+1] = (hP[i] * X + ord(p[i])) % M
        
    def get_hash(h, l, r):
        return (h[r+1] - h[l] * pow_X[r - l + 1]) % M
        
    def get_lcp(i, j, max_len):
        low = 0
        high = max_len
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if mid == 0:
                low = mid + 1
                continue
                
            hash_t = get_hash(hT, i, i + mid - 1)
            hash_p = get_hash(hP, j, j + mid - 1)
            
            if hash_t == hash_p:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

    ans = []
    
    for i in range(n - m + 1):
        lcp_len = get_lcp(i, 0, m)
        if lcp_len == m:
            ans.append(i + 1)
        else:
            remaining_len = m - lcp_len - 1
            if remaining_len == 0:
                ans.append(i + 1)
            else:
                hash_tail_t = get_hash(hT, i + lcp_len + 1, i + m - 1)
                hash_tail_p = get_hash(hP, lcp_len + 1, m - 1)
                
                if hash_tail_t == hash_tail_p:
                    ans.append(i + 1)
                    
    sys.stdout.write(f"{len(ans)}\n")
    if ans:
        sys.stdout.write(" ".join(map(str, ans)) + "\n")
    else:
        sys.stdout.write("\n")

if __name__ == '__main__':
    task_5()