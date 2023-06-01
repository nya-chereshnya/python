n = int(input())

order = [1]
temp_sum = 1

for i in range(2, n+1):
    if temp_sum == n:
        break
    elif temp_sum + i == n:
        order.append(i)
        break
    elif i + temp_sum < n:
        order.append(i)
        temp_sum += i
    elif i + temp_sum > n:
        temp_sum -= order[-1]
        order.pop(-1)
        order.append(i)
        temp_sum += i

print(len(order))
print(*order)
