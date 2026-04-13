import sys
from collections import deque

def task_3():
    n, k = map(int, sys.stdin.readline().split())

    coins = [0] * (n + 1)
    values = list(map(int, sys.stdin.readline().split()))
    for i, v in enumerate(values):
        coins[i + 2] = v

    NEG_INF = float('-inf')
    dp = [NEG_INF] * (n + 1)
    dp[1] = 0
    prev = [-1] * (n + 1)

    dq = deque([1])

    for i in range(2, n + 1):
        while dq and dq[0] < i - k:
            dq.popleft()

        if dq:
            dp[i] = dp[dq[0]] + coins[i]
            prev[i] = dq[0]

        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        dq.append(i)

    path = []
    curr = n
    while curr != -1:
        path.append(curr)
        curr = prev[curr]
    path.reverse()

    sys.stdout.write(str(dp[n]) + '\n')
    sys.stdout.write(str(len(path) - 1) + '\n')
    sys.stdout.write(' '.join(map(str, path)) + '\n')

if __name__ == '__main__':
    task_3()
