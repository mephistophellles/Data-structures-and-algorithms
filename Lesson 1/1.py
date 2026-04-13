import sys

def first():
    first_line = sys.stdin.readline().split()
    if not first_line:
        return
    arr_set = set(sys.stdin.readline().split())
    queries = sys.stdin.readline().split()
    result = ["YES" if q in arr_set else "NO" for q in queries]
    sys.stdout.write('\n'.join(result) + '\n')

if __name__ == '__main__':
    first()