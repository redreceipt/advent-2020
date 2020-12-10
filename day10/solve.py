def one():
    adapters_left = adapters.copy()
    current_joltage = 0
    ones = 0
    threes = 1
    while len(adapters_left):
        next_adapter = min(adapters_left)
        diff = next_adapter - current_joltage
        current_joltage = next_adapter
        if diff == 1:
            ones += 1
        else:
            threes += 1
        adapters_left.remove(next_adapter)

    return ones * threes


def two():
    my_adapter = max(adapters) + 3
    adapters.append(my_adapter)
    chains = []

    def make_arrangements(path):
        highest = path[-1]
        next_adapters = [
            joltage for joltage in adapters
            if joltage - highest <= 3 and joltage - highest > 0
        ]
        for joltage in next_adapters:
            new_path = path + (joltage, )
            if joltage == my_adapter:
                chains.append(new_path)
            make_arrangements(new_path)

    make_arrangements((0, ))
    return len(chains)


adapters = [int(line.strip()) for line in open("example.txt").readlines()]
print(one())
print(two())
