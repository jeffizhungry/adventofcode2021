
class BingoBoard:
    def __init__(self) -> None:
        self.data = []
        for i in range(5):
            line = []
            for j in range(5):
                line.append((-1, False))
            self.data.append(line)
        self.next_line_to_fill_index = 0

    def __str__(self):
        s = ""
        for i in range(5):
            for j in range(5):
                s += f"{str(self.data[i][j][0]).zfill(2)} "
            s += "| "
            for j in range(5):
                s += f"{self.data[i][j][1]} "
            s += "\n"
        return s

    def fill(self, line: str) -> None:
        """
        Initilize the board with this line
        """

        if self.next_line_to_fill_index >= 5:
            return
        spl = line.split()
        for i in range(5):
            self.data[self.next_line_to_fill_index][i] = (int(spl[i]), False)
        self.next_line_to_fill_index += 1

    def mark(self, n: int) -> None:
        """
        Find number on board mark and if found mark as true
        """
        for i in range(5):
            for j in range(5):
                if self.data[i][j][0] == n:
                    self.data[i][j] = (n, True)

    def is_winner(self) -> bool:
        """
        Check if there is a winning row on this board
        """
        # Check rows
        for i in range(5):
            winning_line = True
            for j in range(5):
                winning_line = winning_line and self.data[i][j][1]
            if winning_line:
                return True

        # Check cols
        for j in range(5):
            winning_line = True
            for i in range(5):
                winning_line = winning_line and self.data[i][j][1]
            if winning_line:
                return True

    def score(self) -> int:
        sum = 0
        for i in range(5):
            for j in range(5):
                if self.data[i][j][1] is False:
                    sum += self.data[i][j][0]
        return sum

if __name__ == "__main__":
    # Parse
    input = []
    with open("input.txt", "r") as f:
        input = []
        for line in f:
            input.append(line.strip())
        
    numbers = list(map(lambda x: int(x), input[0].split(",")))
    print("-- drawn numbers:", numbers)

    boards = []
    curr_board = None
    for i, line in enumerate(input[1:]):
        if i % 6 == 0:
            curr_board = BingoBoard()
        elif i % 6 > 0 and i % 6 < 5:
            curr_board.fill(line)
        elif i % 6 == 5:
            curr_board.fill(line)
            boards.append(curr_board)
            curr_board = BingoBoard()
    print("-- len(boards):", len(boards))
    
    # Part 1
    winning_number = -1
    winning_board = None
    for n in numbers:
        for b in boards:
            b.mark(n)
            if b.is_winner():
                winning_number = n
                winning_board = b
                break
        if winning_board is not None:
            break
    print("-- winning board score:", winning_board.score())
    print("-- winning board")
    print(winning_board)
    print("Part 1:", winning_number * winning_board.score())
    print("")

    # Part 2
    processing_boards = boards
    last_number = -1
    last_board = None
    for n in numbers:
        truncated = []
        for b in processing_boards:
            b.mark(n)
            if not b.is_winner():
                truncated.append(b)
            if len(processing_boards) == 1 and b.is_winner():
                last_number = n
                last_board = processing_boards[0]
                break
        if last_board is not None:
            break
        processing_boards = truncated

    print("len(processing_boards):", len(processing_boards))
    print("-- last winning board")
    print(last_board)
    print("-- last winning number")
    print(last_number)
    print("Part 2:", last_number * last_board.score())