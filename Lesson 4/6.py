import sys

def task_6():
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
    
    segments = []
    for _ in range(n):
        l = int(next(tokens))
        r = int(next(tokens))
        segments.append((l, r))
    segments.sort()
    
    total_length = 0
    curr_l, curr_r = segments[0]
    
    for i in range(1, n):
        l, r = segments[i]
        
        if l <= curr_r:
            if r > curr_r:
                curr_r = r
        else:
            total_length += (curr_r - curr_l)
            curr_l, curr_r = l, r
            
    total_length += (curr_r - curr_l)
    
    sys.stdout.write(str(total_length) + '\n')

if __name__ == '__main__':
    task_6()