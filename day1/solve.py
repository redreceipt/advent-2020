f = open("input.txt")
nums = [int(num) for num in f.read().split("\n") if num != ""]

found = False
for x in nums:
    for y in nums:
        for z in nums:
            if x + y + z == 2020:
                found = True
                break
        if found:
            break
    if found:
        break


print(x * y * z)
