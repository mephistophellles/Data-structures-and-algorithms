import sys

def task_6():
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    m = int(data[1])
    a = [int(x) for x in data[2:2+m]]
    total_money = 2 * sum(a)
    if total_money < n:
        sys.stdout.write("-1\n")
        return
    a.sort(reverse=True)
    suffix_sum = [0] * (m + 1)
    for i in range(m - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i+1] + 2 * a[i]
        
    best_count = 100
    best_combo = []
    
    current_combo = []
    def dfs(idx, current_sum, current_count):
        nonlocal best_count, best_combo
        if current_sum == n:
            if current_count < best_count:
                best_count = current_count
                best_combo = list(current_combo)
            return
            
        if idx == m:
            return
        if current_sum > n:
            return
        if current_sum + suffix_sum[idx] < n:
            return
        if current_count >= best_count:
            return
        if current_sum + 2 * a[idx] <= n:
            current_combo.append(a[idx])
            current_combo.append(a[idx])
            dfs(idx + 1, current_sum + 2 * a[idx], current_count + 2)
            current_combo.pop()
            current_combo.pop()
        if current_sum + a[idx] <= n:
            current_combo.append(a[idx])
            dfs(idx + 1, current_sum + a[idx], current_count + 1)
            current_combo.pop()
        dfs(idx + 1, current_sum, current_count)

    dfs(0, 0, 0)
    if best_count != 100:
        best_combo.sort()
        sys.stdout.write(f"{best_count}\n")
        sys.stdout.write(" ".join(map(str, best_combo)) + "\n")
    else:
        sys.stdout.write("0\n")

if __name__ == '__main__':
    task_6()