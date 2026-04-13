import sys

def task_4():
    first_line = sys.stdin.readline()
    if not first_line:
        return
    n = int(first_line.strip())
    
    heap = []
    out = []
    
    for _ in range(n):
        line = sys.stdin.readline().split()
        if not line:
            break
            
        if line[0] == '0':
            val = int(line[1])
            heap.append(val)
            idx = len(heap) - 1
            while idx > 0:
                parent = (idx - 1) // 2
                if heap[parent] < heap[idx]:
                    heap[parent], heap[idx] = heap[idx], heap[parent]
                    idx = parent
                else:
                    break
        else:
            out.append(str(heap[0]))
            last_val = heap.pop()
            
            if heap:
                heap[0] = last_val
                idx = 0
                size = len(heap)
                while True:
                    left = 2 * idx + 1
                    if left >= size:
                        break
                        
                    right = left + 1
                    largest = left
                    if right < size and heap[right] > heap[left]:
                        largest = right
                    if heap[largest] > heap[idx]:
                        heap[idx], heap[largest] = heap[largest], heap[idx]
                        idx = largest
                    else:
                        break 
                        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    task_4()