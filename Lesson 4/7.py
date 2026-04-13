import sys

def task_7():
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
    diff = [0] * 86402
    
    for _ in range(n):
        h1 = int(next(tokens))
        m1 = int(next(tokens))
        s1 = int(next(tokens))
        h2 = int(next(tokens))
        m2 = int(next(tokens))
        s2 = int(next(tokens))
        
        start_sec = h1 * 3600 + m1 * 60 + s1
        end_sec = h2 * 3600 + m2 * 60 + s2
        
        if start_sec == end_sec:
            diff[0] += 1
            diff[86400] -= 1
        elif start_sec < end_sec:
            diff[start_sec] += 1
            diff[end_sec] -= 1
        else:
            diff[start_sec] += 1
            diff[86400] -= 1
            diff[0] += 1
            diff[end_sec] -= 1
            
    active_counters = 0
    total_time = 0
    for i in range(86400):
        active_counters += diff[i]
        
        if active_counters == n:
            total_time += 1
            
    sys.stdout.write(str(total_time) + '\n')

if __name__ == '__main__':
    task_7()