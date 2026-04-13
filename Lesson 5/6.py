import sys

def task_6():
    s = sys.stdin.readline().strip()
    if not s:
        return
    T = "^#" + "#".join(s) + "#$"
    n = len(T)
    
    P = [0] * n
    C = 0
    R = 0
    
    ans = 0

    for i in range(1, n - 1):
        i_mirror = 2 * C - i
        if R > i:
            P[i] = min(R - i, P[i_mirror])
        else:
            P[i] = 0
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        if i + P[i] > R:
            C = i
            R = i + P[i]

        ans += (P[i] + 1) // 2

    sys.stdout.write(str(ans) + '\n')
if __name__ == '__main__':
    task_6()