import sys

def task_4():
    line1 = sys.stdin.readline()
    if not line1:
        return
    n = int(line1.strip())
    
    if n == 0:
        sys.stdout.write("0\n")
        return
    colors = sys.stdin.readline().split()
    stack = []
    destroyed = 0
    
    for color in colors:
        while stack and stack[-1][0] != color and stack[-1][1] >= 3:
            destroyed += stack[-1][1]
            stack.pop()
        if stack and stack[-1][0] == color:
            stack[-1][1] += 1
        else:
            stack.append([color, 1])
    while stack and stack[-1][1] >= 3:
        destroyed += stack[-1][1]
        stack.pop()
        
    sys.stdout.write(str(destroyed) + '\n')

if __name__ == '__main__':
    task_4()