def one(rows):
    valid = 0
    for row in rows:
        policy, letter, password = row.split(" ")
        low, high = policy.split("-")
        count = password.count(letter[0])
        if int(count) >= int(low) and int(count) <= int(high):
            valid += 1
    return valid


def two(rows):
    valid = 0
    for row in rows:
        policy, letter, password = row.split(" ")
        first, second = policy.split("-")
        if (
            password[int(first) - 1] == letter[0]
            and password[int(second) - 1] != letter[0]
        ) or (
            password[int(first) - 1] != letter[0]
            and password[int(second) - 1] == letter[0]
        ):
            valid += 1
    return valid


f = open("input.txt")
rows = [row for row in f.read().split("\n") if row != ""]

print(one(rows))
print(two(rows))
