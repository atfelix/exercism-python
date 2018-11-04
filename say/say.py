def say(number):
    number = int(number)
    if not is_valid(number):
        raise ValueError('Unexpected input value: input must be between 0 and 999,999,999,999 inclusively')
    
    if number == 0:
        return 'zero'

    billions_string = billions(number)
    millions_string = millions(number)
    thousands_string = thousands_and_hundreds(number)

    filtered_list = list(filter(lambda x: x, [billions_string, millions_string, thousands_string]))
    if len(filtered_list) > 1 and 'and' not in thousands_string:
        filtered_list.insert(len(filtered_list) - 1, 'and')
    return ' '.join(filtered_list)

def is_valid(number):
    return 0 <= number < 10 ** 12

def convert_three_digit_number(number):
    assert(0 <= number < 1000)

    hundreds_string = hundreds(number)
    tens_string = tens(number)
    ones_string = ones(number)

    result_string = hundreds_string

    and_string = ' and ' if (result_string and (ones_string or tens_string)) else ''
    hyphen = '-' if (tens_string and ones_string) else ''

    return hundreds_string + and_string + tens_string + hyphen + ones_string

def thousands_and_hundreds(n):
    thousands_string = thousands(n)
    hundreds_string = convert_three_digit_number(n % 1000)

    return ' '.join(filter(lambda x: x, [thousands_string, hundreds_string]))

def hundreds(n):
    assert(0 <= n < 1000)

    h = ' hundred'
    return ['', 'one' + h, 'two' + h, 'three' + h, 'four' + h,
            'five' + h, 'six' + h, 'seven' + h, 'eight' + h, 'nine' + h][n // 100]

def tens(n):
    assert(0 <= n < 1000)

    return ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'][n // 10 % 10]

def ones(n):
    assert(0 <= n < 1000)

    return ['', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine',
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
            'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'][n % 10 if n % 100 >= 20 else n % 20]

def billions(n):
    total_billions = n // (10 ** 9) % 1000
    return descriptor(total_billions, 'billion') if total_billions else ''

def millions(n):
    total_millions = n // (10 ** 6) % 1000
    return descriptor(total_millions, 'million') if total_millions else ''

def thousands(n):
    total_thousands = n // (10 ** 3) % 1000
    return descriptor(total_thousands, 'thousand', end='') if total_thousands else ''

def descriptor(n, string, end='s'):
    space = ' ' if n else ''
    return convert_three_digit_number(n) + space + string

def pluralize(string, number, end='s'):
    return string if 0 <= number <= 1 else (string + end)