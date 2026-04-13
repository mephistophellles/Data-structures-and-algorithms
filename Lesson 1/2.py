import sys
from bisect import bisect_left

def task_2():
    line1 = sys.stdin.readline().split()
    if not line1:
        return
    n = int(line1[0])
    
    a = [int(x) for x in sys.stdin.readline().split()]
    
    queries = [int(x) for x in sys.stdin.readline().split()]
    
    result = []
    for x in queries:
        idx = bisect_left(a, x)
        
        if idx == 0:
            result.append(str(a[0]))
        elif idx == n:
            result.append(str(a[n-1]))
        else:
            left_val = a[idx-1]
            right_val = a[idx]
            
            if x - left_val <= right_val - x:
                result.append(str(left_val))
            else:
                result.append(str(right_val))
                
    sys.stdout.write('\n'.join(result) + '\n')

if __name__ == '__main__':
    task_2()