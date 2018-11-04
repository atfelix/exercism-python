class BowlingFrame(object):
    def __init__(self):
        self.rolls = []
        self.max_pins = 10

    def __len__(self):
        return len(self.rolls)

    def roll(self, pin):
        if not self.is_active():
            return

        if not self.is_valid(pin):
            raise ValueError

        self.rolls.append(pin)
        self.max_pins -= pin

        if self.max_pins == 0:
            self.max_pins = 10

    def is_valid(self, pin):
        return 0 <= pin <= self.max_pins

    def is_active(self):
        return (len(self) < 2
                    or (len(self) == 2 and (self.is_strike() or self.is_spare())))

    def score(self):
        return sum(self.rolls)

    def is_strike(self):
        return len(self.rolls) > 0 and self.rolls[0] == 10
    
    def is_spare(self):
        return len(self.rolls) == 2 and not self.is_strike() and sum(self.rolls) == 10

    def __repr__(self):
        return ''.join(str(self.rolls))


class BowlingGame(object):
    def __init__(self, total_frames=10):
        self.number_of_total_frames = total_frames
        self.number_of_rolls = 0
        self.frames = [BowlingFrame()]

    def __len__(self):
        return len(self.frames)

    def __iter__(self):
        return iter(self.frames)

    def __next__(self):
        for frame in self:
            yield frame

    def roll(self, pin):
        if not self.can_roll():
            raise IndexError

        self.number_of_rolls += 1

        for frame in self:
            frame.roll(pin)

        if self.is_new_frame():
            self.frames.append(BowlingFrame())

    def is_new_frame(self):
        return (len(self) < self.number_of_total_frames
                    and ((self.number_of_rolls % 2) == (self.number_of_strikes() % 2)))
    
    def can_roll(self):
        return any(frame.is_active() for frame in self)
    
    def score(self):
        if not self.game_over():
            raise IndexError

        return sum(frame.score() for frame in self)

    def game_over(self):
        return self.number_of_total_frames == len(self) and not self.can_roll()

    def number_of_strikes(self):
        return sum(frame.is_strike() for frame in self)