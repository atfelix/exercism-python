sounds = {
    3: 'Pling',
    5: 'Plang',
    7: 'Plong'
}

def raindrops(number):
    matches = [mod for mod in sounds.keys() if number % mod == 0]
    return ''.join(sounds[match] for match in matches) if matches else f'{number}'
