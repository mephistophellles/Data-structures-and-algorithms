import sys
import math

def task_4():
    line = sys.stdin.readline()
    if not line:
        return
    c = float(line.strip())
    
    L = 0.0
    R = 100000.0
    for _ in range(100):
        mid = (L + R) / 2.0
        
        if mid * mid + math.sqrt(mid + 1.0) < c:
            L = mid
        else:
            R = mid
    print(f"{R:.20f}")

if __name__ == '__main__':
    task_4()