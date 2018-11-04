class Clock(object):
    def __init__(self, hour, minute):
        minutes = 60 * hour + minute
        self.minute = minutes % 60
        self.hour = minutes // 60 % 24

    def __repr__(self):
        return '%02d:%02d' % (self.hour, self.minute)

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return self + -minutes
