import sys
sys.setrecursionlimit(200000)

def task_2():
    first_line = sys.stdin.readline()
    if not first_line:
        return
    n, r = map(int, first_line.split())
    
    tree = []
    for _ in range(n):
        left_child, right_child = map(int, sys.stdin.readline().split())
        tree.append((left_child, right_child))
        
    def dfs(u):
        if u == -1:
            return True, float('inf'), float('-inf'), 0
        left_child, right_child = tree[u]
        ok_l, min_l, max_l, h_l = dfs(left_child)
        if not ok_l:
            return False, 0, 0, 0
        ok_r, min_r, max_r, h_r = dfs(right_child)
        if not ok_r:
            return False, 0, 0, 0
        if max_l >= u or min_r <= u:
            return False, 0, 0, 0
        if abs(h_l - h_r) > 1:
            return False, 0, 0, 0
        current_min = min(u, min_l)
        current_max = max(u, max_r)
        current_h = max(h_l, h_r) + 1
        return True, current_min, current_max, current_h
    is_avl, _, _, _ = dfs(r)
    
    sys.stdout.write("1\n" if is_avl else "0\n")

if __name__ == '__main__':
    task_2()