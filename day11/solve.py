import copy


def find_visible(pos, lobby):
    found = [[0 for i in range(0)] for j in range(0)]
    print(found)
    # nw = None
    # while not nw:
    # visible = lobby[pos-1][pos-1]


def one(lobby, limit, visible=False):
    # apply padding around seats
    lobby.insert(0, ["."] * 10)
    lobby.append(["."] * 10)
    for row in lobby:
        row.insert(0, ".")
        row.append(".")

    motion = True
    while motion:
        motion = False
        old_lobby = copy.deepcopy(lobby)
        for i, row in enumerate(old_lobby):
            for j, seat in enumerate(row):
                if seat == ".":
                    continue
                # for two, fix this to match new visibility rules
                adjacent_seats = old_lobby[i - 1][j - 1:j + 2] + [
                    old_lobby[i][j - 1]
                ] + [old_lobby[i][j + 1]] + old_lobby[i + 1][j - 1:j + 2]
                num_occupied_adjacent = len(
                    [seat for seat in adjacent_seats if seat == "#"])
                if seat == "L" and num_occupied_adjacent == 0:
                    motion = True
                    lobby[i][j] = "#"
                if seat == "#" and num_occupied_adjacent >= limit:
                    motion = True
                    lobby[i][j] = "L"

    occupied = [seat for row in lobby for seat in row if seat == "#"]
    print(len(occupied))


lobby = [[seat for seat in line.strip()]
         for line in open("input.txt").readlines()]
# one(lobby, 4)
find_visible((5, 5), lobby)
