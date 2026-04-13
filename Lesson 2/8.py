import sys

def task_8():
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
    a = [int(x) for x in tokens[1:n+1]]
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i+1] = pref[i] + a[i]
    a.append(-1)
    
    stack = []
    max_ans = 0
    
    for i in range(n + 1):
        curr_val = a[i]
        while stack and a[stack[-1]] >= curr_val:
            idx = stack.pop()
            left_idx = stack[-1] if stack else -1
            right_idx = i
            
            subarray_sum = pref[right_idx] - pref[left_idx + 1]
            ans = a[idx] * subarray_sum
            
            if ans > max_ans:
                max_ans = ans
                
        stack.append(i)
        
    sys.stdout.write(str(max_ans) + '\n')

if __name__ == '__main__':
    task_8()