import sys

def task_5():
    line = sys.stdin.readline().split()
    if not line:
        return
    a, b, c, d = map(float, line)
    if a < 0:
        a, b, c, d = -a, -b, -c, -d
    L = -10000.0
    R = 10000.0
    for _ in range(100):
        mid = (L + R) / 2.0
        val = ((a * mid + b) * mid + c) * mid + d
        if val > 0:
            R = mid
        else:
            L = mid
    print(f"{R:.19f}")

if __name__ == '__main__':
    task_5()