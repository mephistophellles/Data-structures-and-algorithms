import sys

def task_3():
    a = sys.stdin.readline().strip()
    if not a:
        return
    b = sys.stdin.readline().strip()
    
    n = len(a)
    m = len(b)
    
    if m > n or m == 0:
        sys.stdout.write("0\n")
        return
        
    P = 313
    M = 10**18 + 9
    P_m = pow(P, m, M)
    
    B = b + b
    target_hashes = set()
    
    curr_hash = 0
    for i in range(m):
        curr_hash = (curr_hash * P + ord(B[i])) % M
        
    target_hashes.add(curr_hash)
    
    for i in range(1, m):
        curr_hash = (curr_hash * P - ord(B[i-1]) * P_m + ord(B[i+m-1])) % M
        target_hashes.add(curr_hash)
        
    ans = 0
    curr_hash = 0
    for i in range(m):
        curr_hash = (curr_hash * P + ord(a[i])) % M
        
    if curr_hash in target_hashes:
        ans += 1
    
    for i in range(1, n - m + 1):
        curr_hash = (curr_hash * P - ord(a[i-1]) * P_m + ord(a[i+m-1])) % M
        if curr_hash in target_hashes:
            ans += 1
            
    sys.stdout.write(str(ans) + '\n')

if __name__ == '__main__':
    task_3()