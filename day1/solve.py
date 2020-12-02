def one(nums):
    for x in nums:
        for y in nums:
            if x + y == 2020:
                return x * y


def two(nums):
    for x in nums:
        for y in nums:
            for z in nums:
                if x + y + z == 2020:
                    return x * y * z


f = open("input.txt")
nums = [int(num) for num in f.read().split("\n") if num != ""]


print(one(nums))
print(two(nums))
