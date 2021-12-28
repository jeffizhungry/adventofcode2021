import enum
import functools

class Direction(enum.Enum):
    FORWARD = 1
    UP = 2
    DOWN = 3

def compute_horizontal(data):
    def reducer(acc, delta):
        if acc is None:
            acc = 0
        if delta[0] == Direction.FORWARD:
            acc += delta[1]
        return acc
    return functools.reduce(reducer, data, 0)

def compute_depth(data):
    def reducer(acc, delta):
        if acc is None:
            acc = 0
        if delta[0] == Direction.DOWN:
            acc += delta[1]
        if delta[0] == Direction.UP:
            acc -= delta[1]
        return acc
    return functools.reduce(reducer, data, 0)

if __name__ == "__main__":
    # Parse
    input = []
    with open("input.txt", "r") as f:
        for line in f:
            raw_direction, raw_magnitude = line.split(' ')
            direction = None
            if raw_direction == "forward":
                direction = Direction.FORWARD
            elif raw_direction == "up":
                direction = Direction.UP
            elif raw_direction == "down":
                direction = Direction.DOWN
            input.append((direction, int(raw_magnitude)))

    # Part 1
    print("Horizontal:", compute_horizontal(input))
    print("Depth:", compute_depth(input))
    print("Part 1:", compute_horizontal(input) * compute_depth(input))

    # Part 2
    aim = 0
    horz = 0
    depth = 0
    for entry in input:
        direction, magnitude = entry[0], entry[1]
        if direction == Direction.UP:
            aim -= magnitude
            if aim < 0:
                aim = 0
            continue
        elif direction == Direction.DOWN:
            aim += magnitude
            continue
        elif direction == Direction.FORWARD:
            horz += magnitude
            depth += magnitude * aim
            continue
    print("Horizontal:", horz)
    print("Depth:", depth)
    print("Part 2:", horz * depth)