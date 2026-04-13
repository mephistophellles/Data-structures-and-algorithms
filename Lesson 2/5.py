import sys

def task_5():
    tokens = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        tokens.extend(line.split())
        if tokens:
            n = int(tokens[0])
            if len(tokens) >= n + 1:
                break
                
    if not tokens:
        return
        
    n = int(tokens[0])
    cars = [int(x) for x in tokens[1:n+1]]
    
    stack = []
    ops = []
    expected = 1
    
    for car in cars:
        stack.append(car)
        ops.append(1)
        
        while stack and stack[-1] == expected:
            stack.pop()
            ops.append(2)
            expected += 1
            
    if stack:
        sys.stdout.write("0\n")
        return
        
    compressed = []
    if ops:
        curr_op = ops[0]
        count = 1
        for i in range(1, len(ops)):
            if ops[i] == curr_op:
                count += 1
            else:
                compressed.append(f"{curr_op} {count}")
                curr_op = ops[i]
                count = 1
        compressed.append(f"{curr_op} {count}")
    sys.stdout.write(str(len(compressed)) + "\n")
    sys.stdout.write("\n".join(compressed) + "\n")

if __name__ == '__main__':
    task_5()