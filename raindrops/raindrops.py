def raindrops(number):
    matches = [mod for mod in [3, 5, 7] if number % mod == 0]
    return ''.join(map(soundsFor, matches)) if matches else f'{number}'

def soundsFor(mod):
    if mod == 3:
        return 'Pling'
    elif mod == 5:
        return 'Plang'
    elif mod == 7:
        return 'Plong'
    else:
        raise ValueError('Only 3, 5 and 7 are acceptable values for this function')