from functools import total_ordering

def tally(tournament_results):
    tourney = Tournament(tournament_results)
    tourney_table = tourney.table()
    if not tourney_table:
        return 'Team                           | MP |  W |  D |  L |  P'
    return 'Team                           | MP |  W |  D |  L |  P\n' + '\n'.join(map(lambda x: x.table_string(), tourney.table()))

@total_ordering
class Team(object):

    def __init__(self, name):
        self.name = name
        self.matches_won = 0
        self.matches_lost = 0
        self.matches_drawn = 0

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.points > other.points or (self.points == other.points and self.name < other.name)
    
    def add_loss(self):
        self.matches_lost += 1
    
    def add_win(self):
        self.matches_won += 1

    def add_draw(self):
        self.matches_drawn += 1

    def table_string(self):
        return '%-30s | %2d | %2d | %2d | %2d | %2d' % (self.name,
                                                        self.matches_played,
                                                        self.matches_won,
                                                        self.matches_drawn,
                                                        self.matches_lost,
                                                        self.points)

    @property
    def matches_played(self):
        return self.matches_won + self.matches_lost + self.matches_drawn

    @property
    def points(self):
        return 3 * self.matches_won + self.matches_drawn


class Game(object):

    def __init__(self, match_string):
        self.first_team, self.second_team, self.result = match_string.split(';')


class Tournament(object):

    def __init__(self, tournament_string):
        self.teams = {}
        self.games = []

        for match_string in tournament_string.split('\n'):
            if match_string:
                self.add(Game(match_string))

    def add(self, game):
        self.games.append(game)
        first_team = self.teams.setdefault(game.first_team, Team(game.first_team))
        second_team = self.teams.setdefault(game.second_team, Team(game.second_team))

        if game.result == 'win':
            first_team.add_win()
            second_team.add_loss()
        elif game.result == 'loss':
            first_team.add_loss()
            second_team.add_win()
        else:
            first_team.add_draw()
            second_team.add_draw()
    
    def table(self):
        return sorted(self.teams.values(), reverse=True)
