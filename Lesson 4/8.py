import sys

def task_8():
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
    c = int(next(tokens))
    
    tasks = []
    for i in range(1, n + 1):
        start = int(next(tokens))
        duration = int(next(tokens))
        tasks.append((start + duration, start, i))
        
    tasks.sort()
    
    selected_tasks = []
    current_end_time = 0
    
    for finish, start, idx in tasks:
        if start >= current_end_time:
            selected_tasks.append(idx)
            current_end_time = finish
    max_score = len(selected_tasks) * c
    
    sys.stdout.write(str(max_score) + '\n')
    sys.stdout.write(str(len(selected_tasks)) + '\n')
    sys.stdout.write(' '.join(map(str, selected_tasks)) + '\n')

if __name__ == '__main__':
    task_8()