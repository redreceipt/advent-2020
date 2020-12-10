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
    branches = {}
    num_paths = 1

    for adapter in adapters:
        next_adapters = [
            next_adapter for next_adapter in adapters
            if next_adapter > adapter and next_adapter - adapter <= 3
        ]
        num_paths += len(next_adapters) - num_paths
        branches[adapter] = next_adapters

    def find_options(adapter):
        nonlocal num_paths
        options = branches[adapter]
        if not (len(options)):
            return
        num_paths -= 1
        for option in options:
            num_paths += 1
            find_options(option)

    find_options(0)
    return num_paths + 1


adapters = [int(line.strip()) for line in open("example2.txt").readlines()]
print(one())
print(two())
