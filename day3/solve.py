# This will take the list of input lines and extrapolate them
# out to a full forest of trees. We're moving right 3 down 1 so it needs
# to be three times as wide as it is long.
def makeForest(lines, widthMultiplier):

    rows = len(lines)
    cols = len(lines[0].strip("\n"))
    repeat = ((rows / cols) + 1) * widthMultiplier
    forest = [line.strip("\n") * repeat for line in lines]
    return forest


# Now we move through the forest and mark when we hit a tree
def getTreesHit(forest, right, down):
    treesHit = 0
    col, row = 0, 0
    for line in forest:
        col += right
        row += down
        try:
            if forest[row][col] == "#":
                treesHit += 1
        except IndexError:  # we're out of the forest!
            break

    return treesHit


def one(rows):
    forest = makeForest(rows, 3)
    return getTreesHit(forest, 3, 1)


def two(rows):
    forest = makeForest(rows, 7)
    return (
        getTreesHit(forest, 1, 1)
        * getTreesHit(forest, 3, 1)
        * getTreesHit(forest, 5, 1)
        * getTreesHit(forest, 7, 1)
        * getTreesHit(forest, 1, 2)
    )


f = open("input.txt")
lines = f.readlines()
print(one(lines))
print(two(lines))
