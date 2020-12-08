def get_rules(lines):
    def clean_color(color):
        return color.strip().replace(" bags", "").replace(" bag",
                                                          "").replace(".", "")

    return {
        parent.strip().replace(" bags", ""): {
            clean_color(child)[2:]:
            clean_color(child)[0] if "no" not in child else 0
            for child in children.split(",")
        }
        for parent, children in [line.split("contain") for line in lines]
    }


def one(lines, color):
    rules = get_rules(lines)
    ancestors = set()

    def getParents(child):
        parents = set([
            parent for parent in rules.keys() if child in rules[parent].keys()
        ])
        ancestors.update(parents)
        for parent in parents:
            getParents(parent)

    getParents(color)
    return len(ancestors)


def two(lines, color):
    rules = get_rules(lines)
    num_bags = 0

    def get_children(parent):
        nonlocal num_bags
        children = [[child] * int(rules[parent][child])
                    for child in rules[parent].keys()]
        for group in children:
            num_bags += len(group)
            for child in group:
                get_children(child)

        return children

    get_children(color)
    return num_bags


f = open("input.txt")
lines = f.readlines()
print(one(lines, "shiny gold"))
print(two(lines, "shiny gold"))
