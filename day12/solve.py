def one(moves):
    # x, y
    pos = (0, 0)
    # degrees
    direction = 0
    directionMap = {0: (1, 0), 90: (0, 1), 180: (-1, 0), 270: (0, -1)}
    for move in moves:
        action, value = move[0], int(move[1:])
        if action == "F":
            pos = (pos[0] + directionMap[direction][0] * value,
                   pos[1] + directionMap[direction][1] * value)
        if action == "L":
            direction = (direction + value) % 360
        if action == "R":
            direction = (direction - value) % 360
        if action == "N":
            pos = (pos[0], pos[1] + value)
        if action == "S":
            pos = (pos[0], pos[1] - value)
        if action == "E":
            pos = (pos[0] + value, pos[1])
        if action == "W":
            pos = (pos[0] - value, pos[1])
    return abs(pos[0]) + abs(pos[1])


def two(moves):
    waypoint = (10, 1)
    ship = (0, 0)
    waypoint_angle_map = {
        (1, 1): {
            0: (1, 1),
            90: (-1, 1),
            180: (-1, -1),
            270: (1, -1)
        },
        (0, 1): {
            0: (0, 1),
            90: (-1, 0),
            180: (0, -1),
            270: (1, 0)
        },
        (-1, 1): {
            0: (-1, 1),
            90: (-1, -1),
            180: (1, -1),
            270: (1, 1)
        },
        (-1, 0): {
            0: (-1, 0),
            90: (0, -1),
            180: (1, 0),
            270: (0, 1)
        },
        (-1, -1): {
            0: (-1, -1),
            90: (1, -1),
            180: (1, 1),
            270: (-1, 1)
        },
        (0, -1): {
            0: (0, -1),
            90: (1, 0),
            180: (0, 1),
            270: (-1, 0)
        },
        (1, -1): {
            0: (1, -1),
            90: (1, 1),
            180: (-1, 1),
            270: (-1, -1)
        },
        (1, 0): {
            0: (1, 0),
            90: (0, 1),
            180: (-1, 0),
            270: (0, -1)
        },
    }
    spin = {"L": 1, "R": -1}
    for move in moves:
        action, value = move[0], int(move[1:])
        try:
            x = waypoint[0] / abs(waypoint[0])
        except ZeroDivisionError:
            x = 0
        try:
            y = waypoint[1] / abs(waypoint[1])
        except ZeroDivisionError:
            y = 0
        waypointQuadrant = (x, y)
        if action == "F":
            ship = (ship[0] + waypoint[0] * value,
                    ship[1] + waypoint[1] * value)
        if action in ["L", "R"]:
            if waypoint == (0, 0):
                continue
            angle = (value * spin[action]) % 360
            if angle == 180:
                waypoint = (abs(waypoint[0]) *
                            waypoint_angle_map[waypointQuadrant][angle][0],
                            abs(waypoint[1]) *
                            waypoint_angle_map[waypointQuadrant][angle][1])
            else:
                waypoint = (abs(waypoint[1]) *
                            waypoint_angle_map[waypointQuadrant][angle][0],
                            abs(waypoint[0]) *
                            waypoint_angle_map[waypointQuadrant][angle][1])
        if action == "N":
            waypoint = (waypoint[0], waypoint[1] + value)
        if action == "S":
            waypoint = (waypoint[0], waypoint[1] - value)
        if action == "E":
            waypoint = (waypoint[0] + value, waypoint[1])
        if action == "W":
            waypoint = (waypoint[0] - value, waypoint[1])
    return abs(ship[0]) + abs(ship[1])


moves = [line.strip() for line in open("input.txt")]
print(one(moves))
print(two(moves))
