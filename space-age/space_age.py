class SpaceAgeException(Exception):
    pass

class SpaceAge(object):

    earth_seconds_in_a_year = 31557600
    earth_year_by_planet = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }

    def __init__(self, seconds):
        self.seconds = seconds

    @staticmethod
    def seconds_per_year_by_planet(planet):
        if planet not in SpaceAge.earth_year_by_planet:
            raise SpaceAgeException('No such planet named %s exists', planet)
        return SpaceAge.earth_seconds_in_a_year * SpaceAge.earth_year_by_planet[planet]

    def years_on_planet(self, planet):
        return round(self.seconds / SpaceAge.seconds_per_year_by_planet(planet), 2)

    def on_mercury(self):
        return self.years_on_planet('mercury')

    def on_venus(self):
        return self.years_on_planet('venus')

    def on_earth(self):
        return self.years_on_planet('earth')

    def on_mars(self):
        return self.years_on_planet('mars')
    
    def on_jupiter(self):
        return self.years_on_planet('jupiter')

    def on_saturn(self):
        return self.years_on_planet('saturn')

    def on_uranus(self):
        return self.years_on_planet('uranus')
    
    def on_neptune(self):
        return self.years_on_planet('neptune')