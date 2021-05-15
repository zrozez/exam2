def func(*args):
    a = 0
    for i in args:
        try:
            a += i
        except TypeError:
            continue
    return a
