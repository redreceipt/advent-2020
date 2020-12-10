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
    adapters.insert(0, 0)
    adapters.append(max(adapters) + 3)
    adapters.sort()
    chains = []

    def make_arrangements(path):
        ndx = adapters.index(path[-1])
        next_adapters = [
            adapter for adapter in adapters[ndx + 1:]
            if adapter - path[-1] <= 3
        ]
        for joltage in next_adapters:
            new_path = path + (joltage, )
            if joltage == adapters[-1]:
                chains.append(new_path)
            make_arrangements(new_path)

    make_arrangements((0, ))
    return len(chains)


adapters = [int(line.strip()) for line in open("input.txt").readlines()]
print(one())
print(two())
