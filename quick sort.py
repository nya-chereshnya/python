

def quick_sort(arr):
    l = 0
    r = len(arr) - 1
    mid = (l + r) // 2
    print(arr[mid])
    while l < mid:
        if arr[l] > arr[mid] and arr[r] < arr[mid]:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        if arr[l] > arr[mid]:
            r -= 1
        else:
            l += 1
        if arr[r] < arr[mid]:
            l += 1
        else:
            r -= 1
    if arr[l-1] > arr[mid]:
        arr[l-1], arr[mid] = arr[mid], arr[l-1]
    return arr



print(quick_sort([5, 16, 13, 8, 6, 1, 2, 11]))
# print(quick_sort([6, 5, 1, 3, 8, 4, 7, 9, 2]))
