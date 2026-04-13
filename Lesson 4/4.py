import sys

def task_4():
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token

    tokens = get_tokens()
    
    try:
        n = int(next(tokens))
        k = int(next(tokens))
    except StopIteration:
        return
        
    left = 1
    right = n * n
    
    while left < right:
        mid = (left + right) // 2
        count = 0
        for i in range(1, n + 1):
            count += min(n, mid // i)
        if count < k:
            left = mid + 1
        else:
            right = mid
            
    sys.stdout.write(str(left) + '\n')

if __name__ == '__main__':
    task_4()