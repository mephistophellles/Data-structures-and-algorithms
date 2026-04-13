import sys

def task_1():
    def get_tokens():
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            for token in line.split():
                yield token

    tokens = get_tokens()
    
    try:
        n = int(next(tokens))
    except StopIteration:
        return
        
    cost = [int(next(tokens)) for _ in range(n)]
    if n == 1:
        sys.stdout.write(str(cost[0]) + '\n')
        return
        
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    sys.stdout.write(str(dp[n-1]) + '\n')

if __name__ == '__main__':
    task_1()