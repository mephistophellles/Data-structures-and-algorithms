import sys

def task_5():
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

    def sift_down(start, end):
        root = start
        while True:
            left_child = 2 * root + 1
            if left_child > end:
                break
                
            right_child = left_child + 1
            largest = root
            
            if a[left_child] > a[largest]:
                largest = left_child
                
            if right_child <= end and a[right_child] > a[largest]:
                largest = right_child
                
            if largest == root:
                break

            a[root], a[largest] = a[largest], a[root]
            root = largest
            
    for i in range((n // 2) - 1, -1, -1):
        sift_down(i, n - 1)
        
    for end_idx in range(n - 1, 0, -1):
        a[0], a[end_idx] = a[end_idx], a[0]
        sift_down(0, end_idx - 1)
        
    sys.stdout.write(' '.join(map(str, a)) + '\n')

if __name__ == '__main__':
    task_5()