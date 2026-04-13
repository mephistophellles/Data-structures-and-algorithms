import sys

def task_3():
    n = int(sys.stdin.readline().strip())
    L = 1
    R = n
    while L < R:
        mid = (L + R + 1) // 2
        print(mid, flush=True)
        response = sys.stdin.readline().strip()
        if response == ">=":
            L = mid
        else:
            R = mid - 1
    print(f"! {L}", flush=True)

if __name__ == '__main__':
    task_3()