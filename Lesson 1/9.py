import sys

def task_9():
    line1 = sys.stdin.readline()
    if not line1:
        return
    n = int(line1.strip())
    
    line2 = sys.stdin.readline()
    p = [int(x) for x in line2.split()]
    
    has_one = [False] * (n + 2)
    ptr = n
    ans = ["1"]
    
    for i in range(n):
        has_one[p[i]] = True
        while has_one[ptr]:
            ptr -= 1
        passes = 1 + (i + 1) - (n - ptr)
        ans.append(str(passes))
    sys.stdout.write(' '.join(ans) + '\n')

if __name__ == '__main__':
    task_9()