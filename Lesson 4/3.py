import sys

def task_3():
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
    
    coords = [int(next(tokens)) for _ in range(n)]
    left = 0
    right = coords[-1] - coords[0]
    
    while left < right:
        mid = (left + right + 1) // 2
        
        cows_placed = 1
        last_pos = coords[0]
        
        for i in range(1, n):
            if coords[i] - last_pos >= mid:
                cows_placed += 1
                last_pos = coords[i]
        if cows_placed >= k:
            left = mid
        else:
            right = mid - 1
    sys.stdout.write(str(left) + '\n')

if __name__ == '__main__':
    task_3()