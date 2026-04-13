import sys

def task_1():
    first_line = sys.stdin.readline()
    if not first_line:
        return
    n = int(first_line.strip())
    min_stack = []
    out = []
    
    for _ in range(n):
        line = sys.stdin.readline().split()
        op = line[0]
        
        if op == '1':
            val = int(line[1])
            if not min_stack:
                min_stack.append(val)
            else:
                curr_min = min_stack[-1]
                min_stack.append(val if val < curr_min else curr_min)
                
        elif op == '2':
            min_stack.pop()
            
        else:
            out.append(str(min_stack[-1]))
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_1()