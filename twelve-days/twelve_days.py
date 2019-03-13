from dataclasses import dataclass

@dataclass(frozen=True)
class Verse:
    ordinal: str
    gift: str

verses = (
    Verse('first', 'a Partridge in a Pear Tree'),
    Verse('second', 'two Turtle Doves'),
    Verse('third', 'three French Hens'),
    Verse('fourth', 'four Calling Birds'),
    Verse('fifth', 'five Gold Rings'),
    Verse('sixth', 'six Geese-a-Laying'),
    Verse('seventh', 'seven Swans-a-Swimming'),
    Verse('eighth', 'eight Maids-a-Milking'),
    Verse('ninth', 'nine Ladies Dancing'),
    Verse('tenth', 'ten Lords-a-Leaping'),
    Verse('eleventh', 'eleven Pipers Piping'),
    Verse('twelfth', 'twelve Drummers Drumming')
)

def verse(number):
    other_gifts = ', '.join(verse.gift for verse in reversed(verses[1:number + 1]))
    last_verse = verses[0].gift if number == 0 else ', and ' + verses[0].gift
    return f'On the {verses[number].ordinal} day of Christmas my true love gave to me: {other_gifts}{last_verse}.'

def recite(start_verse, end_verse):
    return [verse(number) for number in range(start_verse - 1, end_verse)]
