if __name__ == "__main__":
    # Parse
    input = []
    with open("input.txt", "r") as f:
        for line in f:
            input.append(line.strip())
    input = input

    # Part 1
    counts = [0] * len(input[0])
    for x in input:
        for i, digit in enumerate(x):
            if digit == "1":
                counts[i] += 1

    most_common = ""
    for c in counts:
        if c >= (len(input)/2):
            most_common += "1"
        else:
            most_common += "0"
    print("-- most common:", most_common)

    gamma = int(most_common, 2)
    mask = (1 << len(counts)) - 1
    epsilon = ~ gamma & mask
    print("-- Gamma:", gamma)
    print("-- Epislon:", epsilon)
    print("Part 1:", gamma * epsilon)
    print("")

    # Part 2
    oxygen_set = input
    oxygen_value = None
    i = 0
    while len(oxygen_set) > 1 and i < len(input[0]):
        ones_set = []
        zeros_set = []
        for x in oxygen_set:
            if x[i] == "1":
                ones_set.append(x)
            else:
                zeros_set.append(x)

        # note: equality should pref ones
        if len(ones_set) >= len(oxygen_set)/2:
            oxygen_set = ones_set
        else:
            oxygen_set = zeros_set
        i += 1
        print("-- len(oxygen_set):", len(oxygen_set))
    print("-- oxygen set:", oxygen_set)
    if len(oxygen_set) == 1:
        oxygen_value = int(oxygen_set[0], 2)
        print("-- oxygen level:", oxygen_value)

    co2_set = input
    co2_value = None
    i = 0
    while len(co2_set) > 1 and i < len(input[0]):
        ones_set = []
        zeros_set = []
        for x in co2_set:
            if x[i] == "1":
                ones_set.append(x)
            else:
                zeros_set.append(x)

        # note: equality should pref zeros
        if len(zeros_set) <= len(co2_set)/2:
            co2_set = zeros_set
        else:
            co2_set = ones_set
        print("-- len(co2_set):", len(co2_set))
        i += 1
    print("-- co2 set:", co2_set)
    if len(co2_set) == 1:
        co2_value = int(co2_set[0], 2)
        print("-- co2 level:", co2_value)

    print("Part 2:", oxygen_value * co2_value)