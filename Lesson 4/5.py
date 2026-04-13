import sys

def task_5():
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token

    tokens = get_tokens()
    
    try:
        n_str = next(tokens)
    except StopIteration:
        return
        
    n = int(n_str)
    k = int(next(tokens))
    
    a = [int(next(tokens)) for _ in range(n)]
    
    left = max(a)
    right = sum(a)
    
    while left < right:
        mid = (left + right) // 2
        segments_count = 1
        current_sum = 0
        
        for val in a:
            if current_sum + val > mid:
                segments_count += 1
                current_sum = val
            else:
                current_sum += val
        if segments_count > k:
            left = mid + 1
        else:
            right = mid
    sys.stdout.write(str(left) + '\n')

if __name__ == '__main__':
    task_5()