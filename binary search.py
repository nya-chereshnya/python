from math import floor


def binary_search(arr, target, left_border, right_border):
    if left_border > right_border:
        return -1
    mid = left_border + floor((right_border - left_border) / 2)
    if arr[mid] == target:
        return mid+1
    if arr[mid] > target:
        return binary_search(arr, target, left_border, mid - 1)
    return binary_search(arr, target, mid + 1, right_border)


n, *A = map(int, input().split())
k, *B = map(int, input().split())
for i in B:
    print(binary_search(A, i, 0, n-1), end=' ')
