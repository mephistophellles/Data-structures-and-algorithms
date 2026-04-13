import sys

def task_3():
    line = sys.stdin.readline()
    if not line:
        return
        
    tokens = line.split()
    stack = []
    
    for token in tokens:
        if token == '+':
            right = stack.pop()
            left = stack.pop()
            stack.append(left + right)
        elif token == '-':
            right = stack.pop()
            left = stack.pop()
            stack.append(left - right)
        elif token == '*':
            right = stack.pop()
            left = stack.pop()
            stack.append(left * right)
        else:
            stack.append(int(token))
            
    sys.stdout.write(str(stack[0]) + '\n')

if __name__ == '__main__':
    task_3()