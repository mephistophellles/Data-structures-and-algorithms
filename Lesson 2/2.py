import sys
from collections import deque

def task_2():
    line1 = sys.stdin.readline()
    if not line1:
        return
    n, k = map(int, line1.split())
    
    line2 = sys.stdin.readline()
    a = [int(x) for x in line2.split()]
    
    dq = deque()
    out = []
    
    for i in range(n):
        if dq and dq[0] == i - k:
            dq.popleft()
        while dq and a[dq[-1]] >= a[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(str(a[dq[0]]))
    sys.stdout.write(' '.join(out) + '\n')

if __name__ == '__main__':
    task_2()