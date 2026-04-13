import sys
from collections import deque

def task_7():
    first_line = sys.stdin.readline()
    if not first_line:
        return
    n = int(first_line.strip())
    
    left_half = deque()
    right_half = deque()
    out = []
    
    for _ in range(n):
        line = sys.stdin.readline().split()
        if not line:
            break
            
        op = line[0]
        
        if op == '+':
            right_half.append(line[1])
        elif op == '*':
            right_half.appendleft(line[1])
        elif op == '-':
            out.append(left_half.popleft())
        if len(right_half) > len(left_half):
            left_half.append(right_half.popleft())
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_7()