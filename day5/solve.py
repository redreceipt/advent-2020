def get_seats(lines):
    seats_in_binary = [
        line.replace("F", "0").replace("B",
                                       "1").replace("L",
                                                    "0").replace("R", "1")
        for line in lines
    ]
    return [(int(seat[:7], 2), int(seat[7:], 2)) for seat in seats_in_binary]


def get_seat_ids(seats):
    return [row * 8 + column for row, column in get_seats(seats)]


def one(lines):
    return max(get_seat_ids(lines))


def two(lines):
    missing_seats = set(range(max(get_seat_ids(lines)))) - set(
        get_seat_ids(lines))
    print(missing_seats)


f = open("input.txt")
lines = f.readlines()
print(one(lines))
two(lines)
