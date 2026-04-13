import sys

def task_4():
    s = sys.stdin.readline().strip()
    if not s:
        return
        
    n = len(s)
    S = s + s
    
    i = 0
    j = 1
    k = 0
    
    while i < n and j < n and k < n:
        if S[i + k] == S[j + k]:
            k += 1
        else:
            if S[i + k] > S[j + k]:
                i += k + 1
            else:
                j += k + 1
                
            if i == j:
                j += 1
                
            k = 0
            
    ans_idx = min(i, j)
    sys.stdout.write(S[ans_idx : ans_idx + n] + '\n')

if __name__ == '__main__':
    task_4()