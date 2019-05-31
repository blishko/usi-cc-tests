def increment(x):
    a = 10
    while a != 0:
        x = x + 1
        a = a - 1
        if a == 2:
            return 12
        else:
            pass
    return x

print increment(1)
