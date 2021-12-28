import requests

def calc_increases(data: list[int]):
    num_increases = 0
    prev = None
    for curr in data:
        if prev is None:
            prev = curr
        else:
            if curr > prev:
                num_increases += 1
            prev = curr
    return num_increases

if __name__ == "__main__":
    input = []
    with open("input.txt", "r") as f:
        for x in f:
            input.append(int(x))
    print("Part 1:", calc_increases(input))

    moving_average = []
    running_average = 0
    for i, curr in enumerate(input):
        if i < 2:
            running_average += curr
            continue
        elif i == 2:
            running_average += curr
            moving_average.append(running_average)
            continue
        else:
            running_average += curr
            running_average -= input[i-3]
            moving_average.append(running_average)
            continue
    print("Part 2:", calc_increases(moving_average))