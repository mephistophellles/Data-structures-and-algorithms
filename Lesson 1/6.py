import sys

def merge_sort_and_count(arr, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_and_count(arr, temp, left, mid)
        inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
        i = left
        j = mid + 1
        k = left
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
            
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
            
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
            
        for i in range(left, right + 1):
            arr[i] = temp[i]
            
    return inv_count

def task_6():
    line1 = sys.stdin.readline()
    if not line1:
        return
    n = int(line1.strip())
    line2 = sys.stdin.readline()
    a = [int(x) for x in line2.split()]
    temp = [0] * n
    inversions = merge_sort_and_count(a, temp, 0, n - 1)
    sys.stdout.write(str(inversions) + '\n')
    sys.stdout.write(' '.join(map(str, a)) + '\n')

if __name__ == '__main__':
    task_6()