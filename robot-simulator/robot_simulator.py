# Globals for the bearings
# Change the values as you see fit
EAST = 1, 0
NORTH = 0, 1
WEST = -1, 0
SOUTH = 0, -1


class Robot(object):
    bearings = [EAST, SOUTH, WEST, NORTH]
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing_index = Robot.bearings.index(bearing)
        self.coordinates = x, y

    @property
    def bearing(self):
        return Robot.bearings[self.bearing_index]

    def advance(self):
        self.coordinates = (self.coordinates[0] + self.bearing[0], self.coordinates[1] + self.bearing[1])
    
    def turn_left(self):
        self.bearing_index = (self.bearing_index - 1) % len(Robot.bearings)
    
    def turn_right(self):
        self.bearing_index = (self.bearing_index + 1) % len(Robot.bearings)

    def simulate(self, string):
        scanner = Scanner(string)
        while scanner.has_next_char():
            char = scanner.get_next_char()
            if char == 'L':
                self.turn_left()
            elif char == 'R':
                self.turn_right()
            elif char == 'A':
                self.advance()

class Scanner(object):

    def __init__(self, string):
        self.string = string if string is not None else ""
        self.current_index = 0

    def has_next(self):
        return self.current_index < len(self.string)

    def has_next_char(self):
        return self.has_next() and self.string[self.current_index].isupper()

    def get_next_char(self):
        ch = self.string[self.current_index]
        self.current_index += 1
        return ch