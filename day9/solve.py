def get_numbers(lines):
    return [int(line.strip()) for line in lines]


def one(preamble_length):
    for i, number in enumerate(numbers):
        found = False
        if i < preamble_length:
            continue
        for first_number in numbers[i - preamble_length:i]:
            for second_number in numbers[i - preamble_length:i]:
                if first_number + second_number == number:
                    found = True

        if not found:
            return (i, number)


def two(error_number):
    valid_numbers = numbers[:error_number[0]]
    for i, first_number in enumerate(valid_numbers):
        for j, last_number in enumerate(valid_numbers):
            if sum(valid_numbers[i:j]) == error_number[1]:
                sequence = valid_numbers[i:j]
                return max(sequence) + min(sequence)


f = open("input.txt")
lines = f.readlines()
numbers = get_numbers(lines)
error_number = one(25)
print(error_number)
print(two(error_number))
