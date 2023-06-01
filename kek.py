n, max_volume = map(int, input().split())
jewels = []


class Jewel:
    def __init__(self, price, volume):
        self.price = price
        self.volume = volume
        self.__coef = self.price / self.volume
        self.coef = self.__coef


for i in range(n):
    price, volume = map(int, input().split())
    jewels.append(Jewel(price, volume))

jewels = sorted(jewels, key=lambda x: x.coef, reverse=True)
# print([i.coef for i in jewels])

sum_volume = 0
total_price = 0
for i in range(n):
    if sum_volume + jewels[i].volume == max_volume:
        total_price += jewels[i].price
        # print(sum_volume, total_price, '222')
        break
    if sum_volume + jewels[i].volume < max_volume:
        total_price += jewels[i].price
        sum_volume += jewels[i].volume
        # print(total_price)
    elif sum_volume + jewels[i].volume > max_volume:
        total_price += (max_volume - sum_volume) * jewels[i].coef
        # print(total_price, '111')
        break

print('{:.3f}'.format(total_price))
