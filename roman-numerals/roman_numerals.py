def numeral(number):
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    thousands = ['', 'M', 'MM', 'MMM']
    answer = ''
    answer += thousands[number // 1000]
    answer += hundreds[(number % 1000) // 100]
    answer += tens[(number % 100) // 10]
    answer += ones[number % 10]
    return answer
