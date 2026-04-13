import sys

def task_6():
    first_line = sys.stdin.readline()
    if not first_line:
        return
    n = int(first_line.strip())
    queue_array = [0] * n
    pos = [0] * 100005
    
    head = 0
    tail = 0
    
    out = []
    
    for _ in range(n):
        line = sys.stdin.readline().split()
        op = line[0]
        
        if op == '1':
            person_id = int(line[1])
            queue_array[tail] = person_id
            pos[person_id] = tail
            tail += 1
            
        elif op == '2':
            if head < tail:
                head += 1
                
        elif op == '3':
            if tail > head:
                tail -= 1
                
        elif op == '4':
            person_id = int(line[1])
            out.append(str(pos[person_id] - head))
            
        else: # op == '5'
            if head < tail:
                out.append(str(queue_array[head]))
                
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_6()