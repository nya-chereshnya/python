# f = []

# for i in range(n):
#     f.append(list(map(int, input().split())))

# class Jewel:
#     def __init__(self, price, volume) -> None:
#         self.price = price
#         self.volume = volume

# amount, max_volume = map(int, input().split())
# jewels = []

# for i in range(amount):
#     jewels.append(Jewel(*map(int, input().split())))

class Segment:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        # self.range = [i for i in range(left, right+1)]
        self.nailed = False


n = int(input())
segments = []
for i in range(n):
    segments.append(Segment(*map(int, input().split())))

nails = []


segments = sorted(segments, key=lambda x: x.right)


def nailed_checker(segments, nail):
    for i in range(len(segments)):
        # print(nail, segments[i].left,  segments[i].right, 'i')
        if nail <= segments[i].right and nail >= segments[i].left:
            # print(segments[i].range)
            segments[i].nailed = True
    # print([i.nailed for i in segments])
    return True


def get_min_nails(segments):
    nails = []
    nails.append(segments[0].right)
    nailed_checker(segments, segments[0].right)
    # print([i.nailed for i in segments])
    for i in range(1, n):
        # print([i.nailed for i in segments])
        # print(segments[i].right)
        if segments[i].nailed == True:
            # print(segments[i].right)
            continue
        if segments[i].left > segments[i-1].right:
            # print(segments[i].right)
            nails.append(segments[i].right)
            nailed_checker(segments, segments[i].right)
            continue
        # print(segments[i].right)
        if segments[i].right >= segments[i-1].left:
            # print(segments[i].right)
            nails.append(segments[i].right)
            nailed_checker(segments, segments[i].right)
            continue
    # print([i.nailed for i in segments])
    return nails


if n == 0:
    print()
else:
    min_nails = get_min_nails(segments)
    print(len(min_nails))
    print(*min_nails)
    # print([i.nailed for i in segments])
# else:
#     nails.append(segments[0].right)

# print(len(nails))
# print(*nails)
