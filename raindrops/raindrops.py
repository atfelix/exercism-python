mods_and_sounds = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))

def raindrops(number):
    sounds = [sound for mod, sound in mods_and_sounds if number % mod == 0]
    return ''.join(sounds) if sounds else f'{number}'