

def merge_sort(arr):
    if len(arr) == 1:
        return arr, 0

    l, inv_l = merge_sort(arr[:len(arr)//2])
    r, inv_r = merge_sort(arr[len(arr)//2:])
    inversions = inv_l + inv_r
    res = []
    l_p = 0
    r_p = 0

    while l_p < len(l) and r_p < len(r):
        if l[l_p] > r[r_p]:
            inversions += len(l) - l_p
            res.append(r[r_p])
            r_p += 1
            continue
        res.append(l[l_p])
        l_p += 1

    res += l[l_p:]
    res += r[r_p:]
    return res, inversions


inversions = 0
n = int(input())
arr = list(map(int, input().split()))
sorted_arr, num_inversions = merge_sort(arr)
print(num_inversions)
