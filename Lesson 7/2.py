import sys

def task_2():
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line.strip())
    ends_with_A = 1
    ends_with_BC = 2
    
    for _ in range(2, n + 1):
        next_A = ends_with_BC
        next_BC = 2 * (ends_with_A + ends_with_BC)
        
        ends_with_A = next_A
        ends_with_BC = next_BC
        
    sys.stdout.write(str(ends_with_A + ends_with_BC) + '\n')

if __name__ == '__main__':
    task_2()