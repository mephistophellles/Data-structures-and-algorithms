import sys

def task_7():
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line.strip())
    if n == 0:
        return
    a = list(range(1, n + 1))
    for i in range(2, n):
        a[i], a[i // 2] = a[i // 2], a[i]
    sys.stdout.write(' '.join(map(str, a)) + '\n')

if __name__ == '__main__':
    task_7()