def get_groups(lines):
    return "".join(lines).split("\n\n")


def one(lines):
    return sum(
        [len(set(group.replace("\n", ""))) for group in get_groups(lines)])


def two(lines):
    yeses_by_group = [
        set(group.strip().split("\n")) for group in get_groups(lines)
    ]
    sum = 0
    for group in yeses_by_group:
        common_yeses = set("abcdefghijklmnopqrstuvwxyz")
        for form in group:
            common_yeses = common_yeses & set(form)
        sum += len(common_yeses)
    return sum


f = open("input.txt")
lines = f.readlines()
print(one(lines))
print(two(lines))
