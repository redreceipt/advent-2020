def get_rules(lines):
    return {
        parent.strip().replace(" bags", ""): [
            child.strip().replace(" bags", "").replace(" bag", "").replace(
                ".", "")[2:] if "no" not in child else None
            for child in children.split(",")
        ]
        for parent, children in [line.split("contain") for line in lines]
    }


def one(lines, color):
    rules = get_rules(lines)

    ancestors = set()

    def getParents(child):
        parents = set(
            [parent for parent in rules.keys() if child in rules[parent]])
        ancestors.update(parents)
        for parent in parents:
            getParents(parent)

    getParents(color)
    return len(ancestors)


def two(lines, color):
    pass


f = open("input.txt")
print(one(f.readlines(), "shiny gold"))
