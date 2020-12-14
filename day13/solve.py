def one(lines):
    earliest_departure = int(lines[0])
    buses = [int(bus) for bus in lines[1].split(",") if bus != "x"]

    min_wait_time = buses[0]
    my_bus = buses[0]
    for bus_id in buses:
        wait_time = bus_id + earliest_departure - (earliest_departure %
                                                   bus_id) - earliest_departure
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            my_bus = bus_id
    return min_wait_time * my_bus


def two(lines):
    buses = [bus for bus in lines[1].split(",")]
    departures = [(int(i), int(bus_id)) for i, bus_id in enumerate(buses)
                  if bus_id != "x"]

    t = 0
    while True:
        valid = True
        for departure in departures:
            if (t + departure[0]) % departure[1] != 0:
                valid = False
        if valid:
            return t
        t += 1
        print(t)


lines = [line.strip() for line in open("example.txt").readlines()]
print(one(lines))
print(two(lines))
