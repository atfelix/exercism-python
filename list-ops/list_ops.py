def append(xs, ys):
    return foldl(lambda xs, y: xs + [y], ys, xs)

def concat(lists):
    return foldl(lambda acc, l: append(acc, l), lists, [])

def filter_clone(function, xs):
    return foldl(lambda acc, x: acc + [x] if function(x) else acc, xs, [])

def length(xs):
    return foldl(lambda acc, x: acc + 1, xs, 0)

def map_clone(function, xs):
    return foldl(lambda acc, x: acc + [function(x)], xs, [])

def foldl(function, xs, acc):
    for x in xs:
        acc = function(acc, x)
    return acc

def foldr(function, xs, acc):
    return foldl(lambda acc, x: function(x, acc), reverse(xs), acc)

def reverse(xs):
    return foldl(lambda acc, x: [x] + acc, xs, [])
