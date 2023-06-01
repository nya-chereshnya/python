

def NOD(a, b):
    nums = [a, b]
    if 0 in nums:
        return b if b else a
    return NOD(min(nums), max(nums) % min(nums))


print(NOD(14159572, 63967072))


