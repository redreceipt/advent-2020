import pprint
import copy


def find_adjacent(row, col, lobby, stop_at_one=True):
    found = [[0 for i in range(3)] for j in range(3)]

    # if row == 1 and col == 1:
    # import pdb
    # pdb.set_trace()

    def look_direction(y, x):
        distance = 1
        seat = None
        while True:
            try:
                if row + y * distance == -1 or col + x * distance == -1:
                    raise IndexError
                seat = lobby[row + y * distance][col + x * distance]
            except IndexError:
                break
            if seat == "#":
                found[1 + y][1 + x] = 1
                break
            if stop_at_one or seat == "L":
                break
            distance += 1

    look_direction(-1, -1)  # NW
    look_direction(-1, 0)  # N
    look_direction(-1, 1)  # NE
    look_direction(0, -1)  # W
    look_direction(0, 1)  # E
    look_direction(1, -1)  # SW
    look_direction(1, 0)  # S
    look_direction(1, 1)  # SE

    return [seat for row in found for seat in row]


def simulate(lobby, limit, stop_at_one=True):
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
                adjacent_seats = find_adjacent(i, j, old_lobby, stop_at_one)
                # print(adjacent_seats)
                num_occupied_adjacent = len(
                    [seat for seat in adjacent_seats if seat == 1])
                if seat == "L" and num_occupied_adjacent == 0:
                    motion = True
                    lobby[i][j] = "#"
                if seat == "#" and num_occupied_adjacent >= limit:
                    motion = True
                    lobby[i][j] = "L"
        # print("lobby")
        # pprint.pprint(lobby)
        # import pdb
        # pdb.set_trace()

    occupied = [seat for row in lobby for seat in row if seat == "#"]
    print(len(occupied))


lobby = [[seat for seat in line.strip()]
         for line in open("input.txt").readlines()]
# simulate(lobby, 4)
simulate(lobby, 5, False)
