class Phrase(object):

    def __init__(self, verb, noun):
        self.verb = verb
        self.noun = noun

verbNounPhrases = [
    Phrase('', ''),
	Phrase('lay in', 'the house that Jack built'),
	Phrase('ate', 'the malt'),
	Phrase('killed', 'the rat'),
	Phrase('worried', 'the cat'),
	Phrase('tossed', 'the dog'),
	Phrase('milked', 'the cow with the crumpled horn'),
	Phrase('kissed', 'the maiden all forlorn'),
	Phrase('married', 'the man all tattered and torn'),
	Phrase('woke', 'the priest all shaven and shorn'),
	Phrase('kept', 'the rooster that crowed in the morn'),
	Phrase('belonged to', 'the farmer sowing his corn'),
	Phrase('', 'the horse and the hound and the horn'),
]

def recite(start_verse, end_verse):
    return list(verse(n) for n in range(start_verse, end_verse + 1))

def verse(n):
    return 'This is %s%s.' % (verbNounPhrases[n].noun, recursiveVerse(n - 1))

def recursiveVerse(n):
    if n == 0:
        return ''
    return ' that %s %s%s' % (verbNounPhrases[n].verb, verbNounPhrases[n].noun, recursiveVerse(n - 1))

