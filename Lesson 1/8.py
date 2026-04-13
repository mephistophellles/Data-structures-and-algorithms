import sys

def task_8():
    line1 = sys.stdin.readline()
    if not line1:
        return
    n = int(line1.strip())
    
    s = sys.stdin.readline().strip()
    counts = [0] * 26
    for char in s:
        counts[ord(char) - 65] += 1
    prefix = []
    center = ""
    for i in range(26):
        if counts[i] >= 2:
            prefix.append(chr(i + 65) * (counts[i] // 2))
    for i in range(26):
        if counts[i] % 2 == 1:
            center = chr(i + 65)
            break
    left_part = "".join(prefix)
    ans = left_part + center + left_part[::-1]
    sys.stdout.write(ans + '\n')

if __name__ == '__main__':
    task_8()