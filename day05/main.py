import argparse

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("input", help="Input data file to use")
parser.add_argument("--test", help="Set to true if this is a test input", action="store_true")
args = parser.parse_args()

def sort_point(p1: int, p2: int) -> (int, int):
    if p1 < p2:
        return (p1, p2)
    else:
        return (p2, p1)

class Point:
    def __init__(self, x, y):
        self.X = int(x)
        self.Y = int(y)
    
    def __str__(self) -> str:
        return f"({self.X}, {self.Y})"

class Line:
    def __init__(self, x1, y1, x2, y2):
        if x1 < x2:
            self.start = Point(x1, y1)
            self.end = Point(x2, y2)
        else:
            self.start = Point(x2, y2)
            self.end = Point(x1, y1)
    
    def __str__(self):
        return f"({self.start.X}, {self.start.Y}) -> ({self.end.X}, {self.end.Y})"

    def is_straight(self) -> bool:
	    return self.start.X == self.end.X or self.start.Y == self.end.Y

    def is_perfect_diagonal(self) -> bool:
        x_start, x_end = sort_point(self.start.X, self.end.X)
        y_start, y_end = sort_point(self.start.Y, self.end.Y)
        return y_end - y_start == x_end - x_start

    def enumerate_points(self):
        points = [self.start]

        if self.is_straight():
            # loop through horizontal
            incr_start, incr_end = sort_point(self.start.X, self.end.X)
            incrs = range(incr_end - incr_start)
            for i in incrs[1:len(incrs)]:
                # BUG: Since we're fixing Y, but good enough for part 1
                points.append(Point(incr_start+i, self.start.Y))

            # loop through vertical
            incr_start, incr_end = sort_point(self.start.Y, self.end.Y)
            incrs = range(incr_end - incr_start)
            for i in incrs[1:len(incrs)]:
                # BUG: Since we're fixing X, but good enough for part 1
                points.append(Point(self.start.X, incr_start + i))

        elif self.is_perfect_diagonal():
            x_start, x_end = sort_point(self.start.X, self.end.X)
            y_start, y_end = sort_point(self.start.Y, self.end.Y)
            if y_end - y_start != x_end - x_start:
                raise Exception("not a diagonal")

            incrs = range(x_end - x_start)
            if self.start.Y < self.end.Y:
                # Positive slope
                for i in incrs[1:len(incrs)]:
                    points.append(Point(x_start + i, self.start.Y + i))
            else:
                # Negative slope
                for i in incrs[1:len(incrs)]:
                    points.append(Point(x_start + i, self.start.Y - i))
            
            
        else:
            raise Exception("unsupported line type")
        
        points.append(self.end)
        return points

class Board:
    def __init__(self, size) -> None:
        self.size = size
        self.data = []
        for i in range(self.size):
            line = []
            for j in range(self.size):
                line.append(0)
            self.data.append(line)

    def __str__(self):
        s = ""
        for i in range(self.size):
            for j in range(self.size):
                s += f"{str(self.data[j][i]).zfill(1)} "
            s += "\n"
        return s
    
    def mark(self, p: Point):
        self.data[p.X][p.Y] += 1
    
    def count(self) -> int:
        result = 0
        for line in self.data:
            for point_value in line:
                if point_value >= 2:
                    result += 1
        return result

if __name__ == "__main__":
    board_size = 1000 
    if args.test:
        board_size = 10

    # Parse
    lines = []
    with open(args.input, "r") as f:
        for line in f:
            start, end = line.strip().split(" -> ")
            start_x, start_y = start.split(",")
            end_x, end_y = end.split(",")
            lines.append(Line(start_x, start_y, end_x, end_y))

    # Part 1
    board = Board(board_size)
    for line in lines:
        if not line.is_straight():
            continue
        points = line.enumerate_points()
        for p in points:
            board.mark(p)
        
    if args.test:
        print(board)
    print("Part 1:", board.count())
    print("")

    # Part 2
    board = Board(board_size)
    for line in lines:
        if not line.is_straight() and not line.is_perfect_diagonal():
            print("-- ignoring:", line)
            continue
        points = line.enumerate_points()
        for p in points:
            board.mark(p)

    if args.test:
        print(board)
    print("Part 2:", board.count())