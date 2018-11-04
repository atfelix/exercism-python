def hey(phrase):
    phrase = phrase.strip()
    if is_screaming(phrase):
        return 'Whoa, chill out!'
    elif is_question(phrase):
        return 'Sure.'
    elif say_nothing(phrase):
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'

def is_screaming(phrase):
    return (any(ch.isalpha() for ch in phrase) 
        and all(not ch.isalpha() or ch.isupper() for ch in phrase))

def say_nothing(phrase):
    return all(ch.isspace() for ch in phrase)

def is_question(phrase):
    return len(phrase) and phrase[-1] == '?'
