import re


def one(lines):
    data = {}
    for line in lines:
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
            or_mask = int(re.sub("X", "0", mask), 2)
            and_mask = int(re.sub("X", "1", mask), 2)
        else:
            address, write = (int(
                re.sub(r"[me\[\]]", "",
                       line.split("=")[0].strip())),
                              int(line.split("=")[1].strip()))

            value = write
            value |= or_mask
            value &= and_mask
            data[address] = value

    return sum([value for value in data.values()])


def two(lines):
    data = {}
    for line in lines:
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
            or_mask = int(re.sub("X", "0", mask), 2)
        else:
            address, write = (int(
                re.sub(r"[me\[\]]", "",
                       line.split("=")[0].strip())),
                              int(line.split("=")[1].strip()))

            value = write
            value |= or_mask

        print(mask)


lines = [line.strip() for line in open("example2.txt")]
# print(one(lines))
print(two(lines))
