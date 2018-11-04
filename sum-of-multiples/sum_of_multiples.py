def sum_of_multiples(limit, multiples):
    set_of_multiples = set()

    for multiple in multiples:
        set_of_multiples.update({m for m in range(0, limit, multiple)})

    return sum(set_of_multiples)